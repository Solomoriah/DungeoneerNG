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

from . import _CoreEncounters, Dice, Monsters, NPCs, Adventurer, Treasure
from .Formatter import Paragraph

dungeon_encounters = _CoreEncounters.dungeon_encounters
wilderness_encounters = _CoreEncounters.wilderness_encounters
city_encounters = _CoreEncounters.city_encounters


def nullenc():
    return [ Paragraph("Null Encounter") ]

def beggar():
    nms = 0
    thfs = 0
    for i in range(Dice.D(2, 4)):
        if Dice.D(1, 10) == 1: # thief
            thfs += 1
        else:
            nms += 1
    rc = []
    while thfs:
        nthfs = Dice.D(1, thfs)
        thfs -= nthfs
        if nthfs > 1:
            character = Adventurer.Character(1, 3, avgstats = 1, booststats = 0, race = "Human")
        else:
            character = Adventurer.Character(1, 3)
        m = Dice.tableroller(Adventurer.nmweapons)
        character.meleeweapon = m[1]
        character.damage = m[3]
        if nthfs > 1:
            character.name = ""
        character.noapp = nthfs
        character.rollhp()
        rc.append(character)
    while nms:
        nnms = Dice.D(1, nms)
        nms -= nnms
        character = Adventurer.Character(0, 1, 0, avgstats = 1, booststats = 0, race = "Human")
        character.name = ""
        character.noapp = nnms
        character.rollhp()
        rc.append(character)
    return rc

def bully():
    nms = 0
    ftrs = 0
    for i in range(Dice.D(2, 4)):
        if Dice.D(1, 10) <= 3: # fighter
            ftrs += 1
        else:
            nms += 1
    rc = []
    while ftrs:
        nftrs = Dice.D(1, ftrs)
        ftrs -= nftrs
        if nftrs > 1:
            character = Adventurer.Character(1, 1, outfit = 0, avgstats = 1, booststats = 0, race = "Human")
        else:
            character = Adventurer.Character(1, 1, outfit = 0)
        m = Dice.tableroller(Adventurer.nmweapons)
        character.meleeweapon = m[1]
        character.damage = m[3]
        if nftrs > 1:
            character.name = ""
        character.noapp = nftrs
        character.rollhp()
        rc.append(character)
    while nms:
        nnms = Dice.D(1, nms)
        nms -= nnms
        character = Adventurer.Character(0, 1, 0, avgstats = 1, booststats = 0, race = "Human")
        character.name = ""
        character.noapp = nnms
        character.rollhp()
        rc.append(character)
    return rc

def citywatch():
    sergeant = Adventurer.Character(Dice.D(1, 3, 1), 1, race = "Human")
    sergeant.name = "Sergeant " + sergeant.name.split()[0]
    squad = Adventurer.Character(1, 1, avgstats = 1, booststats = 0, race = "Human")
    squad.name = ""
    squad.noapp = Dice.D(2, 6) - 1
    squad.rollhp()
    squad.meleeweapon = sergeant.meleeweapon
    squad.damage = sergeant.damage
    squad.shield = sergeant.shield
    squad.shieldvalue = sergeant.shieldvalue
    squad.calc()
    return [ sergeant, squad ]

def mercenary():
    return citywatch() # close enough, and heading will be different

def merchant():

    party = []

    # merchants

    merchants = Dice.D(1, 4)
    party.append(Paragraph("<b>%d Merchants:</b>" % merchants))

    for i in range(merchants):
        m = NPCs.Merchant()
        t = Treasure.Treasure().generate("S", "T", "V")
        m.items += t.item_list()
        party.append(m)

    # guards

    guards = Dice.D(1, 4, 1)
    lvl2 = Dice.D(1, guards)
    lvl1 = guards - lvl2

    party.append(Paragraph("<b>%d Guards:</b>" % (lvl1+lvl2)))

    for i in range(lvl2):
        lvl2ch = Adventurer.Character(2, 1, actuallevel = 2, outfit = 1)
        party.append(lvl2ch)

    if lvl1:
        lvl1ch = Adventurer.Character(1, 1, actuallevel = 1, outfit = 1)
        if lvl1 > 1:
            lvl1ch.name = ""
            lvl1ch.noapp = lvl1
            lvl1ch.rollhp()
        party.append(lvl1ch)

    return party

pressgangweapons = [
    0,
    ( 5, "club", 1, "1d4" ),
    ( 4, "fist", 1, "1d3" ),
]

class PressGang(Adventurer.Character):

    def outfit(self, ldr = 0):

        a = Dice.tableroller(NPCs.piratearmor)
        self.armor = a[1]
        self.armorvalue = a[2]
        self.calc()

        w = Dice.tableroller(pressgangweapons)
        self.meleeweapon = w[1]
        self.damage = w[3]

def pressgang():
    rc = []
    noapp = Dice.D(2, 6)
    noldr = 1
    if noapp > 7:
        noldr = 2
    noapp -= noldr
    ldrlvls = []
    for i in range(noldr):
        ldrlvls.append(Dice.D(1, 4, 1))
    for lvl in sorted(ldrlvls, reverse = True):
        leader = PressGang(lvl, 1)
        rc.append(leader)
    while noapp:
        squad = PressGang(1, 1, avgstats = 1, booststats = 0, race = rc[0].race)
        squad.name = ""
        squad.noapp = Dice.D(1, noapp)
        noapp -= squad.noapp
        squad.rollhp()
        rc.append(squad)
    return rc

priesttable = [
    0,
    ( 3, 0, (1, 4)),
    (21, 1, (0, 0)),
    ( 7, 1, (1, 4)),
    ( 5, 3, (1, 4)),
    ( 1, 2, (1, 4)),
]

def priest():
    rc = []
    maxclr = None
    maxclrlvl = 0
    for n in range(Dice.D(1, 4, 1)):
        odds, cclass, levelroll = Dice.tableroller(priesttable)
        level = 0
        if levelroll[0]:
            level = Dice.D(*levelroll)
        member = NPCs.Pilgrim(level, cclass)
        if member.clas == 0 and member.level > maxclrlvl:
            maxclr = n
            maxclrlvl = member.level
        rc.append(member)
    if maxclr is None:
        rc[0] = NPCs.Pilgrim(Dice.D(1, 4), 0)
    else:
        thecleric = rc.pop(maxclr)
        rc = [ thecleric ] + rc
    return rc

def thief():
    noapp = Dice.D(1, 6) - 1
    rc = [
        Adventurer.Character(Dice.D(1, 3, 1), 3)
    ]
    for i in range(noapp):
        rc.append(Adventurer.Character(1, 3))
    return rc

def wizard():
    noapp = Dice.D(1, 4)
    rc = [
        Adventurer.Character(Dice.D(1, 4, 3), 2)
    ]
    for i in range(noapp - 1):
        rc.append(Adventurer.Character(1, 2))
    return rc


npcenc = { 
    "Beggar":       beggar,
    "Bully":        bully,
    "City Watch":   citywatch,
    "Mercenary":    mercenary,
    "Merchant":     merchant,
    "Press Gang":   pressgang,
    "Priest":       priest,
    "Thief":        thief,
    "Wizard":       wizard,
}


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
        elif row[2] == "Pilgrim":
            return rc + NPCs.pilgrims()
        elif row[2] == "Noble":
            return rc + NPCs.nobles()
    elif row[1] == "npcenc":
        return rc + npcenc.get(row[2], nullenc)()

    return [ Paragraph("Fell Through %s %s -> %s %s" % (type_fld, level_fld, row[1], row[2])) ]


# end of file.
