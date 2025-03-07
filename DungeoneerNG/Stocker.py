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

from . import Dice
from .Formatter import Paragraph
from .Treasure import Treasure
from .Monsters import Monster, monsters
from .NPCs import bandits
from .Adventurer import generate


##############################################################################
#  Tables and Supporting Functions
##############################################################################

randenc = {}
for i in range(1, 10):
    randenc[i] = [ 0, (1, "adventurer"), ]
randenc[1].append((1, "bandit"))


for key in monsters.keys():
    monster = monsters[key]
    lvl = monster.get("dungeonlevel", None)
    if lvl is not None:
        if type(lvl) is int:
            lvl = (lvl,)
        for l in lvl:
            if l not in randenc:
                randenc[l] = [ 0 ]
            randenc[l].append((1, "monster", key))


roomtypes = [
    0,
    ( 5, "Antechamber"),
    ( 3, "Armory"),
    ( 7, "Audience"),
    ( 2, "Aviary"),
    ( 7, "Banquet Room"),
    ( 4, "Barracks"),
    ( 6, "Bath"),
    (10, "Bedroom"),
    ( 2, "Bestiary"),
    ( 1, "Cell"),
    ( 1, "Chantry"),
    ( 2, "Chapel"),
    ( 1, "Cistern"),
    ( 3, "Classroom"),
    ( 8, "Closet"),
    ( 2, "Conjuring"),
    ( 5, "Corridor"),
    ( 1, "Courtroom"),
    ( 1, "Crypt"),
    ( 7, "Dining Room"),
    ( 2, "Divination Room"),
    ( 6, "Dormitory"),
    ( 4, "Dressing Room"),
    ( 3, "Gallery"),
    ( 3, "Game Room"),
    ( 4, "Great Hall"),
    ( 5, "Guardroom"),
    ( 6, "Hall"),
    ( 2, "Harem/Seraglio"),
    ( 2, "Kennel"),
    ( 6, "Kitchen"),
    ( 3, "Laboratory"),
    ( 3, "Library"),
    ( 7, "Lounge"),
    ( 3, "Meditation Room"),
    ( 2, "Museum"),
    ( 1, "Observatory"),
    ( 7, "Office"),
    ( 6, "Pantry"),
    ( 2, "Prison"),
    ( 1, "Privy"),
    ( 4, "Reception Room"),
    ( 3, "Refectory"),
    ( 2, "Robing Room"),
    ( 2, "Shrine"),
    ( 7, "Sitting Room"),
    ( 3, "Smithy"),
    ( 1, "Solar"),
    ( 4, "Stable"),
    ( 6, "Storage"),
    ( 2, "Strongroom/Vault"),
    ( 5, "Study"),
    ( 1, "Temple"),
    ( 1, "Throne Room"),
    ( 1, "Torture Chamber"),
    ( 2, "Training Room"),
    ( 2, "Trophy Room"),
    ( 8, "Vestibule"),
    ( 6, "Waiting Room"),
    ( 3, "Water Closet"),
    ( 3, "Well"),
    ( 4, "Workroom"),
    ( 6, "Workshop"),
]


