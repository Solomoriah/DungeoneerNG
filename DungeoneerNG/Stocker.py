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


import sys, os, time, cgi, zipfile, io, glob

from . import Rooms


##############################################################################
#  Tables and Supporting Functions
##############################################################################

randenc = {}
for i in range(1, 10):
    randenc[i] = [ 0, (1, "adventurer"), ]
randenc[1].append((1, "bandit"))


for key in Monsters.monsters.keys():
    monster = Monsters.monsters[key]
    lvl = monster.get("dungeonlevel", None)
    if lvl is not None:
        if type(lvl) is int:
            lvl = (lvl,)
        for l in lvl:
            if l not in randenc:
                randenc[l] = [ 0 ]
            randenc[l].append((1, "monster", key))


class Paragraph:

    def __init__(self):
        self.category = "paragraph"
        self.text = ""


def empty_fn(withtreasure = 0):
    pass


def monster_fn(withtreasure = 0):
    pass


def special_fn(*args):
    pass


def trap_fn(withtreasure = 0):
    pass


dungeon_table = [
    0,
    (16, empty_fn, 0),
    ( 4, empty_fn, 1),
    (40, monster_fn, 0),
    (24, monster_fn, 1),
    ( 4, special_fn, 0),
    ( 8, trap_fn, 0),
    ( 4, trap_fn, 1),
]


def makedungeon(level, rooms, first = 1):

    rc = [ ]

    rc.append(Paragraph("%d Rooms on Level %d" % (rooms, level)))

    for i in range(rooms):
        roomtype = Dice.tableroller(Rooms.roomtypes)
        row = Dice.tableroller(dungeon_table)
        contents = row[1](row, level)
        items = []
        if Dice.D(1, 2) == 1 or row[2] == "Empty":
            for j in range(Dice.D(1, 3)):
                items.append(Dice.tableroller(Items.itemtable)[1])
        body.append("<p class='Text Body'>\n<b>%d. %s:</b> %s\n<p class='Text Body'>\n%s"
            % (i+first, roomtype[1], ", ".join(items), contents))

    return "\n".join(body)


# end of file.
