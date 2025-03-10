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

###############################################################################
#  Treasure.py -- generate treasures for Basic Fantasy RPG
###############################################################################


from . import Gems, Art, Coins, Magic, Unknown, Dice, ODT

from collections import UserList


def _gen_coins(argtup):
    kind, n, s, b, mul = argtup
    return [ Coins.Coin(kind, (Dice.D(n, s, b) * mul)) ]


def _gen_gems(argtup):
    n, s, b, mul = argtup
    lst = []
    qty = Dice.D(n, s, b) * mul
    while qty > 0:
        n = 1
        if qty > 6:
            if qty > 12:
                n = Dice.D(1, 12, 0)
            else:
                n = Dice.D(1, 6, 0)
        qty -= n
        lst = lst + [ Gems.Gem(n) ]
    return lst


def _gen_art(argtup):
    n, s, b, mul = argtup
    lst = []
    qty = Dice.D(n, s, b) * mul
    while qty > 0:
        n = 1
        objdart = Art.Art()
        if objdart.maxqty > 1:
            n = min(objdart.maxqty, qty)
            if n > 1:
                n = Dice.D(1, n, 0)
        qty -= n
        objdart.qty = n
        lst.append(objdart)
    return lst


def __gen_magic(argtup):
    kind, n, s, b, mul = argtup
    lst = []
    qty = Dice.D(n, s, b) * mul
    for i in range(qty):
        lst = lst + [ Magic.Magic(kind) ]
    return lst


def _gen_magic(argtup):
    if type(argtup) is type([]):
        lst = []
        for i in argtup:
            lst = lst + __gen_magic(i)
        return lst
    else:
        return __gen_magic(argtup)


