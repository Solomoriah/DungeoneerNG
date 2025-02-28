# Basic Fantasy RPG Dungeoneer Suite
# Copyright 2007-2024 Chris Gonnerman
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
#  Magic.py -- generate magic items
###############################################################################

from . import Dice, Spells, _Treasure


###############################################################################
#  Here is the entire magic-item generation table from the 
#  Basic Fantasy RPG Core Rules 4thEd Release 139
###############################################################################


def _typify(row):
    addl = Dice.MRoll(row[2])
    return (0, row[1] % addl[1])


def _quantify(row):
    num = Dice.D(*row[2])
    return (0, row[1] % num)


def _genscroll(row):
    spells = Spells.genscroll(*row[2])
    return (0, "%s: %s" % (row[1], ", ".join(spells)))


_form_tables = {
    "A": [
        ( 1, "Bell"),
        ( 1, "Chime"),
        ( 2, "Belt"),
        ( 1, "Girdle"),
        ( 8, "Boots"),
        ( 2, "Bowl"),
        (13, "Cloak"),
        ( 2, "Crystal Ball"),
        ( 1, "Orb"),
        ( 2, "Drums"),
        ( 5, "Helm"),
        ( 5, "Horn"),
        ( 3, "Lens"),
        ( 3, "Mirror"),
        ( 9, "Medallion"),
        ( 9, "Pendant"),
        (33, "Ring"),
    ],
    "B": [
        (25, "Boots"),
        (25, "Pendant"),
        (50, "Ring"),
    ],
    "C": [
        (40, "Pendant"),
        (60, "Ring"),
    ],
    "D": [
        (17, "Lens"),
        ( 4, "Mirror"),
        ( 9, "Medallion"),
        (20, "Pendant"),
        (50, "Ring"),
    ],
    "E": [
        (40, "Helm"),
        (40, "Pendant"),
        (20, "Ring"),
    ],
    "F": [
        ( 7, "Belt or Girdle"),
        (31, "Cloak"),
        (12, "Pendant"),
        (50, "Ring"),
    ],
    "G": [
        (17, "Bell or Chime"),
        (33, "Drums"),
        (50, "Horn"),
    ],
    "H": [
        (17, "Bowl"),
        (40, "Crystal Ball"),
        (10, "Orb"),
        (33, "Mirror"),
    ],
}

def _miscform(row):
    myargs = row[2]
    myform = Dice.MRoll(_form_tables[myargs[0]])
    title = "%s of %s" % (myform[1], row[1])
    if len(myargs) > 1 and type(myargs[1]) is list:
        addl = Dice.MRoll(myargs[1])
        return (0, title % addl)
    if len(myargs) == 3:
        return (0, title % Dice.D(myargs[1], myargs[2]))
    return (0, title)


_potion_table = [
    (3, "Potion of Clairaudience"),
    (3, "Potion of Clairvoyance"),
    (2, "Potion of Cold Resistance"),
    (3, "Potion of Animal Control"),
    (2, "Potion of Dragon Control"),
    (3, "Potion of Giant Control"),
    (3, "Potion of Human Control"),
    (3, "Potion of Plant Control"),
    (3, "Potion of Undead Control"),
    (7, "Potion of Delusion"),
    (3, "Potion of Diminution"),
    (4, "Potion of Fire Resistance"),
    (4, "Potion of Flying"),
    (4, "Potion of Gaseous Form"),
    (4, "Potion of Giant Strength"),
    (4, "Potion of Growth"),
    (4, "Potion of Healing"),
    (4, "Potion of Heroism"),
    (5, "Potion of Invisibility"),
    (4, "Potion of Invulnerability"),
    (4, "Potion of Levitation"),
    (4, "Potion of Longevity"),
    (4, "Potion of Mind Reading"),
    (2, "Potion of Poison"),
    (3, "Potion of Polymorph Self"),
    (8, "Potion of Speed"),
    (3, "Potion of Treasure Finding"),
]

_cleric_scroll_table = [
    ( 3, "Scroll of One Clerical Spell",        (0, 1), _genscroll),
    ( 3, "Scroll of Two Clerical Spells",       (0, 2), _genscroll),
    ( 2, "Scroll of Three Clerical Spells",     (0, 3), _genscroll),
    ( 1, "Scroll of Four Clerical Spells",      (0, 4), _genscroll),
]

