# Basic Fantasy RPG Dungeoneer Suite
# Copyright 2007-2026 Chris Gonnerman
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

from . import _CoreEncounters, Dice, Monsters, NPCs, Adventurer
from .Formatter import Paragraph

dungeon_encounters = _CoreEncounters.dungeon_encounters
wilderness_encounters = _CoreEncounters.wilderness_encounters
city_encounters = _CoreEncounters.city_encounters


def generate(type_fld, level_fld):

    if type_fld == "wilderness":
        tbl = wilderness_encounters.get(level_fld, None)
    elif type_fld == "city":
        tbl = city_encounters.get(level_fld, None)
    else:
        tbl = dungeon_encounters.get(level_fld, None)
    if tbl is None:
        return [ Paragraph("%s %s not found." % (type_fld, level_fld)) ]

    row = Dice.Roll(tbl)

    if type_fld == "dungeon":
        tag = "Level %s" % level_fld
    else:
        tag = level_fld.capitalize()

    rc = [
        Paragraph("%s %s Encounter: %s" % (tag, type_fld.capitalize(), row[2]), style = "SubHeading"),
    ]

    if row[1] == "monster":
        if row[2] in Monsters.monsters:
            return rc + Monsters.MonsterFactory(row[2], mode = type_fld)
    elif row[1] == "npc":
        if row[2] == "Bandit":
            return rc + NPCs.bandits()
        elif row[2] == "Pirate":
            return rc + NPCs.pirates()
        elif row[2] == "Buccaneer":
            return rc + NPCs.pirates()
        elif row[2] == "Adventurer":
            return rc + Adventurer.generate(level_fld)
        elif row[2] == "Merchant":
            return rc + NPCs.merchants()
        elif row[2] == "Merchant Ship":
            return rc + NPCs.merchantship()
#        elif row[2] == "Pilgrim":
#        elif row[2] == "Noble":

#    elif row[1] == "npcenc":

    return [ Paragraph("Fell Through %s %s -> %s %s" % (type_fld, level_fld, row[1], row[2])) ]


# end of file.
