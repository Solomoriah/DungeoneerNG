# Basic Fantasy RPG Dungeoneer Next Generation Suite
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


import re


xptable = {
     0: (  10,   3),
     1: (  25,  12),
     2: (  75,  25),
     3: ( 145,  30),
     4: ( 240,  40),
     5: ( 360,  45),
     6: ( 500,  55),
     7: ( 670,  65),
     8: ( 875,  70),
     9: (1075,  75),
    10: (1300,  90),
    11: (1575,  95),
    12: (1875, 100),
    13: (2175, 110),
    14: (2500, 115),
    15: (2850, 125),
    16: (3250, 135),
    17: (3600, 145),
    18: (4000, 160),
    19: (4500, 175),
    20: (5250, 200),
    21: (6000, 225),
    22: (6750, 250),
    23: (7500, 275),
    24: (8250, 300),
    25: (9000, 325),
}

# For monsters with more than 25 hit dice, add 750 XP
# to the XP Value and 25 XP to the Special Ability Bonus
# per additional hit die.


def xpcalc(hitdice):
    hitdice = hitdice.split("(")[0]
    if hitdice.startswith("1/2") or hitdice.startswith("1d2"):
        hdval = 0
    else:
        hdval = int(re.match("(\d\d*)", hitdice).group(1))
    specb = len(re.search("(\**)$", hitdice).group(1))
    if hdval in xptable:
        return xptable[hdval][0] + (xptable[hdval][1] * specb)
    topval = xptable[25]
    basexp = topval[0] + (750 * (hdval - 25))
    bonusxp = topval[1] + (25 * (hdval - 25))
    xptable[hdval] = (basexp, bonusxp)
    return basexp + (bonusxp * specb)


# end of file.
