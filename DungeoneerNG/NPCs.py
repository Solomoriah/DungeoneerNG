# Basic Fantasy RPG Dungeoneer Next Generation Suite
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

import random

from .Adventurer import *
from . import Dice, Treasure
from .Formatter import Paragraph


banditarmor = [
    0,
    ( 4, "leather armor", 13 ),
    ( 1, "chain mail", 15 ),
]

piratearmor = [
    0,
    ( 1, "leather armor", 13 ),
    ( 2, "", 11 ),
]

banditweapons = [
    0,
    ( 7, "battle axe", 1, "1d8" ),
    ( 6, "shortsword", 1, "1d6" ),
    ( 7, "longsword", 1, "1d8" ),
    ( 2, "scimitar", 1, "1d8" ),
    ( 2, "spear", 2, "1d6" ),
]

crewweapons = [
    0,
    ( 2, "club", 1, "1d4" ),
    ( 1, "dagger", 1, "1d4" ),
    ( 1, "shortsword", 1, "1d6" ),
]

merchantweapons = [
    0,
    ( 6, "shortsword", 1, "1d6" ),
    ( 2, "longsword", 1, "1d8" ),
    ( 3, "dagger", 1, "1d4" ),
]


class Bandit(Character):

    def outfit(self, ldr = 0):

        if ldr:
            a = Dice.tableroller(banditarmor)
            self.armor = a[1]
            self.armorvalue = a[2]
        else:
            self.armor = "Leather Armor"
            self.armorvalue = 13

        if ldr:
            magicarmor(self, 5)

        self.calc()

        b = Dice.tableroller(banditweapons)
        self.meleeweapon = b[1]
        self.damage = b[3]

        if ldr:
            magicweapon(self, 5)
            self.potion = genpotion(self.clas, self.level)
            self.scroll = genscroll(self.clas, self.level)


class Pirate(Character):

    def outfit(self, ldr = 0):

        a = Dice.tableroller(piratearmor)
        self.armor = a[1]
        self.armorvalue = a[2]

        if ldr:
            magicarmor(self, 5)

        self.calc()

        w = Dice.tableroller(banditweapons)
        self.meleeweapon = w[1]
        self.damage = w[3]

        if ldr:
            magicweapon(self, 5)
            self.potion = genpotion(self.clas, self.level)
            self.scroll = genscroll(self.clas, self.level)


def magicarmor(c, chance):
    if Dice.D(1, 100) > max(10, min(95, c.level * chance)):
        return
    if c.armor == "":
        return
    bonus = Dice.tableroller(armorbonus)[1]
    c.armor = "%s +%d" % (c.armor, bonus)
    c.armorvalue = c.armorvalue + bonus


def magicweapon(c, chance):
    if Dice.D(1, 100) > max(15, min(95, c.level * chance)):
        return
    bonus = Dice.tableroller(meleeweaponbonus)[1]
    c.meleeweapon = "%s %s" % (c.meleeweapon, bonus)
    c.damage = "%s%s" % (c.damage, bonus)


pilgrimarmor = [ 
    armortypes[0],
    [ 0,
        [ 1, "chain mail", 15 ],
    ],
    armortypes[2],
    armortypes[3],
]

pilgrimweapons = [
    meleeweapons[0],
    [ 0,
        [ 1, "longsword", 1, "1d8" ],
    ],
    meleeweapons[2],
    meleeweapons[3],
]

class Pilgrim(Character):

    def __init__(self, level = 1, clas = None, race = None):
        Character.__init__(self, level, clas, 0, 1, booststats = 0, race = race)

    def outfit(self):

        armor = Dice.tableroller(pilgrimarmor[self.clas])

        # is armor magical?
        chance = 5
        if self.clas == 2:
            chance = 4
        if Dice.D(1, 100) < min(95, self.level * chance):
            bonus = Dice.tableroller(armorbonus)[1]
            armor[1] = "<b>%s +%d</b>" % (armor[1], bonus)
            armor[2] = armor[2] + bonus
        self.armor = armor[1]
        self.armorvalue = armor[2]

        wpn = Dice.tableroller(pilgrimweapons[self.clas])

        # is weapon magical?
        chance = 5
        if self.clas == 2:
            chance = 3
        if Dice.D(1, 100) < min(95, self.level * chance):
            bonus = Dice.tableroller(meleeweaponbonus)[1]
            wpn[1] = "<b>%s %s</b>" % (wpn[1], bonus)
            wpn[3] = "%s %s" % (wpn[3], bonus)
        self.meleeweapon = wpn[1]
        self.damage = wpn[3]

        self.calc()


def nobles():

    party = []
    party_race = None

    return party