_magic_user_scroll_table = [
    ( 6, "Scroll of One Magic-User Spell",      (2, 1), _genscroll),
    ( 5, "Scroll of Two Magic-User Spells",     (2, 2), _genscroll),
    ( 5, "Scroll of Three Magic-User Spells",   (2, 3), _genscroll),
    ( 4, "Scroll of Four Magic-User Spells",    (2, 4), _genscroll),
    ( 3, "Scroll of Five Magic-User Spells",    (2, 5), _genscroll),
    ( 2, "Scroll of Six Magic-User Spells",     (2, 6), _genscroll),
    ( 1, "Scroll of Seven Magic-User Spells",   (2, 7), _genscroll),
]

_protection_scroll_table = [
    (10, "Scroll of Protection from Lycanthropes"),
    (14, "Scroll of Protection from Undead"),
    ( 6, "Scroll of Protection from Elementals"),
    ( 5, "Scroll of Protection from Magic"),
]

_scroll_table = [
    ( 9, "Clerical Scroll",     _cleric_scroll_table),
    (26, "Magic-User Scroll",   _magic_user_scroll_table),
    ( 5, "Cursed Scroll"),
    (35, "Protection Scroll",   _protection_scroll_table),
    (10, "Map to Type A Treasure"),
    ( 4, "Map to Type E Treasure"),
    ( 3, "Map to Type G Treasure"),
    ( 8, "Map to %d Magic Items", (1, 4), _quantify),
]

_spell_storing_table = [
    (24, "1"),
    (24, "2"),
    (19, "3"),
    (14, "4"),
    (10, "5"),
    ( 5, "6"),
    ( 4, "7"),
]

_effects_1_table = [
    ( 1, "Blasting",                        ("G",), _miscform),
    ( 4, "Blending",                        ("F",), _miscform),
    ( 8, "Cold Resistance",                 ("F",), _miscform),
    ( 5, "Control Animal",                  ("C",), _miscform),
    ( 7, "Control Human",                   ("C",), _miscform),
    ( 6, "Control Plant",                   ("C",), _miscform),
    ( 2, "Courage",                         ("G",), _miscform),
    ( 3, "Deception",                       ("F",), _miscform),
    (11, "Delusion",                        ("A",), _miscform),
    ( 3, "Djinni Summoning",                ("C",), _miscform),
    ( 1, "Doom",                            ("G",), _miscform),
    (11, "Fire Resistance",                 ("F",), _miscform),
    (13, "Invisibility",                    ("F",), _miscform),
    ( 5, "Levitation",                      ("F",), _miscform),
    (10, "Mind Reading",                    ("C",), _miscform),
    ( 2, "Panic",                           ("G",), _miscform),
    ( 2, "Penetrating Vision",              ("D",), _miscform),
]

_effects_2_table = [
    ( 7, "Protection +1",                   ("F",), _miscform),
    ( 3, "Protection +2",                   ("F",), _miscform),
    ( 1, "Protection +3",                   ("F",), _miscform),
    ( 3, "Protection from Energy Drain",    ("F",), _miscform),
    ( 6, "Protection from Scrying",         ("F",), _miscform),
    ( 3, "Regeneration",                    ("C",), _miscform),
    ( 6, "Scrying",                         ("H",), _miscform),
    ( 3, "Scrying, Superior",               ("H",), _miscform),
    ( 7, "Speed",                           ("B",), _miscform),
    ( 3, "%s Spell Storing",
                       ("C", _spell_storing_table), _miscform),
    ( 8, "Spell Turning",                   ("F",), _miscform),
    (19, "Stealth",                         ("B",), _miscform),
    ( 3, "Telekinesis",                     ("C",), _miscform),
    ( 2, "Telepathy",                       ("C",), _miscform),
    ( 2, "Teleportation",                   ("C",), _miscform),
    ( 2, "True Seeing",                     ("D",), _miscform),
    (10, "Water Walking",                   ("B",), _miscform),
    (11, "Weakness",                        ("C",), _miscform),
    ( 1, "%d Wishes",                  ("C", 1, 4), _miscform),
]

_misc_items_table = [
    (57, "Subtable 1", _effects_1_table),
    (43, "Subtable 2", _effects_2_table),
]

_staff_table = [
    ( 5, "Snake Staff"),
    ( 4, "Staff of Commanding"),
    (11, "Staff of Healing"),
    ( 2, "Staff of Power"),
    ( 4, "Staff of Striking"),
    ( 1, "Staff of Wizardry"),
]

_wand_table = [
    ( 5, "Wand of Cold"),
    ( 5, "Wand of Enemy Detection"),
    ( 5, "Wand of Fear"),
    ( 5, "Wand of Fireballs"),
    ( 5, "Wand of Illusion"),
    ( 5, "Wand of Lightning Bolts"),
    ( 8, "Wand of Magic Detection"),
    ( 6, "Wand of Paralyzation"),
    ( 5, "Wand of Polymorphing"),
    ( 8, "Wand of Secret Door Detection"),
    ( 8, "Wand of Trap Detection"),
]