_treasure_table = {

    # lair treasure

    'A': [
            (50, _gen_coins, ("cp", 5,  6, 0, 100)),
            (60, _gen_coins, ("sp",  5, 6, 0, 100)),
            (40, _gen_coins, ("ep", 5,  4, 0, 100)),
            (70, _gen_coins, ("gp", 10,  6, 0, 100)),
            (50, _gen_coins, ("pp",  1,  10, 0, 100)),
            (50, _gen_gems,  (6, 6, 0, 1)),
            (50, _gen_art,   (6, 6, 0, 1)),
            (30, _gen_magic, ("Any", 0, 0, 3, 1)),
         ],
    'B': [
            (75, _gen_coins, ("cp", 5,  10, 0,  100)),
            (50, _gen_coins, ("sp", 5,  6, 0,  100)),
            (50, _gen_coins, ("ep",  5, 4, 0,  100)),
            (50, _gen_coins, ("gp",  3, 6, 0,  100)),
            (25, _gen_gems,  (1, 6, 0, 1)),
            (25, _gen_art,   (1, 6, 0, 1)),
            (10, _gen_magic, ("AW", 0, 0, 1, 1)),
         ],
    'C': [
            (60, _gen_coins, ("cp", 6, 6, 0,  100)),
            (60, _gen_coins, ("sp", 5,  4, 0,  100)),
            (30, _gen_coins, ("ep",  2,  6, 0,  100)),
            (25, _gen_gems,  (1, 4, 0, 1)),
            (25, _gen_art,   (1, 4, 0, 1)),
            (15, _gen_magic, ("Any", 1, 2, 0, 1)),
         ],
    'D': [
            (30, _gen_coins, ("cp", 4, 6, 0,  100)),
            (45, _gen_coins, ("sp", 6, 6, 0,  100)),
            (90, _gen_coins, ("gp", 5, 8, 0,  100)),
            (30, _gen_gems,  (1, 8, 0, 1)),
            (30, _gen_art,   (1, 8, 0, 1)),
            (20, _gen_magic, [
                    ("Any",    1, 2, 0, 1),
                    ("Potion", 0, 0, 1, 1),
                ]
            ),
         ],
    'E': [
            (30, _gen_coins, ("cp",  2,  8, 0,  100)),
            (60, _gen_coins, ("sp",  6, 10, 0,  100)),
            (50, _gen_coins, ("ep",  3,  8, 0,  100)),
            (50, _gen_coins, ("gp",  4, 10, 0,  100)),
            (10, _gen_gems,  (1, 10, 0, 1)),
            (10, _gen_art,   (1, 10, 0, 1)),
            (30, _gen_magic, [
                    ("Any",    1, 4, 0, 1),
                    ("Scroll", 0, 0, 1, 1),
                ]
            ),
         ],
    'F': [
            (40, _gen_coins, ("sp",  3,  8, 0, 100)),
            (50, _gen_coins, ("ep",  4,  8, 0, 100)),
            (85, _gen_coins, ("gp",  6, 10, 0, 100)),
            (70, _gen_coins, ("pp",  2,  8, 0, 100)),
            (20, _gen_gems,  (2, 12, 0, 1)),
            (20, _gen_art,   (1, 12, 0, 1)),
            (35, _gen_magic, [
                    ("NonWpn", 1, 4, 0, 1),
                    ("Scroll", 0, 0, 1, 1),
                    ("Potion", 0, 0, 1, 1),
                ]
            ),
         ],
    'G': [
            (90, _gen_coins, ("gp",  4, 6, 0, 1000)),
            (75, _gen_coins, ("pp",  5, 8, 0,  100)),
            (25, _gen_gems,  (3,  6, 0, 1)),
            (25, _gen_art,   (1, 10, 0, 1)),
            (50, _gen_magic, [
                    ("Any",    1, 4, 0, 1),
                    ("Scroll", 0, 0, 1, 1),
                ]
            ),
         ],
    'H': [
            (75, _gen_coins, ("cp",  8, 10, 0,  100)),
            (75, _gen_coins, ("sp",  6, 10, 0, 1000)),
            (75, _gen_coins, ("ep",  3, 10, 0, 1000)),
            (75, _gen_coins, ("gp",  5,  8, 0, 1000)),
            (75, _gen_coins, ("pp",  9,  8, 0,  100)),
            (50, _gen_gems,  ( 1, 100, 0, 1)),
            (50, _gen_art,   (10,   4, 0, 1)),
            (20, _gen_magic, [
                    ("Any",    1, 4, 0, 1),
                    ("Scroll", 0, 0, 1, 1),
                    ("Potion", 0, 0, 1, 1),
                ]
            ),
         ],
    'I': [
            (80, _gen_coins, ("pp", 3, 10, 0, 100)),
            (50, _gen_gems,  (2, 6, 0, 1)),
            (50, _gen_art,   (2, 6, 0, 1)),
            (15, _gen_magic, ("Any", 0, 0, 1, 1)),
         ],
    'J': [
            (45, _gen_coins, ("cp", 3,  8, 0, 100)),
            (45, _gen_coins, ("sp", 1,  8, 0, 100)),
         ],
    'K': [
            (90, _gen_coins, ("cp", 2, 10, 0, 100)),
            (35, _gen_coins, ("sp", 1,  8, 0, 100)),
         ],
    'L': [
            (50, _gen_gems,  (1, 4, 0, 1)),
         ],
    'M': [
            (90, _gen_coins, ("gp", 4, 10, 0,  100)),
            (90, _gen_coins, ("pp", 2,  8, 0, 1000)),
         ],
    'N': [
            (40, _gen_magic, ("Potion", 2, 4, 0, 1)),
         ],
    'O': [
            (50, _gen_magic, ("Scroll", 1, 4, 0, 1)),
         ],

    # personal treasure

    'P': [
            (100, _gen_coins, ("cp", 3, 8, 0, 1)),
         ],
    'Q': [
            (100, _gen_coins, ("sp", 3, 6, 0, 1)),
         ],
    'R': [
            (100, _gen_coins, ("ep",  2, 6, 0, 1)),
         ],
    'S': [
            (100, _gen_coins, ("gp",  2, 4, 0, 1)),
         ],
    'T': [
            (100, _gen_coins, ("pp",  1, 6, 0, 1)),
         ],
    'U': [
            ( 50, _gen_coins, ("cp", 1, 20, 0, 1)),
            ( 50, _gen_coins, ("sp", 1, 20, 0, 1)),
            ( 25, _gen_coins, ("gp", 1, 20, 0, 1)),
            (  5, _gen_gems,  (1, 4, 0, 1)),
            (  5, _gen_art,   (1, 4, 0, 1)),
            (  2, _gen_magic, ("Any", 0, 0, 1, 1)),
         ],
    'V': [
            ( 25, _gen_coins, ("sp", 1, 20, 0, 1)),
            ( 25, _gen_coins, ("ep", 1, 20, 0, 1)),
            ( 50, _gen_coins, ("gp", 1, 20, 0, 1)),
            ( 25, _gen_coins, ("pp", 1, 20, 0, 1)),
            ( 10, _gen_gems,  (1, 4, 0, 1)),
            ( 10, _gen_art,   (1, 4, 0, 1)),
            (  5, _gen_magic, ("Any", 0, 0, 1, 1)),
         ],

    'U1': [
            ( 75, _gen_coins, ("cp", 1, 8, 0, 100)),
            ( 50, _gen_coins, ("sp", 1, 6, 0, 100)),
            ( 25, _gen_coins, ("ep", 1, 4, 0, 100)),
            (  7, _gen_coins, ("gp", 1, 4, 0, 100)),
            (  1, _gen_coins, ("pp", 1, 4, 0, 100)),
            (  7, _gen_gems,  (1, 4, 0, 1)),
            (  3, _gen_art,   (1, 4, 0, 1)),
            (  2, _gen_magic, ("Any", 0, 0, 1, 1)),
    ],

    'U2': [
            ( 50, _gen_coins, ("cp", 1, 10, 0, 100)),
            ( 50, _gen_coins, ("sp", 1, 8, 0, 100)),
            ( 25, _gen_coins, ("ep", 1, 6, 0, 100)),
            ( 20, _gen_coins, ("gp", 1, 6, 0, 100)),
            (  2, _gen_coins, ("pp", 1, 4, 0, 100)),
            ( 10, _gen_gems,  (1, 6, 0, 1)),
            (  7, _gen_art,   (1, 4, 0, 1)),
            (  5, _gen_magic, ("Any", 0, 0, 1, 1)),
    ],

    'U3': [
            ( 30, _gen_coins, ("cp", 2, 6, 0, 100)),
            ( 50, _gen_coins, ("sp", 1, 10, 0, 100)),
            ( 25, _gen_coins, ("ep", 1, 8, 0, 100)),
            ( 50, _gen_coins, ("gp", 1, 6, 0, 100)),
            (  4, _gen_coins, ("pp", 1, 4, 0, 100)),
            ( 15, _gen_gems,  (1, 6, 0, 1)),
            (  7, _gen_art,   (1, 6, 0, 1)),
            (  8, _gen_magic, ("Any", 0, 0, 1, 1)),
    ],

    'U45': [
            ( 20, _gen_coins, ("cp", 3, 6, 0, 100)),
            ( 50, _gen_coins, ("sp", 2, 6, 0, 100)),
            ( 25, _gen_coins, ("ep", 1, 10, 0, 100)),
            ( 50, _gen_coins, ("gp", 2, 6, 0, 100)),
            (  8, _gen_coins, ("pp", 1, 4, 0, 100)),
            ( 20, _gen_gems,  (1, 8, 0, 1)),
            ( 10, _gen_art,   (1, 6, 0, 1)),
            ( 12, _gen_magic, ("Any", 0, 0, 1, 1)),
    ],

    'U67': [
            ( 15, _gen_coins, ("cp", 4, 6, 0, 100)),
            ( 50, _gen_coins, ("sp", 3, 6, 0, 100)),
            ( 25, _gen_coins, ("ep", 1, 12, 0, 100)),
            ( 70, _gen_coins, ("gp", 2, 8, 0, 100)),
            ( 15, _gen_coins, ("pp", 1, 4, 0, 100)),
            ( 30, _gen_gems,  (1, 8, 0, 1)),
            ( 15, _gen_art,   (1, 6, 0, 1)),
            ( 16, _gen_magic, ("Any", 0, 0, 1, 1)),
    ],

    'U8': [
            ( 10, _gen_coins, ("cp", 5, 6, 0, 100)),
            ( 50, _gen_coins, ("sp", 5, 6, 0, 100)),
            ( 25, _gen_coins, ("ep", 2, 8, 0, 100)),
            ( 75, _gen_coins, ("gp", 4, 6, 0, 100)),
            ( 30, _gen_coins, ("pp", 1, 4, 0, 100)),
            ( 40, _gen_gems,  (1, 8, 0, 1)),
            ( 30, _gen_art,   (1, 8, 0, 1)),
            ( 20, _gen_magic, ("Any", 0, 0, 1, 1)),
    ],

    # coinage

    'cp': [
            (100, _gen_coins, ("cp", 0, 0, 1, 1)),
         ],
    'sp': [
            (100, _gen_coins, ("sp", 0, 0, 1, 1)),
         ],
    'ep': [
            (100, _gen_coins, ("ep",  0, 0, 1, 1)),
         ],
    'gp': [
            (100, _gen_coins, ("gp",  0, 0, 1, 1)),
         ],
    'pp': [
            (100, _gen_coins, ("pp",  0, 0, 1, 1)),
         ],

    # extra stuff

    'ART':          [ (100, _gen_art,   (0, 0, 1, 1)), ],

    # magic classes

    'MAGIC':        [ (100, _gen_magic, ("Any", 0, 0, 1, 1)), ],
    'POTION':       [ (100, _gen_magic, ("Potion", 0, 0, 1, 1)), ],
    'SCROLL':       [ (100, _gen_magic, ("Scroll", 0, 0, 1, 1)), ],
    'CLSCROLL':     [ (100, _gen_magic, ("CLScroll", 0, 0, 1, 1)), ],
    'MUSCROLL':     [ (100, _gen_magic, ("MUScroll", 0, 0, 1, 1)), ],
    'PROSCROLL':    [ (100, _gen_magic, ("ProScroll", 0, 0, 1, 1)), ],
    'WAND':         [ (100, _gen_magic, ("Wand", 0, 0, 1, 1)), ],
    'STAFF':        [ (100, _gen_magic, ("Staff", 0, 0, 1, 1)), ],
    'WSR':          [ (100, _gen_magic, ("WSR", 0, 0, 1, 1)), ],
    'MISC':         [ (100, _gen_magic, ("Misc", 0, 0, 1, 1)), ],
    'RARE':         [ (100, _gen_magic, ("Rare", 0, 0, 1, 1)), ],
    'ARMOR':        [ (100, _gen_magic, ("Armor", 0, 0, 1, 1)), ],
    'WEAPON':       [ (100, _gen_magic, ("Weapon", 0, 0, 1, 1)), ],
}