def pilgrims():

    party = []
    party_race = None

    # 1d4 clerics of level 1d4 each
    clrs = Dice.D(1, 4)
    nums = []
    for i in range(clrs):
        nums.append(Dice.D(1, 4))
    nums = sorted(nums, reverse = True)

    party.append(Paragraph("<b>%d Cleric%s:</b>" % (clrs, ("", "", "s")[min(clrs,2)])))

    for i in range(clrs):
        clr_ch = Pilgrim(nums[i], 0, race = party_race)
        party.append(clr_ch)
        # a group of pilgrims is likely all of a single race
        if i == 0:
            party_race = clr_ch.race

    # 3d6 normal men
    nm_ch = Character(0, 1, 0, 1, avgstats = 1, booststats = 0, race = party_race)
    nm_ch.noapp = Dice.D(3, 6)
    nm_ch.rollhp()
    nm_ch.name = ""

    party.append(Paragraph("<b>%d Normal Pilgrims:</b>" % nm_ch.noapp))
    party.append(nm_ch)

    # 1d6 fighters of level 1d4 each
    #   in chainmail, with longswords
    ftrs = Dice.D(1, 6)
    nums = []
    for i in range(ftrs):
        nums.append(Dice.D(1, 4))
    nums = sorted(nums, reverse = True)
    party.append(Paragraph("<b>%d Fighter%s:</b>" % (ftrs, ("", "", "s")[min(ftrs,2)])))
    for i in range(ftrs):
        party.append(Pilgrim(nums[i], 1, race = party_race))

    # 1d4 thieves of level 1d4 each
    #   50% devout, 50% on the lam (will add note later)
    thfs = Dice.D(1, 4)
    nums = []
    for i in range(thfs):
        nums.append(Dice.D(1, 4))
    nums = sorted(nums, reverse = True)
    party.append(Paragraph("<b>%d Thie%s:</b>" % (thfs, ("", "f", "ves")[min(thfs,2)])))
    for i in range(thfs):
        party.append(Pilgrim(nums[i], 3, race = party_race))

    # 50% 1 magic-user of level 1d4
    mus = 0
    if party_race in ("Human", "Elf"):
        mus = Dice.D(1, 2) - 1
    if mus:
        party.append(Paragraph("<b>1 Magic-User:</b>"))
        party.append(Pilgrim(Dice.D(1, 4), 2, race = party_race))

    # mules or horses (50% each)
    #   equal to number of pilgrims

    # type A treasure (as offering)
    tr = Treasure.Treasure()
    tr.generate("A")
    if len(tr) > 0:
        party.append(Paragraph("<b>Treasure (as Offering to the Gods):</b>"))
        party.append(tr)

    return party


def nobles():
    party = []
    return party


def bandits():

    # how many flunkies?

    ftrs = Dice.D(2, 12)
    thfs = Dice.D(1, 6)

    # if there are 11 or more mooks, a fighter
    # and a thief will lead them; otherwise,
    # 50% chance of either.

    lftr = 0
    lthf = 0

    if (ftrs + thfs) >= 11:
        lftr = Dice.D(1, 4) + 1
        lthf = Dice.D(1, 4) + 1
    else:
        if Dice.D(1, 100) <= 50:
            lftr = Dice.D(1, 4) + 1
        else:
            lthf = Dice.D(1, 4) + 1

    party = []

    if lftr > 0:
        character = Bandit(lftr, 1)
        character.outfit(1)
        party.append(character)

    if lthf > 0:
        character = Bandit(lthf, 3)
        character.outfit(1)
        party.append(character)

    nftrs = ftrs

    while nftrs:
        character = Bandit(1, 1)
        character.outfit(0)
        character.name = ""
        character.noapp = min(nftrs, Dice.D(1, ftrs))
        nftrs -= character.noapp
        party.append(character)

    nthfs = thfs

    while nthfs:
        character = Bandit(1, 3)
        character.outfit(0)
        character.name = ""
        character.noapp = min(nthfs, Dice.D(1, thfs))
        nthfs -= character.noapp
        party.append(character)

    for character in party:
        if character.noapp > 1:
            character.hitpoints = []
            for i in range(character.noapp):
                character.hitpoints.append(character.rollhp())

    return party


def pirates():

    party = []

    # how many flunkies?

    mooks = Dice.D(3, 8)
    mates = Dice.D(1, 3)

    # captain
    character = Pirate(Dice.D(1, 4) + 2, 1)
    character.outfit(1)
    character.name = "Captain " + character.name
    party.append(character)

    # mates
    for i in range(mates):
        character = Pirate(Dice.D(1, 4) + 1, 1)
        character.outfit(1)
        party.append(character)

    # mooks

    nmooks = mooks

    while nmooks:
        character = Pirate(1, 1)
        character.outfit(0)
        character.name = ""
        character.noapp = min(nmooks, Dice.D(1, mooks))
        nmooks -= character.noapp
        character.hitpoints = []
        for i in range(character.noapp):
            character.hitpoints.append(character.rollhp())
        party.append(character)

    return party