_wandstaffrod_table = [
    ( 8, "Rod of Cancellation"),
    (27, "Staff",   _staff_table),
    (65, "Wand",    _wand_table),
]

_elemental_summoning = [
    (1, "Bowl of Summoning Water Elementals"),
    (1, "Brazier of Summoning Fire Elementals"),
    (1, "Censer of Summoning Air Elementals"),
    (1, "Crucible of Summoning Metal Elementals"),
    (1, "Mallet of Summoning Wood Elementals"),
    (1, "Marble Plate of Summoning Cold Elementals"),
    (1, "Rod of Summoning Lightning Elementals"),
    (1, "Stone of Summoning Earth Elementals"),
]

_rare_items_table = [
    (2, "Bag of Devouring"),
    (6, "Bag of Holding"),
    (5, "Boots of Traveling and Leaping"),
    (6, "Broom of Flying"),
    (6, "Elemental Summoning", _elemental_summoning),
    (1, "Efreeti Bottle"),
    (2, "Flying Carpet"),
    (7, "Gauntlets of Ogre Power"),
    (2, "Girdle of Giant Strength"),
    (1, "Mirror of Imprisonment"),
    (5, "Rope of Climbing"),
]

_special_enemy_table = [
    (1, "Lycanthropes"),
    (1, "Spell Users"),
    (1, "Undead"),
    (1, "Dragons"),
    (1, "Regenerators"),
    (1, "Enchanted Monsters"),
]

_special_ability_table = [
    (9, "Casts Light 30' on Command"),
    (3, "Locate Objects"),
    (4, "Flames on Command"),
    (1, "Drains Energy"),
    (1, "%d Wishes", (1, 4), _quantify),
    (2, "Charm Person"),
]

_roll_again_weapon_table = [
    (40, "+1, %s", _special_ability_table, _typify),
    (10, "+2, %s", _special_ability_table, _typify),
    ( 5, "+3, %s", _special_ability_table, _typify),
    ( 2, "+4, %s", _special_ability_table, _typify),
    ( 1, "+5, %s", _special_ability_table, _typify),
    # NOTE:  This table should include +1/+2 and +1/+3 options
    #        but presently does not.
]

_weapon_adjustment_table = [
    (40, "+1"),
    (10, "+2"),
    ( 5, "+3"),
    ( 2, "+4"),
    ( 1, "+5"),
    (17, "+1, +2 vs. %s", _special_enemy_table, _typify),
    (10, "+1, +3 vs. %s", _special_enemy_table, _typify),
    (10, "Roll Again plus Special Ability", _roll_again_weapon_table),
    ( 3, "Cursed, -1",    0),
    ( 2, "Cursed, -2",    0),
]

_missile_weapon_adjustment_table = [
    (46, "+1"),
    (12, "+2"),
    ( 6, "+3"),
    (18, "+1, +2 vs. %s", _special_enemy_table, _typify),
    (12, "+1, +3 vs. %s", _special_enemy_table, _typify),
    ( 4, "Cursed, -1",    0),
    ( 2, "Cursed, -2",    0),
]

_sword_type_table = [
    ( 5, "Shortsword %s", _weapon_adjustment_table, _typify),
    (11, "Longsword %s", _weapon_adjustment_table, _typify),
    ( 2, "Scimitar %s", _weapon_adjustment_table, _typify),
    ( 2, "Greatsword %s", _weapon_adjustment_table, _typify),
]

_axe_type_table = [
    ( 5, "Hand Axe %s", _weapon_adjustment_table, _typify),
    (13, "Battle Axe %s", _weapon_adjustment_table, _typify),
    ( 2, "Great Axe %s", _weapon_adjustment_table, _typify),
]

_mace_type_table = [
    ( 5, "Hammer %s", _weapon_adjustment_table, _typify),
    (13, "Mace %s", _weapon_adjustment_table, _typify),
    ( 2, "Maul (Great Hammer) %s", _weapon_adjustment_table, _typify),
]

_arrow_type_table = [
    (14, "Shortbow Arrows %s", _missile_weapon_adjustment_table, _typify),
    ( 6, "Longbow Arrows %s", _missile_weapon_adjustment_table, _typify),
]

_bolts_type_table = [
    (14, "Light Crossbow Bolts %s", _missile_weapon_adjustment_table, _typify),
    ( 6, "Heavy Crossbow Bolts %s", _missile_weapon_adjustment_table, _typify),
]