itemtable = [
    0,
    (1, "animal nest"),
    (1, "anvil"),
    (1, "ash"),
    (1, "backpack"),
    (1, "bellows"),
    (1, "belt"),
    (1, "bits of fur"),
    (1, "bits of wood"),
    (1, "blanket"),
    (1, "bloodstain"),
    (1, "bones"),
    (1, "books"),
    (1, "boots"),
    (1, "bottle"),
    (1, "box"),
    (1, "branding iron"),
    (1, "broken glass"),
    (1, "broken or rusty weapons"),
    (1, "bucket"),
    (1, "burned-out torch"),
    (1, "candelabra"),
    (1, "candle"),
    (1, "chains"),
    (1, "claw marks"),
    (1, "cleaver"),
    (1, "clothing"),
    (1, "cobwebs"),
    (1, "cold spot"),
    (1, "corpse"),
    (1, "dice"),
    (1, "dripping water"),
    (1, "drum"),
    (1, "dust"),
    (1, "empty scroll case"),
    (1, "engraving"),
    (1, "flask"),
    (1, "flint and tinder"),
    (1, "fungus"),
    (1, "graffiti"),
    (1, "grinder"),
    (1, "hook"),
    (1, "horn"),
    (1, "hourglass"),
    (1, "insects"),
    (1, "jar"),
    (1, "keg"),
    (1, "key"),
    (1, "lamp"),
    (1, "lantern"),
    (1, "markings"),
    (1, "mold"),
    (1, "mud"),
    (1, "mug"),
    (1, "musical instrument"),
    (1, "mysterious stain"),
    (1, "nonmagical scroll"),
    (1, "playing cards"),
    (1, "pole"),
    (1, "pot"),
    (1, "broken pottery"),
    (1, "pottery (intact)"),
    (1, "pouch"),
    (1, "puddle of water"),
    (1, "rags"),
    (1, "razor"),
    (1, "rivulet"),
    (1, "ropes"),
    (1, "runes"),
    (1, "sack"),
    (1, "scattered stones"),
    (1, "scorch marks"),
    (1, "skull"),
    (1, "slime"),
    (1, "spices"),
    (1, "spike"),
    (1, "straw"),
    (1, "teeth"),
    (1, "tongs"),
    (1, "tools"),
    (1, "tray"),
    (1, "trophy"),
    (1, "twine"),
    (1, "urn"),
    (1, "utensils"),
    (1, "whetstone"),
]


def empty_fn(level, withtreasure):
    rc = [ ]
    if withtreasure:
        tr = Treasure()
        tr.generate("U%d" % min(8, max(1, level)))
        rc.append(tr)
    return rc


def monster_fn(level, withtreasure):
    rc = []
    row = Dice.tableroller(randenc[min(10, max(1, level))])
    if row[1] == "adventurer":
        rc.extend(generate(level))
    elif row[1] == "bandit":
        rc.extend(bandits())
    else:
        m = Monster(row[2], "dungeon")
        rc.append(m)
        if withtreasure:
            tr = Treasure()
            utyp = "U%d" % min(8, max(1, level))
            typ = getattr(m, "personaltreasure", utyp)
            for tt in typ:
                tr.generate(tt)
            rc.append(tr)
    return rc


def special_fn(*args):
    return [ Paragraph("Special"), ]


def trap_fn(level, withtreasure):
    rc = [ Paragraph("Trap") ]
    if withtreasure:
        tr = Treasure()
        tr.generate("U%d" % min(8, max(1, level)))
        rc.append(tr)
    return rc


dungeon_table = [
    0,
    (16, "Empty",                   empty_fn, 0),
    ( 4, "Empty with Treasure",     empty_fn, 1),
    (40, "Monster",                 monster_fn, 0),
    (24, "Monster with Treasure",   monster_fn, 1),
    ( 4, "Special",                 special_fn, 0),
    ( 8, "Trap",                    trap_fn, 0),
    ( 4, "Trap with Treasure",      trap_fn, 1),
]


def DungeonFactory(level, rooms, first = 1):

    rc = [ 
        Paragraph("%d Rooms on Level %d" % (rooms, level)),
    ]

    for i in range(rooms):

        roomtype = Dice.tableroller(roomtypes)
        rc.append(Paragraph("%d. %s:" % (first+i, roomtypes[1]), style = "MapKeyHeading"))

        row = Dice.tableroller(dungeon_table)
        rc.append(Paragraph(row[1]))

        if Dice.D(1, 2) == 1 or row[2] == "Empty":
            items = []
            for j in range(Dice.D(1, 3)):
                items.append(Dice.tableroller(itemtable)[1])
            rc.append(Paragraph(", ".join(items)))

        contents = row[2](level, row[3])
        if contents:
            rc.extend(contents)

    return rc


# end of file.