_treasure_table['U4'] = _treasure_table['U45']
_treasure_table['U5'] = _treasure_table['U45']
_treasure_table['U6'] = _treasure_table['U67']
_treasure_table['U7'] = _treasure_table['U67']


def Types():
    types = _treasure_table.keys()
    ones = list(filter(lambda x: len(x) == 1, types))
    mults = list(filter(lambda x: len(x) > 1, types))
    ones.sort()
    mults.sort()
    return ones + mults


class Treasure(UserList):

    def __init__(self, init = None):
        self.category = "treasure"
        self.treasuretypes = []
        if init is None:
            self.data = []
        else:
            self.data = init

    def generate(self, typ):
        typ = typ.upper()
        self.treasuretypes.append(typ)
        if typ in _treasure_table:
            tbl = _treasure_table[typ]
            for i in tbl:
                if Dice.D(1, 100, 0) <= i[0]:
                    self.extend(i[1](i[2]))
        else:
            self.append(Unknown.Unknown(typ))
        self.combine()

    def combine(self):
        self.data = sorted(self.data)
        hits = 1
        while hits:
            hits = 0
            for i in range(len(self.data) - 1):
                if self[i] is not None and self[i+1] is not None:
                    if self[i].cat == self[i+1].cat \
                    and self[i].name == self[i+1].name \
                    and self[i].value == self[i+1].value:
                        self[i].qty += self[i+1].qty
                        self[i+1] = None
                        hits += 1
            if hits:
                self.data = list(filter(lambda x: x is not None, self.data))

    def to_html(self):

        rc = []

        for t in self.data:
            article = "a"
            if t.shortname[0].lower() in "aeiou":
                article = "an"
            t.textvalue = "{:,.0f}".format(t.value)
            t.textqty = "{:,.0f}".format(t.qty)
            if t.cat == "Magic":
                if t.qty > 1:
                    rc.append("%s <b>%s</b>" % (t.textqty, t.shortname.lower()))
                else:
                    rc.append("%s <b>%s</b>" % (article, t.shortname.lower()))
            elif t.cat == "Coin":
                rc.append("%s %s" % (t.textqty, t.shortname.lower()))
            elif t.value > 0:
                if t.qty == 1:
                    rc.append("%s %s (worth %s gp)" % (article, t.shortname.lower(), t.textvalue))
                else:
                    rc.append("%s %s (worth %s gp)" % (t.textqty, t.shortname.lower(), t.textvalue))
            else:
                rc.append("%s %s" % (t.textqty, t.shortname.lower()))

        if len(rc) < 3:
            return "Treasure: %s" % " and ".join(rc)

        if len(rc) > 0:
            return "Treasure: %s, and %s" % (", ".join(rc[:-1]), rc[-1])

        return "Treasure: (nothing)"

    def to_odt(self):
        return ODT.textbody(ODT.fixbold(self.to_html()))


# end of script.
