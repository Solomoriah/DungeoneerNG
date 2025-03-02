# Basic Fantasy RPG Dungeoneer Suite
# Copyright 2007-2025 Chris Gonnerman
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# Redistributions of source code must retain the above copyright
# notice, self list of conditions and the following disclaimer.
#
# Redistributions in binary form must reproduce the above copyright
# notice, self list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution.
#
# Neither the name of the author nor the names of any contributors
# may be used to endorse or promote products derived from self software
# without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# AUTHOR OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


try:
    from DungeoneerNG import _Monsters, Dice
except:
    import _Monsters, Dice


monsters = _Monsters.monsters

class Monster(object):

    def __init__(self, name, mode = "one", noapp = None):
        self.category = "monster"
        m = _Monsters.monsters[name]
        for key in m.keys():
            setattr(self, key, m[key])
        self.hitpoints = []
        if noapp is not None:
            self.noapp = noapp
        elif mode != "one":
            roll = getattr(self, "noapproll%s" % mode, (0, 0, 1))
            self.noapp = Dice.D(*roll)
        else:
            self.noapp = 1
        for i in range(self.noapp):
            self.hitpoints.append(max(1, Dice.D(*self.hitdiceroll)))


def MonsterFactory(name, mode = "one"):

    if mode == "one":
        return [ Monster(name, mode) ]

    prime = Monster(name, mode)
    if not hasattr(prime, "leaders"):
        return [ prime ]

    totalapp = prime.noapp
    rc = [ prime ]

    last_ldr = None
    for num_m, ldr_mode, ldr_single, ldr_name, ldr_odds in prime.leaders:
        if num_m and totalapp < num_m:
            continue
        if (ldr_mode == "all" or ldr_mode == mode) and Dice.rollunder(ldr_odds):
            if ldr_single == 2 and ldr_name == last_ldr:
                continue
            last_ldr = ldr_name
            if ldr_single:
                nldr = 1
            else:
                nldr = totalapp // num_m
            prime.noapp -= nldr
            prime.hitpoints = prime.hitpoints[:prime.noapp]
            rc.append(Monster(ldr_name, noapp = nldr))

    return rc


# end of file.
