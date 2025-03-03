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
        if "alternatetable" in m:
            oldm = m
            m = _Monsters.monsters[Dice.tableroller(m["alternatetable"])[1]]
            m["alternatetable"] = oldm["alternatetable"]
            m["allunique"] = oldm.get("allunique", 0)
        for key in m.keys():
            setattr(self, key, m[key])
        self.hitpoints = []
        self.noapp = 1
        if noapp is not None:
            self.noapp = noapp
        elif mode != "one":
            roll = getattr(self, "noapproll%s" % mode, (0, 0, 1))
            if type(roll) is tuple:
                self.noapp = Dice.D(*roll)
        for i in range(self.noapp):
            self.hitpoints.append(max(1, Dice.D(*self.hitdiceroll)))
        myequipment = getattr(self, "equipment", None)
        wpntbl = getattr(self, "weapontable", None)
        if wpntbl:
            # weapon tables need to start with a primary weapon; code below
            # avoids running too many loops looking for one randomly by
            # selecting the first after 6 tries.
            self.baseattack = getattr(self, "baseattack", '')
            self.basedamage = getattr(self, "basedamage", '')
            primary = None
            secondary = None
            for i in range(6):
                wpn = Dice.tableroller(wpntbl)
                if wpn[2]:
                    secondary = (wpn[1], wpn[3], wpn[-1])
                else:
                    primary = (wpn[1], wpn[3], wpn[-1])
                    break
            if primary is None:
                wpn = wpntbl[1]
                primary = (wpn[1], wpn[3], wpn[-1])
            if secondary is None:
                secondary = (None, None, None)
            if myequipment is not None:
                self.equipment = ", ".join(filter(None, [ primary[2], secondary[2], myequipment ]))
            self.noattacks = "%s %s" % (self.baseattack, " or ".join(filter(None, [ primary[0], secondary[0] ])))
            self.damage = ", ".join(filter(None, [ self.basedamage, primary[1], secondary[1] ]))


trollkin_table = {
    1: 'Trollkin, Infant, 1 HD',
    2: 'Trollkin, Infant, 2 HD',
    3: 'Trollkin, Juvenile, 3 HD',
    4: 'Trollkin, Juvenile, 4 HD',
    5: 'Trollkin, Adolescent, 5 HD',
    6: 'Trollkin, Adolescent, 6 HD',
}


def trollwifelair_generator(m):

    roll = Dice.D(1, 10, 0)

    if roll == 1:
        return [ m ]

    if roll > 3:
        return [ m, Monster('Troll', 'one') ]

    rc = [ m ]
    nkin = Dice.D(1, 6, 0)
    kinhd = Dice.D(2, 6, 0)
    while (kinhd / nkin) > 6.0:
        nkin += 1

    basekinhd = kinhd // nkin
    remain = kinhd % nkin

    # now we know the size of the trollkin;
    #   remain are basekinhd+1,
    #   nkin - remain are basekinhd
    # generate them in that order

    if remain:
        rc.append(Monster(trollkin_table[basekinhd+1], noapp = remain))
    rc.append(Monster(trollkin_table[basekinhd], noapp = (nkin - remain)))

    return rc


generators = {
    'trollwifelair': trollwifelair_generator,
}


def MonsterFactory(name, mode = "one"):

    if mode == "one":
        return [ Monster(name, mode) ]

    prime = Monster(name, mode)

    if hasattr(prime, "alternatetable"):
        # to begin with, we're effectively discarding prime here
        alt_track = { }
        allunique = getattr(prime, "allunique", 0)
        for row in prime.alternatetable[1:]:
            alt_track[row[1]] = 0
        for i in range(prime.noapp):
            row = Dice.tableroller(prime.alternatetable)
            alt_track[row[1]] += 1
        # now we know how many there are, let's create them.
        rc = []
        for row in prime.alternatetable[1:]:
            if alt_track[row[1]]:
                if allunique:
                    for i in range(alt_track[row[1]]):
                        rc.append(Monster(row[1], "one"))
                else:
                    rc.append(Monster(row[1], noapp = alt_track[row[1]]))
        return rc

    roll = getattr(prime, "noapproll%s" % mode, None)
    if type(roll) is type('') and roll in generators:
        return generators[roll](prime)

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