class Merchant(Character):

    def __init__(self, teamsters = None, race = None):
        if teamsters:
            Character.__init__(self, 0, 1, 0, 1, avgstats = 1, booststats = 0, race = race)
            self.noapp = teamsters
            self.rollhp()
            # should never be fewer than 2 teamsters
            self.name = "%d Teamsters" % teamsters
        else:
            level = 0
            if Dice.D(1, 100) < 20:
                level = min(Dice.D(1, 3), Dice.D(1, 3))
            Character.__init__(self, level, 1, 0, 1, booststats = 0, race = race)
            self.noapp = 1
            # boost intelligence, wisdom, charisma if bad
            for thestat in (1, 2, 5):
                self.stats[thestat] = max(self.stats[thestat], Dice.D(3, 6), 9)

    def outfit(self, ldr = 0):

        self.armor = "Leather Armor"
        self.armorvalue = 13

        if ldr:
            magicarmor(self, 5)

        self.calc()

        b = Dice.tableroller(merchantweapons)
        self.meleeweapon = b[1]
        self.damage = b[3]

        if ldr:
            magicweapon(self, 5)


class MerchantCrew(Character):

    def outfit(self):

        self.armor = ""
        self.armorvalue = 11

        self.calc()

        w = Dice.tableroller(crewweapons)
        self.meleeweapon = w[1]
        self.damage = w[3]


def merchants():

    party = []

    # 50% of a single merchant, 50% 1d4+1

    num_merch = 1
    if Dice.D(1, 100) >= 50:
        num_merch = Dice.D(1, 4, 1)

    party.append(Paragraph("<b>%d Merchant%s:</b>" % (num_merch, ("", "", "s")[min(num_merch,2)])))

    worker_races = []

    for i in range(num_merch):
        m = Merchant()
        worker_races.append(m.race)
        party.append(m)

    worker_race = random.choice(worker_races)

    num_wagons = max(num_merch, Dice.D(2, 4, 0))

    party.append(Paragraph("<b>%d Wagons, with Teamsters:</b>" % num_wagons))

    party.append(Merchant(teamsters = num_wagons, race = worker_race))

    party += merchant_guards()
    party += merchant_treasure()

    return party


def merchantship():

    party = []

    party.append(Paragraph("<b>The Merchant:</b>"))

    m = Merchant()
    worker_race = m.race
    party.append(m)

    party.append(Paragraph("<b>The Crew:</b>"))

    num = crew_count = Dice.D(2, 8, 8)

    officer = MerchantCrew(0, 1)
    officer.name = "Captain %s" % officer.name.split()[0]
    officer.meleeweapon = "Longsword"
    officer.damage = "1d8"
    party.append(officer)

    officer = MerchantCrew(0, 1)
    officer.name = "First Mate %s" % officer.name.split()[0]
    officer.meleeweapon = "Longsword"
    officer.damage = "1d8"
    party.append(officer)

    num -= 2

    while num > 0:
        crew = MerchantCrew(0, 1)
        if num > (crew_count // 2):
            crew.noapp = min(num, Dice.D(2, 6))
            num -= crew.noapp
        else:
            crew.noapp = num
            num = 0
        crew.name = "%d Crewmen" % crew.noapp
        crew.rollhp()
        party.append(crew)

    party += merchant_guards()
    party += merchant_treasure()

    return party


def merchant_guards():

    party = []

    lvl2 = Dice.D(1, 4)
    lvl1 = Dice.D(1, 4, 2)

    party.append(Paragraph("<b>%d Guards:</b>" % (lvl1+lvl2)))

    lvl2ch = Character(2, 1, actuallevel = 2, outfit = 1)
    lvl2ch.name = ""
    lvl2ch.noapp = lvl2
    lvl2ch.rollhp()
    party.append(lvl2ch)

    lvl1ch = Character(1, 1, actuallevel = 1, outfit = 1)
    lvl1ch.name = ""
    lvl1ch.noapp = lvl1
    lvl1ch.rollhp()
    party.append(lvl1ch)

    return party


def merchant_treasure():

    tr = Treasure.Treasure()
    tr.generate("A0M")

    if len(tr) < 1:
        return []

    return [ Paragraph("<b>Treasure:</b>"), tr ]


def generate(typ):
    if typ == "b":
        party = bandits()
    elif typ == "p":
        party = pirates()
    elif typ == "ms":
        party = merchantship()
    elif typ == "m":
        party = merchants()
    elif typ == "n":
        party = nobles()
    elif typ == "pg":
        party = pilgrims()
    return party


if __name__ == "__main__":

    party = bandits()
    print(htmlshowparty(party))


# end of file.