_bow_type_table = [
    (14, "Shortbow %s", _missile_weapon_adjustment_table, _typify),
    ( 6, "Longbow %s", _missile_weapon_adjustment_table, _typify),
]

_polearm_type_table = [
    ( 5, "Spear %s", _weapon_adjustment_table, _typify),
    (11, "Pike %s", _weapon_adjustment_table, _typify),
    ( 2, "Longspear %s", _weapon_adjustment_table, _typify),
    ( 2, "Halberd %s", _weapon_adjustment_table, _typify),
]

_weapon_type_table = [
    (18, "Sword", _sword_type_table),
    ( 9, "Dagger %s", _weapon_adjustment_table, _typify),
    ( 9, "Axe", _axe_type_table),
    ( 9, "Mace", _mace_type_table),
    (11, "Arrows", _arrow_type_table),
    (11, "Bolts", _bolts_type_table),
    ( 9, "Bow", _bow_type_table),
    ( 4, "Sling %s", _missile_weapon_adjustment_table, _typify),
    ( 9, "Polearm", _polearm_type_table),
]

_cursed_armor_table = [
    (50, "-1"),
    (30, "-2"),
    (10, "-3"),
]

_armor_adjustment_table = [
    (50, "+1"),
    (30, "+2"),
    (10, "+3"),
    ( 5, "Cursed", _cursed_armor_table),
    ( 5, "Cursed, Armor Class 11"),
]

_shield_adjustment_table = [
    (50, "+1"),
    (30, "+2"),
    (10, "+3"),
    ( 5, "Cursed", _cursed_armor_table),
]

_armor_type_table = [
    ( 9, "Leather Armor %s", _armor_adjustment_table, _typify),
    (19, "Chain Mail %s", _armor_adjustment_table, _typify),
    (15, "Plate Mail %s", _armor_adjustment_table, _typify),
    (57, "Shield %s", _shield_adjustment_table, _typify),
]

_wpn_armor_table = [
    (70, "Weapons", _weapon_type_table),
    (30, "Armor",   _armor_type_table),
]

_magic_table = [
    (25, "Weapon",          _weapon_type_table),
    (10, "Armor",           _armor_type_table),
    (20, "Potion",          _potion_table),
    (30, "Scroll",          _scroll_table),
    ( 5, "Misc",            _misc_items_table),
    ( 5, "Wand/Staff/Rod",  _wandstaffrod_table),
    ( 5, "Rare",            _rare_items_table),
]

_non_weapon_item_table = [
    (10, "Armor",          _armor_type_table),
    (20, "Potion",         _potion_table),
    (30, "Scroll",         _scroll_table),
    ( 5, "Misc",           _misc_items_table),
    ( 5, "Wand/Staff/Rod", _wandstaffrod_table),
    ( 5, "Miscellaneous",  _rare_items_table),
]


class Magic(_Treasure.Item):

    __magic_switch = {
        "ANY":          _magic_table,
        "POTION":       _potion_table,
        "CLSCROLL":     _cleric_scroll_table,
        "MUSCROLL":     _magic_user_scroll_table,
        "PROSCROLL":    _protection_scroll_table,
        "SCROLL":       _scroll_table,
        "WPNARMOR":     _wpn_armor_table,
        "NONWPN":       _non_weapon_item_table,
        "MISC":         _misc_items_table,
        "WAND":         _wand_table,
        "STAFF":        _staff_table,
        "WSR":          _wandstaffrod_table,
        "RARE":         _rare_items_table,
        "ARMOR":        _armor_type_table,
        "WEAPON":       _weapon_type_table,
    }

    def __init__(self, kind = "Any"):
        _Treasure.Item.__init__(self)
        self.cat = "Magic"
        self.fullcat = self.fullcat + "." + self.cat
        row = Dice.MRoll(self.__magic_switch[kind.upper()])
        self.name = self.shortname = row[1]
        if len(row) > 3:
            self.desc = row[3]

    def __str__(self):
        s = self.cat + ": "
        if self.qty != 1:
            s = s + " " + str(self.qty)
        s = s + " " + self.name
        if self.desc:
            s = s + (" [%d sub-items]" % len(self.desc))
        return s


###############################################################################
#  Test Main
###############################################################################

if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        # args should be [ [ n ] t ]
        if len(sys.argv) == 2:
            n = 1
            t = sys.argv[1]
        else:
            n = int(sys.argv[1])
            t = sys.argv[2]
        for i in range(n):
            print(Magic(t))
    else:
        print(Magic())


# end of file.
