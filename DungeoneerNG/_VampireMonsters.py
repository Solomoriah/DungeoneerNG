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

monsters = {
    "Vampire Spawn, 3 HD": {

        "armorclass": "14 (m)",
        "attackbonus": 3,
        "damage": "1d6+1 punch or 1d8+1 or by weapon +1 or 1d3 bite or no gaze",
        "description": [
            "Vampires are undead monsters.  Though they may look just a bit more pale than when they were alive, they do appear to live and even breathe as mortals do (though they do not, in fact, need to breathe to survive).  A vampire has all the memories and abilities it had in life, and is effectively immortal.  Living forever in the shadows often leads to vampires being decadent, while their hunger for blood makes them cruel.",
            "When a human (or, at the GMs option, some other living humanoid) is turned into a vampire it is called a vampire spawn.  Spawn normally begin with 3 hit dice; if a humanoid having more than 3 hit dice is turned, it will begin as a spawn with the number of hit dice it had in life, up to a maximum of 6.  Vampires who are able to feed regularly gain one hit die about every 10 years; some advance faster, some slower, and the GM may wish to roll 2d8+1 for the number of years a given vampire will need to advance a hit die (rolling again after each such gain).",
            "Vampires regenerate in a similar fashion to trolls, recovering 1 hit point per turn (not round) after damage is suffered.  Much like trolls, some forms of damage inflicted upon a vampire cannot be regenerated, such as damage from contact with holy water or exposure to sunlight.  This is called \"permanent damage\" though it can be healed by consuming life energy, as explained in the following paragraph.  Vampires do not heal \"normally\" as living creatures do, but can regain such lost hit points by drinking blood from living creatures.",
            "The vampire's bite inflicts 1d3 points of damage, then each round thereafter one energy level is drained from the victim.  Each level of energy drain inflicted permits the vampire to heal one point of permanent damage, or to regenerate a number of points of ordinary damage equal to the number of hit points lost by the victim.  If using the bite as an attack in combat, the vampire suffers a penalty of -5 to Armor Class due to the vulnerable position it must assume.",
            "If exposed to direct sunlight, the vampire will suffer 3d8 points of permanent damage each round.  Even a partial exposure inflicts 1d8 points of permanent damage.  No saving throw normally applies.",
            "If a vampire's victim is slain by the vampire's bite, the victim will arise as a vampire spawn at the next sunset (but not less than 12 hours later) and thereafter will be under the complete control of the \"parent\" vampire (the \"sire\") until such time as either victim or parent are destroyed.  This transformation can be prevented by driving a stake through the heart of the victim before it arises as a vampire (so long as the stake remains in place until after the event would have occurred).  Alternately, the victim can be recovered by casting restoration followed by raise dead.  One level of energy drain will be restored by this procedure.",
            "Vampires cast no reflections in silvered mirrors or water, though despite conventional wisdom to the contrary they do cast reflections in most other reflective materials; the innate purity of silver and water simply will not reflect them.",
            "Vampires are strong.  As shown on the table above, spawn receive a bonus of +1 to damage inflicted by melee weapons due to this strength, while more mature vampires receive a bonus of +2 or even +3.  Thus, a vampire will generally choose to use a melee weapon (or even its bare hands) in combat rather than attempting to bite.",
            "Vampires are unharmed by non-magical weapons, and like all undead are immune to sleep, charm, and hold spells.",
            "A vampire can be held at bay by several things, including the smell of garlic, a silver or silvered mirror, or a holy symbol presented by a believer (GM's discretion is advised here, but in general someone threatened by a vampire may be more devout than usual).  In such a situation the vampire cannot approach within 5 feet of the repellent item or character, nor can it make any melee attacks or otherwise touch those within the warded area.  If it can summon animals (see below), it can still direct them to attack.",
            "Fresh running water (such as a stream or river) acts as a barrier to a vampire; one cannot cross over any such waterway, neither by bridge or by waterway or even by flying.  It is possible for a vampire to be carried across while lying in its own coffin with the lid closed; the presence of the water flowing beneath the coffin will force the vampire to remain dormant.  Being immersed in running water causes 3d8 points of permanent damage each round.  Of course, vampires are damaged by holy water just with as all other undead monsters.",
            "A vampire may not enter any private dwelling without being invited by someone who resides there, and then only if invited while the resident is actually inside the structure.  Public buildings of any sort do not present this problem; even private rooms in inns are fully accessible to a vampire.",
            "If reduced to 0 hit points in combat, but still able to regenerate at least some of that damage, the vampire is not destroyed.  The vampire will begin to regenerate 1 hit point per turn after 2d6 turns, and may resume normal activity as soon as the first point is restored.  Do not tally negative hit points for a vampire, even if you do so for characters and/or monsters otherwise; if permanent damage is applied to a vampire which is dormant due to normal damage, the permanent damage is considered to override the same number of points of normal damage.",
            "Vampires of 7 hit dice or more are sires, maintaining control of all their own vampire spawn, and are no longer controlled by their own vampiric sire.  New vampires created by those having fewer than 7 hit dice are under the control of the creator's sire; when the creator reaches 7 hit dice it assumes control of all of its own spawn.",
            "Special Vampiric Abilities:",
            "Starting at 6 hit dice, a vampire gains an ability from the list below each time it gains a new hit die (until all abilities have been acquired).  These abilities are generally gained in the order given, but not always.",
            "Charm Gaze:  A vampire can charm any sentient living creature who meets its gaze; a save vs. Spells is allowed to resist, but at a penalty of -2 due to the power of the charm.  This charm is so powerful that the victim will not resist being bitten by the vampire.",
            "Nocturnal Dominion:  Creatures of the night will obey the vampire.  This power allows control of one of the following: rats, bats, or wolves.  This power may be gained multiple times, granting dominion over a different type each time.  Dominion over Rats allows the vampire to call forth 10d10 rats or 5d4 giant rats; Dominion over Bats allows the vampire to summon  10d10 bats or 3d6 giant bats; and Dominion over Wolves allows the vampire to summon a pack of 3d6 wolves.  Each form of dominion can be used at most once per day, and dominion cannot be used twice within an hour (so it is not possible to summon both giant rats and wolves at the same time, for example).  The relevant type of creature must be \"nearby\" as determined by the GM, will arrive 2d6 rounds later, and will obey the vampire for up to an hour before leaving.",
            "Animal Transformation:  The vampire gains the ability to transform into any sort of creature over which it has dominion.  Obviously, this power can only be gained after at least one form of dominion is available.  The transformation requires a single round during which the vampire cannot attack.  The vampire can use the movement and attack forms of the animal shape assumed, as given in the Core Rules, while retaining its armor class, resistance to non-magical weapons, and regenerative abilities.  The vampire cannot use its charm or energy drain abilities while in animal form, but effects already active will remain so.",
            "Assume Gaseous Form (as the potion):  A vampire having this ability can shift into the form of a mist, moving at a \"flying\" rate of 50' per round.  Such a vampire cannot attack, use any of its abilities, or command any spawn or summoned animals while in this form.  Normally the vampire can resume its physical form in a single round.  If reduced to 0 or fewer hit points but still able to regenerate, a vampire having this power will automatically assume gaseous form and may move away as desired; in this case the vampire cannot resume its physical form until it has recovered at least 1 hit point (as explained above).",
            "Undead Control (minimum 10 hit dice):  The vampire can control other undead monsters.  The vampire must be able to see the undead to be controlled, and the attempt is rolled on the Clerics vs. Undead table in the Core Rules as if the vampire were a cleric of the same level as its hit dice.  Any undead who would be turned will serve for a limited time, generally up to an hour; any who would be destroyed will serve indefinitely.",
            "Destroying a Vampire:",
            "Ending the existence of a vampire is not an easy task, for the vampire must suffer as many points of permanent damage as it has hit points.  Besides the methods described above, a vampire can be destroyed by cremation in a funeral pyre while in any dormant state, such as when reduced to zero hit points by normal damage.",
            "The most dramatic method of defeating a vampire is actually the least reliable: driving a wooden stake through its heart.  Doing this will instantly reduce the vampire to zero hit points as if harmed by normal damage; regeneration is not possible while the stake is present.  Removal of the stake, however, allows the vampire to begin regenerating as described above.  It is not normally possible to drive a stake through a vampire's heart while it is actively resisting, but this can be done after reducing the monster to zero hit points in the usual way.  Of course, after staking a vampire it is possible to use sunlight, running water, or a funeral pyre as described above to complete its destruction.",
            "Vampires with Character Classes:",
            "Any character who has a class and level who becomes a vampire retains that class and level.  The vampire can no longer increase their level or learn new class abilities.  Treat such a vampire as being a sort of \"combination class\" where its attack bonus, hit points, and so on are the better of the figures from either its character class or its new monstrous nature.",
            "For example, a 7th level Thief who becomes a vampire remains a 7th level Thief but is now a 3 hit die Vampire Spawn as well.  The attack bonus of the character is +4, which is better than a 3 hit die monster's +3 AB, so the +4 figure will be used.  A 7th level Thief has about 18 hit points, while a 3 hit die monster has about 14; whichever actual roll is better represents the monster's actual hit points.  All thief abilities remain available, with the vampiric nature added to them."
        ],
        "hitdice": "3*",
        "hitdiceroll": [
            3,
            8,
            0
        ],
        "morale": "9",
        "movement": "30'",
        "name": "Vampire Spawn, 3 HD",
        "noappearing": "1d4, Wild 1d4, Lair 2d4",
        "noapproll": [
            1,
            4,
            0
        ],
        "noapprolllair": [
            2,
            4,
            0
        ],
        "noapprollwild": [
            1,
            4,
            0
        ],
        "noattacks": "1 punch or 1 weapon or 1 bite or gaze",
        "saveas": "Fighter: 3",
        "specialbonus": 1,
        "treasure": "B",
        "xp": "175"
    },
    "Vampire Spawn, 4 HD": {

        "armorclass": "15 (m)",
        "attackbonus": 4,
        "damage": "1d6+1 punch or 1d8+1 or by weapon +1 or 1d3 bite or no gaze",
        "description": [
            "Vampires are undead monsters.  Though they may look just a bit more pale than when they were alive, they do appear to live and even breathe as mortals do (though they do not, in fact, need to breathe to survive).  A vampire has all the memories and abilities it had in life, and is effectively immortal.  Living forever in the shadows often leads to vampires being decadent, while their hunger for blood makes them cruel.",
            "When a human (or, at the GMs option, some other living humanoid) is turned into a vampire it is called a vampire spawn.  Spawn normally begin with 3 hit dice; if a humanoid having more than 3 hit dice is turned, it will begin as a spawn with the number of hit dice it had in life, up to a maximum of 6.  Vampires who are able to feed regularly gain one hit die about every 10 years; some advance faster, some slower, and the GM may wish to roll 2d8+1 for the number of years a given vampire will need to advance a hit die (rolling again after each such gain).",
            "Vampires regenerate in a similar fashion to trolls, recovering 1 hit point per turn (not round) after damage is suffered.  Much like trolls, some forms of damage inflicted upon a vampire cannot be regenerated, such as damage from contact with holy water or exposure to sunlight.  This is called \"permanent damage\" though it can be healed by consuming life energy, as explained in the following paragraph.  Vampires do not heal \"normally\" as living creatures do, but can regain such lost hit points by drinking blood from living creatures.",
            "The vampire's bite inflicts 1d3 points of damage, then each round thereafter one energy level is drained from the victim.  Each level of energy drain inflicted permits the vampire to heal one point of permanent damage, or to regenerate a number of points of ordinary damage equal to the number of hit points lost by the victim.  If using the bite as an attack in combat, the vampire suffers a penalty of -5 to Armor Class due to the vulnerable position it must assume.",
            "If exposed to direct sunlight, the vampire will suffer 3d8 points of permanent damage each round.  Even a partial exposure inflicts 1d8 points of permanent damage.  No saving throw normally applies.",
            "If a vampire's victim is slain by the vampire's bite, the victim will arise as a vampire spawn at the next sunset (but not less than 12 hours later) and thereafter will be under the complete control of the \"parent\" vampire (the \"sire\") until such time as either victim or parent are destroyed.  This transformation can be prevented by driving a stake through the heart of the victim before it arises as a vampire (so long as the stake remains in place until after the event would have occurred).  Alternately, the victim can be recovered by casting restoration followed by raise dead.  One level of energy drain will be restored by this procedure.",
            "Vampires cast no reflections in silvered mirrors or water, though despite conventional wisdom to the contrary they do cast reflections in most other reflective materials; the innate purity of silver and water simply will not reflect them.",
            "Vampires are strong.  As shown on the table above, spawn receive a bonus of +1 to damage inflicted by melee weapons due to this strength, while more mature vampires receive a bonus of +2 or even +3.  Thus, a vampire will generally choose to use a melee weapon (or even its bare hands) in combat rather than attempting to bite.",
            "Vampires are unharmed by non-magical weapons, and like all undead are immune to sleep, charm, and hold spells.",
            "A vampire can be held at bay by several things, including the smell of garlic, a silver or silvered mirror, or a holy symbol presented by a believer (GM's discretion is advised here, but in general someone threatened by a vampire may be more devout than usual).  In such a situation the vampire cannot approach within 5 feet of the repellent item or character, nor can it make any melee attacks or otherwise touch those within the warded area.  If it can summon animals (see below), it can still direct them to attack.",
            "Fresh running water (such as a stream or river) acts as a barrier to a vampire; one cannot cross over any such waterway, neither by bridge or by waterway or even by flying.  It is possible for a vampire to be carried across while lying in its own coffin with the lid closed; the presence of the water flowing beneath the coffin will force the vampire to remain dormant.  Being immersed in running water causes 3d8 points of permanent damage each round.  Of course, vampires are damaged by holy water just with as all other undead monsters.",
            "A vampire may not enter any private dwelling without being invited by someone who resides there, and then only if invited while the resident is actually inside the structure.  Public buildings of any sort do not present this problem; even private rooms in inns are fully accessible to a vampire.",
            "If reduced to 0 hit points in combat, but still able to regenerate at least some of that damage, the vampire is not destroyed.  The vampire will begin to regenerate 1 hit point per turn after 2d6 turns, and may resume normal activity as soon as the first point is restored.  Do not tally negative hit points for a vampire, even if you do so for characters and/or monsters otherwise; if permanent damage is applied to a vampire which is dormant due to normal damage, the permanent damage is considered to override the same number of points of normal damage.",
            "Vampires of 7 hit dice or more are sires, maintaining control of all their own vampire spawn, and are no longer controlled by their own vampiric sire.  New vampires created by those having fewer than 7 hit dice are under the control of the creator's sire; when the creator reaches 7 hit dice it assumes control of all of its own spawn.",
            "Special Vampiric Abilities:",
            "Starting at 6 hit dice, a vampire gains an ability from the list below each time it gains a new hit die (until all abilities have been acquired).  These abilities are generally gained in the order given, but not always.",
            "Charm Gaze:  A vampire can charm any sentient living creature who meets its gaze; a save vs. Spells is allowed to resist, but at a penalty of -2 due to the power of the charm.  This charm is so powerful that the victim will not resist being bitten by the vampire.",
            "Nocturnal Dominion:  Creatures of the night will obey the vampire.  This power allows control of one of the following: rats, bats, or wolves.  This power may be gained multiple times, granting dominion over a different type each time.  Dominion over Rats allows the vampire to call forth 10d10 rats or 5d4 giant rats; Dominion over Bats allows the vampire to summon  10d10 bats or 3d6 giant bats; and Dominion over Wolves allows the vampire to summon a pack of 3d6 wolves.  Each form of dominion can be used at most once per day, and dominion cannot be used twice within an hour (so it is not possible to summon both giant rats and wolves at the same time, for example).  The relevant type of creature must be \"nearby\" as determined by the GM, will arrive 2d6 rounds later, and will obey the vampire for up to an hour before leaving.",
            "Animal Transformation:  The vampire gains the ability to transform into any sort of creature over which it has dominion.  Obviously, this power can only be gained after at least one form of dominion is available.  The transformation requires a single round during which the vampire cannot attack.  The vampire can use the movement and attack forms of the animal shape assumed, as given in the Core Rules, while retaining its armor class, resistance to non-magical weapons, and regenerative abilities.  The vampire cannot use its charm or energy drain abilities while in animal form, but effects already active will remain so.",
            "Assume Gaseous Form (as the potion):  A vampire having this ability can shift into the form of a mist, moving at a \"flying\" rate of 50' per round.  Such a vampire cannot attack, use any of its abilities, or command any spawn or summoned animals while in this form.  Normally the vampire can resume its physical form in a single round.  If reduced to 0 or fewer hit points but still able to regenerate, a vampire having this power will automatically assume gaseous form and may move away as desired; in this case the vampire cannot resume its physical form until it has recovered at least 1 hit point (as explained above).",
            "Undead Control (minimum 10 hit dice):  The vampire can control other undead monsters.  The vampire must be able to see the undead to be controlled, and the attempt is rolled on the Clerics vs. Undead table in the Core Rules as if the vampire were a cleric of the same level as its hit dice.  Any undead who would be turned will serve for a limited time, generally up to an hour; any who would be destroyed will serve indefinitely.",
            "Destroying a Vampire:",
            "Ending the existence of a vampire is not an easy task, for the vampire must suffer as many points of permanent damage as it has hit points.  Besides the methods described above, a vampire can be destroyed by cremation in a funeral pyre while in any dormant state, such as when reduced to zero hit points by normal damage.",
            "The most dramatic method of defeating a vampire is actually the least reliable: driving a wooden stake through its heart.  Doing this will instantly reduce the vampire to zero hit points as if harmed by normal damage; regeneration is not possible while the stake is present.  Removal of the stake, however, allows the vampire to begin regenerating as described above.  It is not normally possible to drive a stake through a vampire's heart while it is actively resisting, but this can be done after reducing the monster to zero hit points in the usual way.  Of course, after staking a vampire it is possible to use sunlight, running water, or a funeral pyre as described above to complete its destruction.",
            "Vampires with Character Classes:",
            "Any character who has a class and level who becomes a vampire retains that class and level.  The vampire can no longer increase their level or learn new class abilities.  Treat such a vampire as being a sort of \"combination class\" where its attack bonus, hit points, and so on are the better of the figures from either its character class or its new monstrous nature.",
            "For example, a 7th level Thief who becomes a vampire remains a 7th level Thief but is now a 3 hit die Vampire Spawn as well.  The attack bonus of the character is +4, which is better than a 3 hit die monster's +3 AB, so the +4 figure will be used.  A 7th level Thief has about 18 hit points, while a 3 hit die monster has about 14; whichever actual roll is better represents the monster's actual hit points.  All thief abilities remain available, with the vampiric nature added to them."
        ],
        "hitdice": "4*",
        "hitdiceroll": [
            4,
            8,
            0
        ],
        "morale": "9",
        "movement": "30'",
        "name": "Vampire Spawn, 4 HD",
        "noappearing": "1d4, Wild 1d4, Lair 2d4",
        "noapproll": [
            1,
            4,
            0
        ],
        "noapprolllair": [
            2,
            4,
            0
        ],
        "noapprollwild": [
            1,
            4,
            0
        ],
        "noattacks": "1 punch or 1 weapon or 1 bite or gaze",
        "saveas": "Fighter: 4",
        "specialbonus": 1,
        "treasure": "B",
        "xp": "280"
    },
    "Vampire Spawn, 5 HD": {

        "armorclass": "16 (m)",
        "attackbonus": 5,
        "damage": "1d6+1 punch or 1d8+1 or by weapon +1 or 1d3 bite or save vs. Spell -2 or allow bite gaze",
        "description": [
            "Vampires are undead monsters.  Though they may look just a bit more pale than when they were alive, they do appear to live and even breathe as mortals do (though they do not, in fact, need to breathe to survive).  A vampire has all the memories and abilities it had in life, and is effectively immortal.  Living forever in the shadows often leads to vampires being decadent, while their hunger for blood makes them cruel.",
            "When a human (or, at the GMs option, some other living humanoid) is turned into a vampire it is called a vampire spawn.  Spawn normally begin with 3 hit dice; if a humanoid having more than 3 hit dice is turned, it will begin as a spawn with the number of hit dice it had in life, up to a maximum of 6.  Vampires who are able to feed regularly gain one hit die about every 10 years; some advance faster, some slower, and the GM may wish to roll 2d8+1 for the number of years a given vampire will need to advance a hit die (rolling again after each such gain).",
            "Vampires regenerate in a similar fashion to trolls, recovering 1 hit point per turn (not round) after damage is suffered.  Much like trolls, some forms of damage inflicted upon a vampire cannot be regenerated, such as damage from contact with holy water or exposure to sunlight.  This is called \"permanent damage\" though it can be healed by consuming life energy, as explained in the following paragraph.  Vampires do not heal \"normally\" as living creatures do, but can regain such lost hit points by drinking blood from living creatures.",
            "The vampire's bite inflicts 1d3 points of damage, then each round thereafter one energy level is drained from the victim.  Each level of energy drain inflicted permits the vampire to heal one point of permanent damage, or to regenerate a number of points of ordinary damage equal to the number of hit points lost by the victim.  If using the bite as an attack in combat, the vampire suffers a penalty of -5 to Armor Class due to the vulnerable position it must assume.",
            "If exposed to direct sunlight, the vampire will suffer 3d8 points of permanent damage each round.  Even a partial exposure inflicts 1d8 points of permanent damage.  No saving throw normally applies.",
            "If a vampire's victim is slain by the vampire's bite, the victim will arise as a vampire spawn at the next sunset (but not less than 12 hours later) and thereafter will be under the complete control of the \"parent\" vampire (the \"sire\") until such time as either victim or parent are destroyed.  This transformation can be prevented by driving a stake through the heart of the victim before it arises as a vampire (so long as the stake remains in place until after the event would have occurred).  Alternately, the victim can be recovered by casting restoration followed by raise dead.  One level of energy drain will be restored by this procedure.",
            "Vampires cast no reflections in silvered mirrors or water, though despite conventional wisdom to the contrary they do cast reflections in most other reflective materials; the innate purity of silver and water simply will not reflect them.",
            "Vampires are strong.  As shown on the table above, spawn receive a bonus of +1 to damage inflicted by melee weapons due to this strength, while more mature vampires receive a bonus of +2 or even +3.  Thus, a vampire will generally choose to use a melee weapon (or even its bare hands) in combat rather than attempting to bite.",
            "Vampires are unharmed by non-magical weapons, and like all undead are immune to sleep, charm, and hold spells.",
            "A vampire can be held at bay by several things, including the smell of garlic, a silver or silvered mirror, or a holy symbol presented by a believer (GM's discretion is advised here, but in general someone threatened by a vampire may be more devout than usual).  In such a situation the vampire cannot approach within 5 feet of the repellent item or character, nor can it make any melee attacks or otherwise touch those within the warded area.  If it can summon animals (see below), it can still direct them to attack.",
            "Fresh running water (such as a stream or river) acts as a barrier to a vampire; one cannot cross over any such waterway, neither by bridge or by waterway or even by flying.  It is possible for a vampire to be carried across while lying in its own coffin with the lid closed; the presence of the water flowing beneath the coffin will force the vampire to remain dormant.  Being immersed in running water causes 3d8 points of permanent damage each round.  Of course, vampires are damaged by holy water just with as all other undead monsters.",
            "A vampire may not enter any private dwelling without being invited by someone who resides there, and then only if invited while the resident is actually inside the structure.  Public buildings of any sort do not present this problem; even private rooms in inns are fully accessible to a vampire.",
            "If reduced to 0 hit points in combat, but still able to regenerate at least some of that damage, the vampire is not destroyed.  The vampire will begin to regenerate 1 hit point per turn after 2d6 turns, and may resume normal activity as soon as the first point is restored.  Do not tally negative hit points for a vampire, even if you do so for characters and/or monsters otherwise; if permanent damage is applied to a vampire which is dormant due to normal damage, the permanent damage is considered to override the same number of points of normal damage.",
            "Vampires of 7 hit dice or more are sires, maintaining control of all their own vampire spawn, and are no longer controlled by their own vampiric sire.  New vampires created by those having fewer than 7 hit dice are under the control of the creator's sire; when the creator reaches 7 hit dice it assumes control of all of its own spawn.",
            "Special Vampiric Abilities:",
            "Starting at 6 hit dice, a vampire gains an ability from the list below each time it gains a new hit die (until all abilities have been acquired).  These abilities are generally gained in the order given, but not always.",
            "Charm Gaze:  A vampire can charm any sentient living creature who meets its gaze; a save vs. Spells is allowed to resist, but at a penalty of -2 due to the power of the charm.  This charm is so powerful that the victim will not resist being bitten by the vampire.",
            "Nocturnal Dominion:  Creatures of the night will obey the vampire.  This power allows control of one of the following: rats, bats, or wolves.  This power may be gained multiple times, granting dominion over a different type each time.  Dominion over Rats allows the vampire to call forth 10d10 rats or 5d4 giant rats; Dominion over Bats allows the vampire to summon  10d10 bats or 3d6 giant bats; and Dominion over Wolves allows the vampire to summon a pack of 3d6 wolves.  Each form of dominion can be used at most once per day, and dominion cannot be used twice within an hour (so it is not possible to summon both giant rats and wolves at the same time, for example).  The relevant type of creature must be \"nearby\" as determined by the GM, will arrive 2d6 rounds later, and will obey the vampire for up to an hour before leaving.",
            "Animal Transformation:  The vampire gains the ability to transform into any sort of creature over which it has dominion.  Obviously, this power can only be gained after at least one form of dominion is available.  The transformation requires a single round during which the vampire cannot attack.  The vampire can use the movement and attack forms of the animal shape assumed, as given in the Core Rules, while retaining its armor class, resistance to non-magical weapons, and regenerative abilities.  The vampire cannot use its charm or energy drain abilities while in animal form, but effects already active will remain so.",
            "Assume Gaseous Form (as the potion):  A vampire having this ability can shift into the form of a mist, moving at a \"flying\" rate of 50' per round.  Such a vampire cannot attack, use any of its abilities, or command any spawn or summoned animals while in this form.  Normally the vampire can resume its physical form in a single round.  If reduced to 0 or fewer hit points but still able to regenerate, a vampire having this power will automatically assume gaseous form and may move away as desired; in this case the vampire cannot resume its physical form until it has recovered at least 1 hit point (as explained above).",
            "Undead Control (minimum 10 hit dice):  The vampire can control other undead monsters.  The vampire must be able to see the undead to be controlled, and the attempt is rolled on the Clerics vs. Undead table in the Core Rules as if the vampire were a cleric of the same level as its hit dice.  Any undead who would be turned will serve for a limited time, generally up to an hour; any who would be destroyed will serve indefinitely.",
            "Destroying a Vampire:",
            "Ending the existence of a vampire is not an easy task, for the vampire must suffer as many points of permanent damage as it has hit points.  Besides the methods described above, a vampire can be destroyed by cremation in a funeral pyre while in any dormant state, such as when reduced to zero hit points by normal damage.",
            "The most dramatic method of defeating a vampire is actually the least reliable: driving a wooden stake through its heart.  Doing this will instantly reduce the vampire to zero hit points as if harmed by normal damage; regeneration is not possible while the stake is present.  Removal of the stake, however, allows the vampire to begin regenerating as described above.  It is not normally possible to drive a stake through a vampire's heart while it is actively resisting, but this can be done after reducing the monster to zero hit points in the usual way.  Of course, after staking a vampire it is possible to use sunlight, running water, or a funeral pyre as described above to complete its destruction.",
            "Vampires with Character Classes:",
            "Any character who has a class and level who becomes a vampire retains that class and level.  The vampire can no longer increase their level or learn new class abilities.  Treat such a vampire as being a sort of \"combination class\" where its attack bonus, hit points, and so on are the better of the figures from either its character class or its new monstrous nature.",
            "For example, a 7th level Thief who becomes a vampire remains a 7th level Thief but is now a 3 hit die Vampire Spawn as well.  The attack bonus of the character is +4, which is better than a 3 hit die monster's +3 AB, so the +4 figure will be used.  A 7th level Thief has about 18 hit points, while a 3 hit die monster has about 14; whichever actual roll is better represents the monster's actual hit points.  All thief abilities remain available, with the vampiric nature added to them."
        ],
        "hitdice": "5*",
        "hitdiceroll": [
            5,
            8,
            0
        ],
        "morale": "10",
        "movement": "40'",
        "name": "Vampire Spawn, 5 HD",
        "noappearing": "1d4, Wild 1d4, Lair 2d4",
        "noapproll": [
            1,
            4,
            0
        ],
        "noapprolllair": [
            2,
            4,
            0
        ],
        "noapprollwild": [
            1,
            4,
            0
        ],
        "noattacks": "1 punch or 1 weapon or 1 bite or gaze",
        "saveas": "Fighter: 5",
        "specialbonus": 1,
        "treasure": "B",
        "xp": "405"
    },
    "Vampire Spawn, 6 HD": {

        "armorclass": "17 (m)",
        "attackbonus": 6,
        "damage": "1d6+1 punch or 1d8+1 or by weapon +1 or 1d3 bite or save vs. Spell -2 or allow bite gaze",
        "description": [
            "Vampires are undead monsters.  Though they may look just a bit more pale than when they were alive, they do appear to live and even breathe as mortals do (though they do not, in fact, need to breathe to survive).  A vampire has all the memories and abilities it had in life, and is effectively immortal.  Living forever in the shadows often leads to vampires being decadent, while their hunger for blood makes them cruel.",
            "When a human (or, at the GMs option, some other living humanoid) is turned into a vampire it is called a vampire spawn.  Spawn normally begin with 3 hit dice; if a humanoid having more than 3 hit dice is turned, it will begin as a spawn with the number of hit dice it had in life, up to a maximum of 6.  Vampires who are able to feed regularly gain one hit die about every 10 years; some advance faster, some slower, and the GM may wish to roll 2d8+1 for the number of years a given vampire will need to advance a hit die (rolling again after each such gain).",
            "Vampires regenerate in a similar fashion to trolls, recovering 1 hit point per turn (not round) after damage is suffered.  Much like trolls, some forms of damage inflicted upon a vampire cannot be regenerated, such as damage from contact with holy water or exposure to sunlight.  This is called \"permanent damage\" though it can be healed by consuming life energy, as explained in the following paragraph.  Vampires do not heal \"normally\" as living creatures do, but can regain such lost hit points by drinking blood from living creatures.",
            "The vampire's bite inflicts 1d3 points of damage, then each round thereafter one energy level is drained from the victim.  Each level of energy drain inflicted permits the vampire to heal one point of permanent damage, or to regenerate a number of points of ordinary damage equal to the number of hit points lost by the victim.  If using the bite as an attack in combat, the vampire suffers a penalty of -5 to Armor Class due to the vulnerable position it must assume.",
            "If exposed to direct sunlight, the vampire will suffer 3d8 points of permanent damage each round.  Even a partial exposure inflicts 1d8 points of permanent damage.  No saving throw normally applies.",
            "If a vampire's victim is slain by the vampire's bite, the victim will arise as a vampire spawn at the next sunset (but not less than 12 hours later) and thereafter will be under the complete control of the \"parent\" vampire (the \"sire\") until such time as either victim or parent are destroyed.  This transformation can be prevented by driving a stake through the heart of the victim before it arises as a vampire (so long as the stake remains in place until after the event would have occurred).  Alternately, the victim can be recovered by casting restoration followed by raise dead.  One level of energy drain will be restored by this procedure.",
            "Vampires cast no reflections in silvered mirrors or water, though despite conventional wisdom to the contrary they do cast reflections in most other reflective materials; the innate purity of silver and water simply will not reflect them.",
            "Vampires are strong.  As shown on the table above, spawn receive a bonus of +1 to damage inflicted by melee weapons due to this strength, while more mature vampires receive a bonus of +2 or even +3.  Thus, a vampire will generally choose to use a melee weapon (or even its bare hands) in combat rather than attempting to bite.",
            "Vampires are unharmed by non-magical weapons, and like all undead are immune to sleep, charm, and hold spells.",
            "A vampire can be held at bay by several things, including the smell of garlic, a silver or silvered mirror, or a holy symbol presented by a believer (GM's discretion is advised here, but in general someone threatened by a vampire may be more devout than usual).  In such a situation the vampire cannot approach within 5 feet of the repellent item or character, nor can it make any melee attacks or otherwise touch those within the warded area.  If it can summon animals (see below), it can still direct them to attack.",
            "Fresh running water (such as a stream or river) acts as a barrier to a vampire; one cannot cross over any such waterway, neither by bridge or by waterway or even by flying.  It is possible for a vampire to be carried across while lying in its own coffin with the lid closed; the presence of the water flowing beneath the coffin will force the vampire to remain dormant.  Being immersed in running water causes 3d8 points of permanent damage each round.  Of course, vampires are damaged by holy water just with as all other undead monsters.",
            "A vampire may not enter any private dwelling without being invited by someone who resides there, and then only if invited while the resident is actually inside the structure.  Public buildings of any sort do not present this problem; even private rooms in inns are fully accessible to a vampire.",
            "If reduced to 0 hit points in combat, but still able to regenerate at least some of that damage, the vampire is not destroyed.  The vampire will begin to regenerate 1 hit point per turn after 2d6 turns, and may resume normal activity as soon as the first point is restored.  Do not tally negative hit points for a vampire, even if you do so for characters and/or monsters otherwise; if permanent damage is applied to a vampire which is dormant due to normal damage, the permanent damage is considered to override the same number of points of normal damage.",
            "Vampires of 7 hit dice or more are sires, maintaining control of all their own vampire spawn, and are no longer controlled by their own vampiric sire.  New vampires created by those having fewer than 7 hit dice are under the control of the creator's sire; when the creator reaches 7 hit dice it assumes control of all of its own spawn.",
            "Special Vampiric Abilities:",
            "Starting at 6 hit dice, a vampire gains an ability from the list below each time it gains a new hit die (until all abilities have been acquired).  These abilities are generally gained in the order given, but not always.",
            "Charm Gaze:  A vampire can charm any sentient living creature who meets its gaze; a save vs. Spells is allowed to resist, but at a penalty of -2 due to the power of the charm.  This charm is so powerful that the victim will not resist being bitten by the vampire.",
            "Nocturnal Dominion:  Creatures of the night will obey the vampire.  This power allows control of one of the following: rats, bats, or wolves.  This power may be gained multiple times, granting dominion over a different type each time.  Dominion over Rats allows the vampire to call forth 10d10 rats or 5d4 giant rats; Dominion over Bats allows the vampire to summon  10d10 bats or 3d6 giant bats; and Dominion over Wolves allows the vampire to summon a pack of 3d6 wolves.  Each form of dominion can be used at most once per day, and dominion cannot be used twice within an hour (so it is not possible to summon both giant rats and wolves at the same time, for example).  The relevant type of creature must be \"nearby\" as determined by the GM, will arrive 2d6 rounds later, and will obey the vampire for up to an hour before leaving.",
            "Animal Transformation:  The vampire gains the ability to transform into any sort of creature over which it has dominion.  Obviously, this power can only be gained after at least one form of dominion is available.  The transformation requires a single round during which the vampire cannot attack.  The vampire can use the movement and attack forms of the animal shape assumed, as given in the Core Rules, while retaining its armor class, resistance to non-magical weapons, and regenerative abilities.  The vampire cannot use its charm or energy drain abilities while in animal form, but effects already active will remain so.",
            "Assume Gaseous Form (as the potion):  A vampire having this ability can shift into the form of a mist, moving at a \"flying\" rate of 50' per round.  Such a vampire cannot attack, use any of its abilities, or command any spawn or summoned animals while in this form.  Normally the vampire can resume its physical form in a single round.  If reduced to 0 or fewer hit points but still able to regenerate, a vampire having this power will automatically assume gaseous form and may move away as desired; in this case the vampire cannot resume its physical form until it has recovered at least 1 hit point (as explained above).",
            "Undead Control (minimum 10 hit dice):  The vampire can control other undead monsters.  The vampire must be able to see the undead to be controlled, and the attempt is rolled on the Clerics vs. Undead table in the Core Rules as if the vampire were a cleric of the same level as its hit dice.  Any undead who would be turned will serve for a limited time, generally up to an hour; any who would be destroyed will serve indefinitely.",
            "Destroying a Vampire:",
            "Ending the existence of a vampire is not an easy task, for the vampire must suffer as many points of permanent damage as it has hit points.  Besides the methods described above, a vampire can be destroyed by cremation in a funeral pyre while in any dormant state, such as when reduced to zero hit points by normal damage.",
            "The most dramatic method of defeating a vampire is actually the least reliable: driving a wooden stake through its heart.  Doing this will instantly reduce the vampire to zero hit points as if harmed by normal damage; regeneration is not possible while the stake is present.  Removal of the stake, however, allows the vampire to begin regenerating as described above.  It is not normally possible to drive a stake through a vampire's heart while it is actively resisting, but this can be done after reducing the monster to zero hit points in the usual way.  Of course, after staking a vampire it is possible to use sunlight, running water, or a funeral pyre as described above to complete its destruction.",
            "Vampires with Character Classes:",
            "Any character who has a class and level who becomes a vampire retains that class and level.  The vampire can no longer increase their level or learn new class abilities.  Treat such a vampire as being a sort of \"combination class\" where its attack bonus, hit points, and so on are the better of the figures from either its character class or its new monstrous nature.",
            "For example, a 7th level Thief who becomes a vampire remains a 7th level Thief but is now a 3 hit die Vampire Spawn as well.  The attack bonus of the character is +4, which is better than a 3 hit die monster's +3 AB, so the +4 figure will be used.  A 7th level Thief has about 18 hit points, while a 3 hit die monster has about 14; whichever actual roll is better represents the monster's actual hit points.  All thief abilities remain available, with the vampiric nature added to them."
        ],
        "hitdice": "6*",
        "hitdiceroll": [
            6,
            8,
            0
        ],
        "morale": "10",
        "movement": "40'",
        "name": "Vampire Spawn, 6 HD",
        "noappearing": "1d4, Wild 1d4, Lair 2d4",
        "noapproll": [
            1,
            4,
            0
        ],
        "noapprolllair": [
            2,
            4,
            0
        ],
        "noapprollwild": [
            1,
            4,
            0
        ],
        "noattacks": "1 punch or 1 weapon or 1 bite or gaze",
        "saveas": "Fighter: 6",
        "specialbonus": 1,
        "treasure": "B",
        "xp": "555"
    },
    "Vampire, 7 HD": {

        "armorclass": "18 (m)",
        "attackbonus": 7,
        "damage": "1d6+2 punch or 1d8+2 or by weapon +2 or 1d3 bite or save vs. Spell -2 or allow bite gaze",
        "description": [
            "Vampires are undead monsters.  Though they may look just a bit more pale than when they were alive, they do appear to live and even breathe as mortals do (though they do not, in fact, need to breathe to survive).  A vampire has all the memories and abilities it had in life, and is effectively immortal.  Living forever in the shadows often leads to vampires being decadent, while their hunger for blood makes them cruel.",
            "When a human (or, at the GMs option, some other living humanoid) is turned into a vampire it is called a vampire spawn.  Spawn normally begin with 3 hit dice; if a humanoid having more than 3 hit dice is turned, it will begin as a spawn with the number of hit dice it had in life, up to a maximum of 6.  Vampires who are able to feed regularly gain one hit die about every 10 years; some advance faster, some slower, and the GM may wish to roll 2d8+1 for the number of years a given vampire will need to advance a hit die (rolling again after each such gain).",
            "Vampires regenerate in a similar fashion to trolls, recovering 1 hit point per turn (not round) after damage is suffered.  Much like trolls, some forms of damage inflicted upon a vampire cannot be regenerated, such as damage from contact with holy water or exposure to sunlight.  This is called \"permanent damage\" though it can be healed by consuming life energy, as explained in the following paragraph.  Vampires do not heal \"normally\" as living creatures do, but can regain such lost hit points by drinking blood from living creatures.",
            "The vampire's bite inflicts 1d3 points of damage, then each round thereafter one energy level is drained from the victim.  Each level of energy drain inflicted permits the vampire to heal one point of permanent damage, or to regenerate a number of points of ordinary damage equal to the number of hit points lost by the victim.  If using the bite as an attack in combat, the vampire suffers a penalty of -5 to Armor Class due to the vulnerable position it must assume.",
            "If exposed to direct sunlight, the vampire will suffer 3d8 points of permanent damage each round.  Even a partial exposure inflicts 1d8 points of permanent damage.  No saving throw normally applies.",
            "If a vampire's victim is slain by the vampire's bite, the victim will arise as a vampire spawn at the next sunset (but not less than 12 hours later) and thereafter will be under the complete control of the \"parent\" vampire (the \"sire\") until such time as either victim or parent are destroyed.  This transformation can be prevented by driving a stake through the heart of the victim before it arises as a vampire (so long as the stake remains in place until after the event would have occurred).  Alternately, the victim can be recovered by casting restoration followed by raise dead.  One level of energy drain will be restored by this procedure.",
            "Vampires cast no reflections in silvered mirrors or water, though despite conventional wisdom to the contrary they do cast reflections in most other reflective materials; the innate purity of silver and water simply will not reflect them.",
            "Vampires are strong.  As shown on the table above, spawn receive a bonus of +1 to damage inflicted by melee weapons due to this strength, while more mature vampires receive a bonus of +2 or even +3.  Thus, a vampire will generally choose to use a melee weapon (or even its bare hands) in combat rather than attempting to bite.",
            "Vampires are unharmed by non-magical weapons, and like all undead are immune to sleep, charm, and hold spells.",
            "A vampire can be held at bay by several things, including the smell of garlic, a silver or silvered mirror, or a holy symbol presented by a believer (GM's discretion is advised here, but in general someone threatened by a vampire may be more devout than usual).  In such a situation the vampire cannot approach within 5 feet of the repellent item or character, nor can it make any melee attacks or otherwise touch those within the warded area.  If it can summon animals (see below), it can still direct them to attack.",
            "Fresh running water (such as a stream or river) acts as a barrier to a vampire; one cannot cross over any such waterway, neither by bridge or by waterway or even by flying.  It is possible for a vampire to be carried across while lying in its own coffin with the lid closed; the presence of the water flowing beneath the coffin will force the vampire to remain dormant.  Being immersed in running water causes 3d8 points of permanent damage each round.  Of course, vampires are damaged by holy water just with as all other undead monsters.",
            "A vampire may not enter any private dwelling without being invited by someone who resides there, and then only if invited while the resident is actually inside the structure.  Public buildings of any sort do not present this problem; even private rooms in inns are fully accessible to a vampire.",
            "If reduced to 0 hit points in combat, but still able to regenerate at least some of that damage, the vampire is not destroyed.  The vampire will begin to regenerate 1 hit point per turn after 2d6 turns, and may resume normal activity as soon as the first point is restored.  Do not tally negative hit points for a vampire, even if you do so for characters and/or monsters otherwise; if permanent damage is applied to a vampire which is dormant due to normal damage, the permanent damage is considered to override the same number of points of normal damage.",
            "Vampires of 7 hit dice or more are sires, maintaining control of all their own vampire spawn, and are no longer controlled by their own vampiric sire.  New vampires created by those having fewer than 7 hit dice are under the control of the creator's sire; when the creator reaches 7 hit dice it assumes control of all of its own spawn.",
            "Special Vampiric Abilities:",
            "Starting at 6 hit dice, a vampire gains an ability from the list below each time it gains a new hit die (until all abilities have been acquired).  These abilities are generally gained in the order given, but not always.",
            "Charm Gaze:  A vampire can charm any sentient living creature who meets its gaze; a save vs. Spells is allowed to resist, but at a penalty of -2 due to the power of the charm.  This charm is so powerful that the victim will not resist being bitten by the vampire.",
            "Nocturnal Dominion:  Creatures of the night will obey the vampire.  This power allows control of one of the following: rats, bats, or wolves.  This power may be gained multiple times, granting dominion over a different type each time.  Dominion over Rats allows the vampire to call forth 10d10 rats or 5d4 giant rats; Dominion over Bats allows the vampire to summon  10d10 bats or 3d6 giant bats; and Dominion over Wolves allows the vampire to summon a pack of 3d6 wolves.  Each form of dominion can be used at most once per day, and dominion cannot be used twice within an hour (so it is not possible to summon both giant rats and wolves at the same time, for example).  The relevant type of creature must be \"nearby\" as determined by the GM, will arrive 2d6 rounds later, and will obey the vampire for up to an hour before leaving.",
            "Animal Transformation:  The vampire gains the ability to transform into any sort of creature over which it has dominion.  Obviously, this power can only be gained after at least one form of dominion is available.  The transformation requires a single round during which the vampire cannot attack.  The vampire can use the movement and attack forms of the animal shape assumed, as given in the Core Rules, while retaining its armor class, resistance to non-magical weapons, and regenerative abilities.  The vampire cannot use its charm or energy drain abilities while in animal form, but effects already active will remain so.",
            "Assume Gaseous Form (as the potion):  A vampire having this ability can shift into the form of a mist, moving at a \"flying\" rate of 50' per round.  Such a vampire cannot attack, use any of its abilities, or command any spawn or summoned animals while in this form.  Normally the vampire can resume its physical form in a single round.  If reduced to 0 or fewer hit points but still able to regenerate, a vampire having this power will automatically assume gaseous form and may move away as desired; in this case the vampire cannot resume its physical form until it has recovered at least 1 hit point (as explained above).",
            "Undead Control (minimum 10 hit dice):  The vampire can control other undead monsters.  The vampire must be able to see the undead to be controlled, and the attempt is rolled on the Clerics vs. Undead table in the Core Rules as if the vampire were a cleric of the same level as its hit dice.  Any undead who would be turned will serve for a limited time, generally up to an hour; any who would be destroyed will serve indefinitely.",
            "Destroying a Vampire:",
            "Ending the existence of a vampire is not an easy task, for the vampire must suffer as many points of permanent damage as it has hit points.  Besides the methods described above, a vampire can be destroyed by cremation in a funeral pyre while in any dormant state, such as when reduced to zero hit points by normal damage.",
            "The most dramatic method of defeating a vampire is actually the least reliable: driving a wooden stake through its heart.  Doing this will instantly reduce the vampire to zero hit points as if harmed by normal damage; regeneration is not possible while the stake is present.  Removal of the stake, however, allows the vampire to begin regenerating as described above.  It is not normally possible to drive a stake through a vampire's heart while it is actively resisting, but this can be done after reducing the monster to zero hit points in the usual way.  Of course, after staking a vampire it is possible to use sunlight, running water, or a funeral pyre as described above to complete its destruction.",
            "Vampires with Character Classes:",
            "Any character who has a class and level who becomes a vampire retains that class and level.  The vampire can no longer increase their level or learn new class abilities.  Treat such a vampire as being a sort of \"combination class\" where its attack bonus, hit points, and so on are the better of the figures from either its character class or its new monstrous nature.",
            "For example, a 7th level Thief who becomes a vampire remains a 7th level Thief but is now a 3 hit die Vampire Spawn as well.  The attack bonus of the character is +4, which is better than a 3 hit die monster's +3 AB, so the +4 figure will be used.  A 7th level Thief has about 18 hit points, while a 3 hit die monster has about 14; whichever actual roll is better represents the monster's actual hit points.  All thief abilities remain available, with the vampiric nature added to them."
        ],
        "hitdice": "7**",
        "hitdiceroll": [
            7,
            8,
            0
        ],
        "morale": "11",
        "movement": "40'",
        "name": "Vampire, 7 HD",
        "noappearing": "1d6, Wild 1d6, Lair 1d6",
        "noapproll": [
            1,
            6,
            0
        ],
        "noapprolllair": [
            1,
            6,
            0
        ],
        "noapprollwild": [
            1,
            6,
            0
        ],
        "noattacks": "1 punch or 1 weapon or 1 bite or gaze",
        "saveas": "Fighter: 7",
        "specialbonus": 2,
        "treasure": "F",
        "xp": "800"
    },
    "Vampire, 8 HD": {

        "armorclass": "19 (m)",
        "attackbonus": 8,
        "damage": "1d6+2 punch or 1d8+2 or by weapon +2 or 1d3 bite or save vs. Spell -2 or allow bite gaze",
        "description": [
            "Vampires are undead monsters.  Though they may look just a bit more pale than when they were alive, they do appear to live and even breathe as mortals do (though they do not, in fact, need to breathe to survive).  A vampire has all the memories and abilities it had in life, and is effectively immortal.  Living forever in the shadows often leads to vampires being decadent, while their hunger for blood makes them cruel.",
            "When a human (or, at the GMs option, some other living humanoid) is turned into a vampire it is called a vampire spawn.  Spawn normally begin with 3 hit dice; if a humanoid having more than 3 hit dice is turned, it will begin as a spawn with the number of hit dice it had in life, up to a maximum of 6.  Vampires who are able to feed regularly gain one hit die about every 10 years; some advance faster, some slower, and the GM may wish to roll 2d8+1 for the number of years a given vampire will need to advance a hit die (rolling again after each such gain).",
            "Vampires regenerate in a similar fashion to trolls, recovering 1 hit point per turn (not round) after damage is suffered.  Much like trolls, some forms of damage inflicted upon a vampire cannot be regenerated, such as damage from contact with holy water or exposure to sunlight.  This is called \"permanent damage\" though it can be healed by consuming life energy, as explained in the following paragraph.  Vampires do not heal \"normally\" as living creatures do, but can regain such lost hit points by drinking blood from living creatures.",
            "The vampire's bite inflicts 1d3 points of damage, then each round thereafter one energy level is drained from the victim.  Each level of energy drain inflicted permits the vampire to heal one point of permanent damage, or to regenerate a number of points of ordinary damage equal to the number of hit points lost by the victim.  If using the bite as an attack in combat, the vampire suffers a penalty of -5 to Armor Class due to the vulnerable position it must assume.",
            "If exposed to direct sunlight, the vampire will suffer 3d8 points of permanent damage each round.  Even a partial exposure inflicts 1d8 points of permanent damage.  No saving throw normally applies.",
            "If a vampire's victim is slain by the vampire's bite, the victim will arise as a vampire spawn at the next sunset (but not less than 12 hours later) and thereafter will be under the complete control of the \"parent\" vampire (the \"sire\") until such time as either victim or parent are destroyed.  This transformation can be prevented by driving a stake through the heart of the victim before it arises as a vampire (so long as the stake remains in place until after the event would have occurred).  Alternately, the victim can be recovered by casting restoration followed by raise dead.  One level of energy drain will be restored by this procedure.",
            "Vampires cast no reflections in silvered mirrors or water, though despite conventional wisdom to the contrary they do cast reflections in most other reflective materials; the innate purity of silver and water simply will not reflect them.",
            "Vampires are strong.  As shown on the table above, spawn receive a bonus of +1 to damage inflicted by melee weapons due to this strength, while more mature vampires receive a bonus of +2 or even +3.  Thus, a vampire will generally choose to use a melee weapon (or even its bare hands) in combat rather than attempting to bite.",
            "Vampires are unharmed by non-magical weapons, and like all undead are immune to sleep, charm, and hold spells.",
            "A vampire can be held at bay by several things, including the smell of garlic, a silver or silvered mirror, or a holy symbol presented by a believer (GM's discretion is advised here, but in general someone threatened by a vampire may be more devout than usual).  In such a situation the vampire cannot approach within 5 feet of the repellent item or character, nor can it make any melee attacks or otherwise touch those within the warded area.  If it can summon animals (see below), it can still direct them to attack.",
            "Fresh running water (such as a stream or river) acts as a barrier to a vampire; one cannot cross over any such waterway, neither by bridge or by waterway or even by flying.  It is possible for a vampire to be carried across while lying in its own coffin with the lid closed; the presence of the water flowing beneath the coffin will force the vampire to remain dormant.  Being immersed in running water causes 3d8 points of permanent damage each round.  Of course, vampires are damaged by holy water just with as all other undead monsters.",
            "A vampire may not enter any private dwelling without being invited by someone who resides there, and then only if invited while the resident is actually inside the structure.  Public buildings of any sort do not present this problem; even private rooms in inns are fully accessible to a vampire.",
            "If reduced to 0 hit points in combat, but still able to regenerate at least some of that damage, the vampire is not destroyed.  The vampire will begin to regenerate 1 hit point per turn after 2d6 turns, and may resume normal activity as soon as the first point is restored.  Do not tally negative hit points for a vampire, even if you do so for characters and/or monsters otherwise; if permanent damage is applied to a vampire which is dormant due to normal damage, the permanent damage is considered to override the same number of points of normal damage.",
            "Vampires of 7 hit dice or more are sires, maintaining control of all their own vampire spawn, and are no longer controlled by their own vampiric sire.  New vampires created by those having fewer than 7 hit dice are under the control of the creator's sire; when the creator reaches 7 hit dice it assumes control of all of its own spawn.",
            "Special Vampiric Abilities:",
            "Starting at 6 hit dice, a vampire gains an ability from the list below each time it gains a new hit die (until all abilities have been acquired).  These abilities are generally gained in the order given, but not always.",
            "Charm Gaze:  A vampire can charm any sentient living creature who meets its gaze; a save vs. Spells is allowed to resist, but at a penalty of -2 due to the power of the charm.  This charm is so powerful that the victim will not resist being bitten by the vampire.",
            "Nocturnal Dominion:  Creatures of the night will obey the vampire.  This power allows control of one of the following: rats, bats, or wolves.  This power may be gained multiple times, granting dominion over a different type each time.  Dominion over Rats allows the vampire to call forth 10d10 rats or 5d4 giant rats; Dominion over Bats allows the vampire to summon  10d10 bats or 3d6 giant bats; and Dominion over Wolves allows the vampire to summon a pack of 3d6 wolves.  Each form of dominion can be used at most once per day, and dominion cannot be used twice within an hour (so it is not possible to summon both giant rats and wolves at the same time, for example).  The relevant type of creature must be \"nearby\" as determined by the GM, will arrive 2d6 rounds later, and will obey the vampire for up to an hour before leaving.",
            "Animal Transformation:  The vampire gains the ability to transform into any sort of creature over which it has dominion.  Obviously, this power can only be gained after at least one form of dominion is available.  The transformation requires a single round during which the vampire cannot attack.  The vampire can use the movement and attack forms of the animal shape assumed, as given in the Core Rules, while retaining its armor class, resistance to non-magical weapons, and regenerative abilities.  The vampire cannot use its charm or energy drain abilities while in animal form, but effects already active will remain so.",
            "Assume Gaseous Form (as the potion):  A vampire having this ability can shift into the form of a mist, moving at a \"flying\" rate of 50' per round.  Such a vampire cannot attack, use any of its abilities, or command any spawn or summoned animals while in this form.  Normally the vampire can resume its physical form in a single round.  If reduced to 0 or fewer hit points but still able to regenerate, a vampire having this power will automatically assume gaseous form and may move away as desired; in this case the vampire cannot resume its physical form until it has recovered at least 1 hit point (as explained above).",
            "Undead Control (minimum 10 hit dice):  The vampire can control other undead monsters.  The vampire must be able to see the undead to be controlled, and the attempt is rolled on the Clerics vs. Undead table in the Core Rules as if the vampire were a cleric of the same level as its hit dice.  Any undead who would be turned will serve for a limited time, generally up to an hour; any who would be destroyed will serve indefinitely.",
            "Destroying a Vampire:",
            "Ending the existence of a vampire is not an easy task, for the vampire must suffer as many points of permanent damage as it has hit points.  Besides the methods described above, a vampire can be destroyed by cremation in a funeral pyre while in any dormant state, such as when reduced to zero hit points by normal damage.",
            "The most dramatic method of defeating a vampire is actually the least reliable: driving a wooden stake through its heart.  Doing this will instantly reduce the vampire to zero hit points as if harmed by normal damage; regeneration is not possible while the stake is present.  Removal of the stake, however, allows the vampire to begin regenerating as described above.  It is not normally possible to drive a stake through a vampire's heart while it is actively resisting, but this can be done after reducing the monster to zero hit points in the usual way.  Of course, after staking a vampire it is possible to use sunlight, running water, or a funeral pyre as described above to complete its destruction.",
            "Vampires with Character Classes:",
            "Any character who has a class and level who becomes a vampire retains that class and level.  The vampire can no longer increase their level or learn new class abilities.  Treat such a vampire as being a sort of \"combination class\" where its attack bonus, hit points, and so on are the better of the figures from either its character class or its new monstrous nature.",
            "For example, a 7th level Thief who becomes a vampire remains a 7th level Thief but is now a 3 hit die Vampire Spawn as well.  The attack bonus of the character is +4, which is better than a 3 hit die monster's +3 AB, so the +4 figure will be used.  A 7th level Thief has about 18 hit points, while a 3 hit die monster has about 14; whichever actual roll is better represents the monster's actual hit points.  All thief abilities remain available, with the vampiric nature added to them."
        ],
        "hitdice": "8**",
        "hitdiceroll": [
            8,
            8,
            0
        ],
        "morale": "11",
        "movement": "40'",
        "name": "Vampire, 8 HD",
        "noappearing": "1d6, Wild 1d6, Lair 1d6",
        "noapproll": [
            1,
            6,
            0
        ],
        "noapprolllair": [
            1,
            6,
            0
        ],
        "noapprollwild": [
            1,
            6,
            0
        ],
        "noattacks": "1 punch or 1 weapon or 1 bite or gaze",
        "saveas": "Fighter: 8",
        "specialbonus": 2,
        "treasure": "F",
        "xp": "1015"
    },
    "Vampire, 9 HD": {

        "armorclass": "20 (m)",
        "attackbonus": 8,
        "damage": "1d6+2 punch or 1d8+2 or by weapon +2 or 1d3 bite or save vs. Spell -2 or allow bite gaze",
        "description": [
            "Vampires are undead monsters.  Though they may look just a bit more pale than when they were alive, they do appear to live and even breathe as mortals do (though they do not, in fact, need to breathe to survive).  A vampire has all the memories and abilities it had in life, and is effectively immortal.  Living forever in the shadows often leads to vampires being decadent, while their hunger for blood makes them cruel.",
            "When a human (or, at the GMs option, some other living humanoid) is turned into a vampire it is called a vampire spawn.  Spawn normally begin with 3 hit dice; if a humanoid having more than 3 hit dice is turned, it will begin as a spawn with the number of hit dice it had in life, up to a maximum of 6.  Vampires who are able to feed regularly gain one hit die about every 10 years; some advance faster, some slower, and the GM may wish to roll 2d8+1 for the number of years a given vampire will need to advance a hit die (rolling again after each such gain).",
            "Vampires regenerate in a similar fashion to trolls, recovering 1 hit point per turn (not round) after damage is suffered.  Much like trolls, some forms of damage inflicted upon a vampire cannot be regenerated, such as damage from contact with holy water or exposure to sunlight.  This is called \"permanent damage\" though it can be healed by consuming life energy, as explained in the following paragraph.  Vampires do not heal \"normally\" as living creatures do, but can regain such lost hit points by drinking blood from living creatures.",
            "The vampire's bite inflicts 1d3 points of damage, then each round thereafter one energy level is drained from the victim.  Each level of energy drain inflicted permits the vampire to heal one point of permanent damage, or to regenerate a number of points of ordinary damage equal to the number of hit points lost by the victim.  If using the bite as an attack in combat, the vampire suffers a penalty of -5 to Armor Class due to the vulnerable position it must assume.",
            "If exposed to direct sunlight, the vampire will suffer 3d8 points of permanent damage each round.  Even a partial exposure inflicts 1d8 points of permanent damage.  No saving throw normally applies.",
            "If a vampire's victim is slain by the vampire's bite, the victim will arise as a vampire spawn at the next sunset (but not less than 12 hours later) and thereafter will be under the complete control of the \"parent\" vampire (the \"sire\") until such time as either victim or parent are destroyed.  This transformation can be prevented by driving a stake through the heart of the victim before it arises as a vampire (so long as the stake remains in place until after the event would have occurred).  Alternately, the victim can be recovered by casting restoration followed by raise dead.  One level of energy drain will be restored by this procedure.",
            "Vampires cast no reflections in silvered mirrors or water, though despite conventional wisdom to the contrary they do cast reflections in most other reflective materials; the innate purity of silver and water simply will not reflect them.",
            "Vampires are strong.  As shown on the table above, spawn receive a bonus of +1 to damage inflicted by melee weapons due to this strength, while more mature vampires receive a bonus of +2 or even +3.  Thus, a vampire will generally choose to use a melee weapon (or even its bare hands) in combat rather than attempting to bite.",
            "Vampires are unharmed by non-magical weapons, and like all undead are immune to sleep, charm, and hold spells.",
            "A vampire can be held at bay by several things, including the smell of garlic, a silver or silvered mirror, or a holy symbol presented by a believer (GM's discretion is advised here, but in general someone threatened by a vampire may be more devout than usual).  In such a situation the vampire cannot approach within 5 feet of the repellent item or character, nor can it make any melee attacks or otherwise touch those within the warded area.  If it can summon animals (see below), it can still direct them to attack.",
            "Fresh running water (such as a stream or river) acts as a barrier to a vampire; one cannot cross over any such waterway, neither by bridge or by waterway or even by flying.  It is possible for a vampire to be carried across while lying in its own coffin with the lid closed; the presence of the water flowing beneath the coffin will force the vampire to remain dormant.  Being immersed in running water causes 3d8 points of permanent damage each round.  Of course, vampires are damaged by holy water just with as all other undead monsters.",
            "A vampire may not enter any private dwelling without being invited by someone who resides there, and then only if invited while the resident is actually inside the structure.  Public buildings of any sort do not present this problem; even private rooms in inns are fully accessible to a vampire.",
            "If reduced to 0 hit points in combat, but still able to regenerate at least some of that damage, the vampire is not destroyed.  The vampire will begin to regenerate 1 hit point per turn after 2d6 turns, and may resume normal activity as soon as the first point is restored.  Do not tally negative hit points for a vampire, even if you do so for characters and/or monsters otherwise; if permanent damage is applied to a vampire which is dormant due to normal damage, the permanent damage is considered to override the same number of points of normal damage.",
            "Vampires of 7 hit dice or more are sires, maintaining control of all their own vampire spawn, and are no longer controlled by their own vampiric sire.  New vampires created by those having fewer than 7 hit dice are under the control of the creator's sire; when the creator reaches 7 hit dice it assumes control of all of its own spawn.",
            "Special Vampiric Abilities:",
            "Starting at 6 hit dice, a vampire gains an ability from the list below each time it gains a new hit die (until all abilities have been acquired).  These abilities are generally gained in the order given, but not always.",
            "Charm Gaze:  A vampire can charm any sentient living creature who meets its gaze; a save vs. Spells is allowed to resist, but at a penalty of -2 due to the power of the charm.  This charm is so powerful that the victim will not resist being bitten by the vampire.",
            "Nocturnal Dominion:  Creatures of the night will obey the vampire.  This power allows control of one of the following: rats, bats, or wolves.  This power may be gained multiple times, granting dominion over a different type each time.  Dominion over Rats allows the vampire to call forth 10d10 rats or 5d4 giant rats; Dominion over Bats allows the vampire to summon  10d10 bats or 3d6 giant bats; and Dominion over Wolves allows the vampire to summon a pack of 3d6 wolves.  Each form of dominion can be used at most once per day, and dominion cannot be used twice within an hour (so it is not possible to summon both giant rats and wolves at the same time, for example).  The relevant type of creature must be \"nearby\" as determined by the GM, will arrive 2d6 rounds later, and will obey the vampire for up to an hour before leaving.",
            "Animal Transformation:  The vampire gains the ability to transform into any sort of creature over which it has dominion.  Obviously, this power can only be gained after at least one form of dominion is available.  The transformation requires a single round during which the vampire cannot attack.  The vampire can use the movement and attack forms of the animal shape assumed, as given in the Core Rules, while retaining its armor class, resistance to non-magical weapons, and regenerative abilities.  The vampire cannot use its charm or energy drain abilities while in animal form, but effects already active will remain so.",
            "Assume Gaseous Form (as the potion):  A vampire having this ability can shift into the form of a mist, moving at a \"flying\" rate of 50' per round.  Such a vampire cannot attack, use any of its abilities, or command any spawn or summoned animals while in this form.  Normally the vampire can resume its physical form in a single round.  If reduced to 0 or fewer hit points but still able to regenerate, a vampire having this power will automatically assume gaseous form and may move away as desired; in this case the vampire cannot resume its physical form until it has recovered at least 1 hit point (as explained above).",
            "Undead Control (minimum 10 hit dice):  The vampire can control other undead monsters.  The vampire must be able to see the undead to be controlled, and the attempt is rolled on the Clerics vs. Undead table in the Core Rules as if the vampire were a cleric of the same level as its hit dice.  Any undead who would be turned will serve for a limited time, generally up to an hour; any who would be destroyed will serve indefinitely.",
            "Destroying a Vampire:",
            "Ending the existence of a vampire is not an easy task, for the vampire must suffer as many points of permanent damage as it has hit points.  Besides the methods described above, a vampire can be destroyed by cremation in a funeral pyre while in any dormant state, such as when reduced to zero hit points by normal damage.",
            "The most dramatic method of defeating a vampire is actually the least reliable: driving a wooden stake through its heart.  Doing this will instantly reduce the vampire to zero hit points as if harmed by normal damage; regeneration is not possible while the stake is present.  Removal of the stake, however, allows the vampire to begin regenerating as described above.  It is not normally possible to drive a stake through a vampire's heart while it is actively resisting, but this can be done after reducing the monster to zero hit points in the usual way.  Of course, after staking a vampire it is possible to use sunlight, running water, or a funeral pyre as described above to complete its destruction.",
            "Vampires with Character Classes:",
            "Any character who has a class and level who becomes a vampire retains that class and level.  The vampire can no longer increase their level or learn new class abilities.  Treat such a vampire as being a sort of \"combination class\" where its attack bonus, hit points, and so on are the better of the figures from either its character class or its new monstrous nature.",
            "For example, a 7th level Thief who becomes a vampire remains a 7th level Thief but is now a 3 hit die Vampire Spawn as well.  The attack bonus of the character is +4, which is better than a 3 hit die monster's +3 AB, so the +4 figure will be used.  A 7th level Thief has about 18 hit points, while a 3 hit die monster has about 14; whichever actual roll is better represents the monster's actual hit points.  All thief abilities remain available, with the vampiric nature added to them."
        ],
        "hitdice": "9** (+8)",
        "hitdiceroll": [
            9,
            8,
            0
        ],
        "morale": "11",
        "movement": "40'",
        "name": "Vampire, 9 HD",
        "noappearing": "1d6, Wild 1d6, Lair 1d6",
        "noapproll": [
            1,
            6,
            0
        ],
        "noapprolllair": [
            1,
            6,
            0
        ],
        "noapprollwild": [
            1,
            6,
            0
        ],
        "noattacks": "1 punch or 1 weapon or 1 bite or gaze",
        "saveas": "Fighter: 9",
        "specialbonus": 2,
        "treasure": "F",
        "xp": "1015"
    },
    "Vampire, 10 HD": {

        "armorclass": "21 (m)",
        "attackbonus": 9,
        "damage": "1d6+3 punch or 1d8+3 or by weapon +3 or 1d3 bite or save vs. Spell -2 or allow bite gaze",
        "description": [
            "Vampires are undead monsters.  Though they may look just a bit more pale than when they were alive, they do appear to live and even breathe as mortals do (though they do not, in fact, need to breathe to survive).  A vampire has all the memories and abilities it had in life, and is effectively immortal.  Living forever in the shadows often leads to vampires being decadent, while their hunger for blood makes them cruel.",
            "When a human (or, at the GMs option, some other living humanoid) is turned into a vampire it is called a vampire spawn.  Spawn normally begin with 3 hit dice; if a humanoid having more than 3 hit dice is turned, it will begin as a spawn with the number of hit dice it had in life, up to a maximum of 6.  Vampires who are able to feed regularly gain one hit die about every 10 years; some advance faster, some slower, and the GM may wish to roll 2d8+1 for the number of years a given vampire will need to advance a hit die (rolling again after each such gain).",
            "Vampires regenerate in a similar fashion to trolls, recovering 1 hit point per turn (not round) after damage is suffered.  Much like trolls, some forms of damage inflicted upon a vampire cannot be regenerated, such as damage from contact with holy water or exposure to sunlight.  This is called \"permanent damage\" though it can be healed by consuming life energy, as explained in the following paragraph.  Vampires do not heal \"normally\" as living creatures do, but can regain such lost hit points by drinking blood from living creatures.",
            "The vampire's bite inflicts 1d3 points of damage, then each round thereafter one energy level is drained from the victim.  Each level of energy drain inflicted permits the vampire to heal one point of permanent damage, or to regenerate a number of points of ordinary damage equal to the number of hit points lost by the victim.  If using the bite as an attack in combat, the vampire suffers a penalty of -5 to Armor Class due to the vulnerable position it must assume.",
            "If exposed to direct sunlight, the vampire will suffer 3d8 points of permanent damage each round.  Even a partial exposure inflicts 1d8 points of permanent damage.  No saving throw normally applies.",
            "If a vampire's victim is slain by the vampire's bite, the victim will arise as a vampire spawn at the next sunset (but not less than 12 hours later) and thereafter will be under the complete control of the \"parent\" vampire (the \"sire\") until such time as either victim or parent are destroyed.  This transformation can be prevented by driving a stake through the heart of the victim before it arises as a vampire (so long as the stake remains in place until after the event would have occurred).  Alternately, the victim can be recovered by casting restoration followed by raise dead.  One level of energy drain will be restored by this procedure.",
            "Vampires cast no reflections in silvered mirrors or water, though despite conventional wisdom to the contrary they do cast reflections in most other reflective materials; the innate purity of silver and water simply will not reflect them.",
            "Vampires are strong.  As shown on the table above, spawn receive a bonus of +1 to damage inflicted by melee weapons due to this strength, while more mature vampires receive a bonus of +2 or even +3.  Thus, a vampire will generally choose to use a melee weapon (or even its bare hands) in combat rather than attempting to bite.",
            "Vampires are unharmed by non-magical weapons, and like all undead are immune to sleep, charm, and hold spells.",
            "A vampire can be held at bay by several things, including the smell of garlic, a silver or silvered mirror, or a holy symbol presented by a believer (GM's discretion is advised here, but in general someone threatened by a vampire may be more devout than usual).  In such a situation the vampire cannot approach within 5 feet of the repellent item or character, nor can it make any melee attacks or otherwise touch those within the warded area.  If it can summon animals (see below), it can still direct them to attack.",
            "Fresh running water (such as a stream or river) acts as a barrier to a vampire; one cannot cross over any such waterway, neither by bridge or by waterway or even by flying.  It is possible for a vampire to be carried across while lying in its own coffin with the lid closed; the presence of the water flowing beneath the coffin will force the vampire to remain dormant.  Being immersed in running water causes 3d8 points of permanent damage each round.  Of course, vampires are damaged by holy water just with as all other undead monsters.",
            "A vampire may not enter any private dwelling without being invited by someone who resides there, and then only if invited while the resident is actually inside the structure.  Public buildings of any sort do not present this problem; even private rooms in inns are fully accessible to a vampire.",
            "If reduced to 0 hit points in combat, but still able to regenerate at least some of that damage, the vampire is not destroyed.  The vampire will begin to regenerate 1 hit point per turn after 2d6 turns, and may resume normal activity as soon as the first point is restored.  Do not tally negative hit points for a vampire, even if you do so for characters and/or monsters otherwise; if permanent damage is applied to a vampire which is dormant due to normal damage, the permanent damage is considered to override the same number of points of normal damage.",
            "Vampires of 7 hit dice or more are sires, maintaining control of all their own vampire spawn, and are no longer controlled by their own vampiric sire.  New vampires created by those having fewer than 7 hit dice are under the control of the creator's sire; when the creator reaches 7 hit dice it assumes control of all of its own spawn.",
            "Special Vampiric Abilities:",
            "Starting at 6 hit dice, a vampire gains an ability from the list below each time it gains a new hit die (until all abilities have been acquired).  These abilities are generally gained in the order given, but not always.",
            "Charm Gaze:  A vampire can charm any sentient living creature who meets its gaze; a save vs. Spells is allowed to resist, but at a penalty of -2 due to the power of the charm.  This charm is so powerful that the victim will not resist being bitten by the vampire.",
            "Nocturnal Dominion:  Creatures of the night will obey the vampire.  This power allows control of one of the following: rats, bats, or wolves.  This power may be gained multiple times, granting dominion over a different type each time.  Dominion over Rats allows the vampire to call forth 10d10 rats or 5d4 giant rats; Dominion over Bats allows the vampire to summon  10d10 bats or 3d6 giant bats; and Dominion over Wolves allows the vampire to summon a pack of 3d6 wolves.  Each form of dominion can be used at most once per day, and dominion cannot be used twice within an hour (so it is not possible to summon both giant rats and wolves at the same time, for example).  The relevant type of creature must be \"nearby\" as determined by the GM, will arrive 2d6 rounds later, and will obey the vampire for up to an hour before leaving.",
            "Animal Transformation:  The vampire gains the ability to transform into any sort of creature over which it has dominion.  Obviously, this power can only be gained after at least one form of dominion is available.  The transformation requires a single round during which the vampire cannot attack.  The vampire can use the movement and attack forms of the animal shape assumed, as given in the Core Rules, while retaining its armor class, resistance to non-magical weapons, and regenerative abilities.  The vampire cannot use its charm or energy drain abilities while in animal form, but effects already active will remain so.",
            "Assume Gaseous Form (as the potion):  A vampire having this ability can shift into the form of a mist, moving at a \"flying\" rate of 50' per round.  Such a vampire cannot attack, use any of its abilities, or command any spawn or summoned animals while in this form.  Normally the vampire can resume its physical form in a single round.  If reduced to 0 or fewer hit points but still able to regenerate, a vampire having this power will automatically assume gaseous form and may move away as desired; in this case the vampire cannot resume its physical form until it has recovered at least 1 hit point (as explained above).",
            "Undead Control (minimum 10 hit dice):  The vampire can control other undead monsters.  The vampire must be able to see the undead to be controlled, and the attempt is rolled on the Clerics vs. Undead table in the Core Rules as if the vampire were a cleric of the same level as its hit dice.  Any undead who would be turned will serve for a limited time, generally up to an hour; any who would be destroyed will serve indefinitely.",
            "Destroying a Vampire:",
            "Ending the existence of a vampire is not an easy task, for the vampire must suffer as many points of permanent damage as it has hit points.  Besides the methods described above, a vampire can be destroyed by cremation in a funeral pyre while in any dormant state, such as when reduced to zero hit points by normal damage.",
            "The most dramatic method of defeating a vampire is actually the least reliable: driving a wooden stake through its heart.  Doing this will instantly reduce the vampire to zero hit points as if harmed by normal damage; regeneration is not possible while the stake is present.  Removal of the stake, however, allows the vampire to begin regenerating as described above.  It is not normally possible to drive a stake through a vampire's heart while it is actively resisting, but this can be done after reducing the monster to zero hit points in the usual way.  Of course, after staking a vampire it is possible to use sunlight, running water, or a funeral pyre as described above to complete its destruction.",
            "Vampires with Character Classes:",
            "Any character who has a class and level who becomes a vampire retains that class and level.  The vampire can no longer increase their level or learn new class abilities.  Treat such a vampire as being a sort of \"combination class\" where its attack bonus, hit points, and so on are the better of the figures from either its character class or its new monstrous nature.",
            "For example, a 7th level Thief who becomes a vampire remains a 7th level Thief but is now a 3 hit die Vampire Spawn as well.  The attack bonus of the character is +4, which is better than a 3 hit die monster's +3 AB, so the +4 figure will be used.  A 7th level Thief has about 18 hit points, while a 3 hit die monster has about 14; whichever actual roll is better represents the monster's actual hit points.  All thief abilities remain available, with the vampiric nature added to them."
        ],
        "hitdice": "10** (+9)",
        "hitdiceroll": [
            10,
            8,
            0
        ],
        "morale": "11",
        "movement": "40'",
        "name": "Vampire, 10 HD",
        "noappearing": "1d6, Wild 1d6, Lair 1d6",
        "noapproll": [
            1,
            6,
            0
        ],
        "noapprolllair": [
            1,
            6,
            0
        ],
        "noapprollwild": [
            1,
            6,
            0
        ],
        "noattacks": "1 punch or 1 weapon or 1 bite or gaze",
        "saveas": "Fighter: 10",
        "specialbonus": 2,
        "treasure": "F x 2",
        "xp": "1480"
    },
    "Vampire, 11 HD": {

        "armorclass": "21 (m)",
        "attackbonus": 9,
        "damage": "1d6+3 punch or 1d8+3 or by weapon +3 or 1d3 bite or save vs. Spell -2 or allow bite gaze",
        "description": [
            "Vampires are undead monsters.  Though they may look just a bit more pale than when they were alive, they do appear to live and even breathe as mortals do (though they do not, in fact, need to breathe to survive).  A vampire has all the memories and abilities it had in life, and is effectively immortal.  Living forever in the shadows often leads to vampires being decadent, while their hunger for blood makes them cruel.",
            "When a human (or, at the GMs option, some other living humanoid) is turned into a vampire it is called a vampire spawn.  Spawn normally begin with 3 hit dice; if a humanoid having more than 3 hit dice is turned, it will begin as a spawn with the number of hit dice it had in life, up to a maximum of 6.  Vampires who are able to feed regularly gain one hit die about every 10 years; some advance faster, some slower, and the GM may wish to roll 2d8+1 for the number of years a given vampire will need to advance a hit die (rolling again after each such gain).",
            "Vampires regenerate in a similar fashion to trolls, recovering 1 hit point per turn (not round) after damage is suffered.  Much like trolls, some forms of damage inflicted upon a vampire cannot be regenerated, such as damage from contact with holy water or exposure to sunlight.  This is called \"permanent damage\" though it can be healed by consuming life energy, as explained in the following paragraph.  Vampires do not heal \"normally\" as living creatures do, but can regain such lost hit points by drinking blood from living creatures.",
            "The vampire's bite inflicts 1d3 points of damage, then each round thereafter one energy level is drained from the victim.  Each level of energy drain inflicted permits the vampire to heal one point of permanent damage, or to regenerate a number of points of ordinary damage equal to the number of hit points lost by the victim.  If using the bite as an attack in combat, the vampire suffers a penalty of -5 to Armor Class due to the vulnerable position it must assume.",
            "If exposed to direct sunlight, the vampire will suffer 3d8 points of permanent damage each round.  Even a partial exposure inflicts 1d8 points of permanent damage.  No saving throw normally applies.",
            "If a vampire's victim is slain by the vampire's bite, the victim will arise as a vampire spawn at the next sunset (but not less than 12 hours later) and thereafter will be under the complete control of the \"parent\" vampire (the \"sire\") until such time as either victim or parent are destroyed.  This transformation can be prevented by driving a stake through the heart of the victim before it arises as a vampire (so long as the stake remains in place until after the event would have occurred).  Alternately, the victim can be recovered by casting restoration followed by raise dead.  One level of energy drain will be restored by this procedure.",
            "Vampires cast no reflections in silvered mirrors or water, though despite conventional wisdom to the contrary they do cast reflections in most other reflective materials; the innate purity of silver and water simply will not reflect them.",
            "Vampires are strong.  As shown on the table above, spawn receive a bonus of +1 to damage inflicted by melee weapons due to this strength, while more mature vampires receive a bonus of +2 or even +3.  Thus, a vampire will generally choose to use a melee weapon (or even its bare hands) in combat rather than attempting to bite.",
            "Vampires are unharmed by non-magical weapons, and like all undead are immune to sleep, charm, and hold spells.",
            "A vampire can be held at bay by several things, including the smell of garlic, a silver or silvered mirror, or a holy symbol presented by a believer (GM's discretion is advised here, but in general someone threatened by a vampire may be more devout than usual).  In such a situation the vampire cannot approach within 5 feet of the repellent item or character, nor can it make any melee attacks or otherwise touch those within the warded area.  If it can summon animals (see below), it can still direct them to attack.",
            "Fresh running water (such as a stream or river) acts as a barrier to a vampire; one cannot cross over any such waterway, neither by bridge or by waterway or even by flying.  It is possible for a vampire to be carried across while lying in its own coffin with the lid closed; the presence of the water flowing beneath the coffin will force the vampire to remain dormant.  Being immersed in running water causes 3d8 points of permanent damage each round.  Of course, vampires are damaged by holy water just with as all other undead monsters.",
            "A vampire may not enter any private dwelling without being invited by someone who resides there, and then only if invited while the resident is actually inside the structure.  Public buildings of any sort do not present this problem; even private rooms in inns are fully accessible to a vampire.",
            "If reduced to 0 hit points in combat, but still able to regenerate at least some of that damage, the vampire is not destroyed.  The vampire will begin to regenerate 1 hit point per turn after 2d6 turns, and may resume normal activity as soon as the first point is restored.  Do not tally negative hit points for a vampire, even if you do so for characters and/or monsters otherwise; if permanent damage is applied to a vampire which is dormant due to normal damage, the permanent damage is considered to override the same number of points of normal damage.",
            "Vampires of 7 hit dice or more are sires, maintaining control of all their own vampire spawn, and are no longer controlled by their own vampiric sire.  New vampires created by those having fewer than 7 hit dice are under the control of the creator's sire; when the creator reaches 7 hit dice it assumes control of all of its own spawn.",
            "Special Vampiric Abilities:",
            "Starting at 6 hit dice, a vampire gains an ability from the list below each time it gains a new hit die (until all abilities have been acquired).  These abilities are generally gained in the order given, but not always.",
            "Charm Gaze:  A vampire can charm any sentient living creature who meets its gaze; a save vs. Spells is allowed to resist, but at a penalty of -2 due to the power of the charm.  This charm is so powerful that the victim will not resist being bitten by the vampire.",
            "Nocturnal Dominion:  Creatures of the night will obey the vampire.  This power allows control of one of the following: rats, bats, or wolves.  This power may be gained multiple times, granting dominion over a different type each time.  Dominion over Rats allows the vampire to call forth 10d10 rats or 5d4 giant rats; Dominion over Bats allows the vampire to summon  10d10 bats or 3d6 giant bats; and Dominion over Wolves allows the vampire to summon a pack of 3d6 wolves.  Each form of dominion can be used at most once per day, and dominion cannot be used twice within an hour (so it is not possible to summon both giant rats and wolves at the same time, for example).  The relevant type of creature must be \"nearby\" as determined by the GM, will arrive 2d6 rounds later, and will obey the vampire for up to an hour before leaving.",
            "Animal Transformation:  The vampire gains the ability to transform into any sort of creature over which it has dominion.  Obviously, this power can only be gained after at least one form of dominion is available.  The transformation requires a single round during which the vampire cannot attack.  The vampire can use the movement and attack forms of the animal shape assumed, as given in the Core Rules, while retaining its armor class, resistance to non-magical weapons, and regenerative abilities.  The vampire cannot use its charm or energy drain abilities while in animal form, but effects already active will remain so.",
            "Assume Gaseous Form (as the potion):  A vampire having this ability can shift into the form of a mist, moving at a \"flying\" rate of 50' per round.  Such a vampire cannot attack, use any of its abilities, or command any spawn or summoned animals while in this form.  Normally the vampire can resume its physical form in a single round.  If reduced to 0 or fewer hit points but still able to regenerate, a vampire having this power will automatically assume gaseous form and may move away as desired; in this case the vampire cannot resume its physical form until it has recovered at least 1 hit point (as explained above).",
            "Undead Control (minimum 10 hit dice):  The vampire can control other undead monsters.  The vampire must be able to see the undead to be controlled, and the attempt is rolled on the Clerics vs. Undead table in the Core Rules as if the vampire were a cleric of the same level as its hit dice.  Any undead who would be turned will serve for a limited time, generally up to an hour; any who would be destroyed will serve indefinitely.",
            "Destroying a Vampire:",
            "Ending the existence of a vampire is not an easy task, for the vampire must suffer as many points of permanent damage as it has hit points.  Besides the methods described above, a vampire can be destroyed by cremation in a funeral pyre while in any dormant state, such as when reduced to zero hit points by normal damage.",
            "The most dramatic method of defeating a vampire is actually the least reliable: driving a wooden stake through its heart.  Doing this will instantly reduce the vampire to zero hit points as if harmed by normal damage; regeneration is not possible while the stake is present.  Removal of the stake, however, allows the vampire to begin regenerating as described above.  It is not normally possible to drive a stake through a vampire's heart while it is actively resisting, but this can be done after reducing the monster to zero hit points in the usual way.  Of course, after staking a vampire it is possible to use sunlight, running water, or a funeral pyre as described above to complete its destruction.",
            "Vampires with Character Classes:",
            "Any character who has a class and level who becomes a vampire retains that class and level.  The vampire can no longer increase their level or learn new class abilities.  Treat such a vampire as being a sort of \"combination class\" where its attack bonus, hit points, and so on are the better of the figures from either its character class or its new monstrous nature.",
            "For example, a 7th level Thief who becomes a vampire remains a 7th level Thief but is now a 3 hit die Vampire Spawn as well.  The attack bonus of the character is +4, which is better than a 3 hit die monster's +3 AB, so the +4 figure will be used.  A 7th level Thief has about 18 hit points, while a 3 hit die monster has about 14; whichever actual roll is better represents the monster's actual hit points.  All thief abilities remain available, with the vampiric nature added to them."
        ],
        "hitdice": "11** (+9)",
        "hitdiceroll": [
            11,
            8,
            0
        ],
        "morale": "11",
        "movement": "40'",
        "name": "Vampire, 11 HD",
        "noappearing": "1d6, Wild 1d6, Lair 1d6",
        "noapproll": [
            1,
            6,
            0
        ],
        "noapprolllair": [
            1,
            6,
            0
        ],
        "noapprollwild": [
            1,
            6,
            0
        ],
        "noattacks": "1 punch or 1 weapon or 1 bite or gaze",
        "saveas": "Fighter: 11",
        "specialbonus": 2,
        "treasure": "F x 2",
        "xp": "1765"
    },
    "Vampire, 12 HD": {

        "armorclass": "21 (m)",
        "attackbonus": 10,
        "damage": "1d6+3 punch or 1d8+3 or by weapon +3 or 1d3 bite or save vs. Spell -2 or allow bite gaze",
        "description": [
            "Vampires are undead monsters.  Though they may look just a bit more pale than when they were alive, they do appear to live and even breathe as mortals do (though they do not, in fact, need to breathe to survive).  A vampire has all the memories and abilities it had in life, and is effectively immortal.  Living forever in the shadows often leads to vampires being decadent, while their hunger for blood makes them cruel.",
            "When a human (or, at the GMs option, some other living humanoid) is turned into a vampire it is called a vampire spawn.  Spawn normally begin with 3 hit dice; if a humanoid having more than 3 hit dice is turned, it will begin as a spawn with the number of hit dice it had in life, up to a maximum of 6.  Vampires who are able to feed regularly gain one hit die about every 10 years; some advance faster, some slower, and the GM may wish to roll 2d8+1 for the number of years a given vampire will need to advance a hit die (rolling again after each such gain).",
            "Vampires regenerate in a similar fashion to trolls, recovering 1 hit point per turn (not round) after damage is suffered.  Much like trolls, some forms of damage inflicted upon a vampire cannot be regenerated, such as damage from contact with holy water or exposure to sunlight.  This is called \"permanent damage\" though it can be healed by consuming life energy, as explained in the following paragraph.  Vampires do not heal \"normally\" as living creatures do, but can regain such lost hit points by drinking blood from living creatures.",
            "The vampire's bite inflicts 1d3 points of damage, then each round thereafter one energy level is drained from the victim.  Each level of energy drain inflicted permits the vampire to heal one point of permanent damage, or to regenerate a number of points of ordinary damage equal to the number of hit points lost by the victim.  If using the bite as an attack in combat, the vampire suffers a penalty of -5 to Armor Class due to the vulnerable position it must assume.",
            "If exposed to direct sunlight, the vampire will suffer 3d8 points of permanent damage each round.  Even a partial exposure inflicts 1d8 points of permanent damage.  No saving throw normally applies.",
            "If a vampire's victim is slain by the vampire's bite, the victim will arise as a vampire spawn at the next sunset (but not less than 12 hours later) and thereafter will be under the complete control of the \"parent\" vampire (the \"sire\") until such time as either victim or parent are destroyed.  This transformation can be prevented by driving a stake through the heart of the victim before it arises as a vampire (so long as the stake remains in place until after the event would have occurred).  Alternately, the victim can be recovered by casting restoration followed by raise dead.  One level of energy drain will be restored by this procedure.",
            "Vampires cast no reflections in silvered mirrors or water, though despite conventional wisdom to the contrary they do cast reflections in most other reflective materials; the innate purity of silver and water simply will not reflect them.",
            "Vampires are strong.  As shown on the table above, spawn receive a bonus of +1 to damage inflicted by melee weapons due to this strength, while more mature vampires receive a bonus of +2 or even +3.  Thus, a vampire will generally choose to use a melee weapon (or even its bare hands) in combat rather than attempting to bite.",
            "Vampires are unharmed by non-magical weapons, and like all undead are immune to sleep, charm, and hold spells.",
            "A vampire can be held at bay by several things, including the smell of garlic, a silver or silvered mirror, or a holy symbol presented by a believer (GM's discretion is advised here, but in general someone threatened by a vampire may be more devout than usual).  In such a situation the vampire cannot approach within 5 feet of the repellent item or character, nor can it make any melee attacks or otherwise touch those within the warded area.  If it can summon animals (see below), it can still direct them to attack.",
            "Fresh running water (such as a stream or river) acts as a barrier to a vampire; one cannot cross over any such waterway, neither by bridge or by waterway or even by flying.  It is possible for a vampire to be carried across while lying in its own coffin with the lid closed; the presence of the water flowing beneath the coffin will force the vampire to remain dormant.  Being immersed in running water causes 3d8 points of permanent damage each round.  Of course, vampires are damaged by holy water just with as all other undead monsters.",
            "A vampire may not enter any private dwelling without being invited by someone who resides there, and then only if invited while the resident is actually inside the structure.  Public buildings of any sort do not present this problem; even private rooms in inns are fully accessible to a vampire.",
            "If reduced to 0 hit points in combat, but still able to regenerate at least some of that damage, the vampire is not destroyed.  The vampire will begin to regenerate 1 hit point per turn after 2d6 turns, and may resume normal activity as soon as the first point is restored.  Do not tally negative hit points for a vampire, even if you do so for characters and/or monsters otherwise; if permanent damage is applied to a vampire which is dormant due to normal damage, the permanent damage is considered to override the same number of points of normal damage.",
            "Vampires of 7 hit dice or more are sires, maintaining control of all their own vampire spawn, and are no longer controlled by their own vampiric sire.  New vampires created by those having fewer than 7 hit dice are under the control of the creator's sire; when the creator reaches 7 hit dice it assumes control of all of its own spawn.",
            "Special Vampiric Abilities:",
            "Starting at 6 hit dice, a vampire gains an ability from the list below each time it gains a new hit die (until all abilities have been acquired).  These abilities are generally gained in the order given, but not always.",
            "Charm Gaze:  A vampire can charm any sentient living creature who meets its gaze; a save vs. Spells is allowed to resist, but at a penalty of -2 due to the power of the charm.  This charm is so powerful that the victim will not resist being bitten by the vampire.",
            "Nocturnal Dominion:  Creatures of the night will obey the vampire.  This power allows control of one of the following: rats, bats, or wolves.  This power may be gained multiple times, granting dominion over a different type each time.  Dominion over Rats allows the vampire to call forth 10d10 rats or 5d4 giant rats; Dominion over Bats allows the vampire to summon  10d10 bats or 3d6 giant bats; and Dominion over Wolves allows the vampire to summon a pack of 3d6 wolves.  Each form of dominion can be used at most once per day, and dominion cannot be used twice within an hour (so it is not possible to summon both giant rats and wolves at the same time, for example).  The relevant type of creature must be \"nearby\" as determined by the GM, will arrive 2d6 rounds later, and will obey the vampire for up to an hour before leaving.",
            "Animal Transformation:  The vampire gains the ability to transform into any sort of creature over which it has dominion.  Obviously, this power can only be gained after at least one form of dominion is available.  The transformation requires a single round during which the vampire cannot attack.  The vampire can use the movement and attack forms of the animal shape assumed, as given in the Core Rules, while retaining its armor class, resistance to non-magical weapons, and regenerative abilities.  The vampire cannot use its charm or energy drain abilities while in animal form, but effects already active will remain so.",
            "Assume Gaseous Form (as the potion):  A vampire having this ability can shift into the form of a mist, moving at a \"flying\" rate of 50' per round.  Such a vampire cannot attack, use any of its abilities, or command any spawn or summoned animals while in this form.  Normally the vampire can resume its physical form in a single round.  If reduced to 0 or fewer hit points but still able to regenerate, a vampire having this power will automatically assume gaseous form and may move away as desired; in this case the vampire cannot resume its physical form until it has recovered at least 1 hit point (as explained above).",
            "Undead Control (minimum 10 hit dice):  The vampire can control other undead monsters.  The vampire must be able to see the undead to be controlled, and the attempt is rolled on the Clerics vs. Undead table in the Core Rules as if the vampire were a cleric of the same level as its hit dice.  Any undead who would be turned will serve for a limited time, generally up to an hour; any who would be destroyed will serve indefinitely.",
            "Destroying a Vampire:",
            "Ending the existence of a vampire is not an easy task, for the vampire must suffer as many points of permanent damage as it has hit points.  Besides the methods described above, a vampire can be destroyed by cremation in a funeral pyre while in any dormant state, such as when reduced to zero hit points by normal damage.",
            "The most dramatic method of defeating a vampire is actually the least reliable: driving a wooden stake through its heart.  Doing this will instantly reduce the vampire to zero hit points as if harmed by normal damage; regeneration is not possible while the stake is present.  Removal of the stake, however, allows the vampire to begin regenerating as described above.  It is not normally possible to drive a stake through a vampire's heart while it is actively resisting, but this can be done after reducing the monster to zero hit points in the usual way.  Of course, after staking a vampire it is possible to use sunlight, running water, or a funeral pyre as described above to complete its destruction.",
            "Vampires with Character Classes:",
            "Any character who has a class and level who becomes a vampire retains that class and level.  The vampire can no longer increase their level or learn new class abilities.  Treat such a vampire as being a sort of \"combination class\" where its attack bonus, hit points, and so on are the better of the figures from either its character class or its new monstrous nature.",
            "For example, a 7th level Thief who becomes a vampire remains a 7th level Thief but is now a 3 hit die Vampire Spawn as well.  The attack bonus of the character is +4, which is better than a 3 hit die monster's +3 AB, so the +4 figure will be used.  A 7th level Thief has about 18 hit points, while a 3 hit die monster has about 14; whichever actual roll is better represents the monster's actual hit points.  All thief abilities remain available, with the vampiric nature added to them."
        ],
        "hitdice": "12** (+10)",
        "hitdiceroll": [
            12,
            8,
            0
        ],
        "morale": "11",
        "movement": "40'",
        "name": "Vampire, 12 HD",
        "noappearing": "1d6, Wild 1d6, Lair 1d6",
        "noapproll": [
            1,
            6,
            0
        ],
        "noapprolllair": [
            1,
            6,
            0
        ],
        "noapprollwild": [
            1,
            6,
            0
        ],
        "noattacks": "1 punch or 1 weapon or 1 bite or gaze",
        "saveas": "Fighter: 12",
        "specialbonus": 2,
        "treasure": "F x 2",
        "xp": "2075"
    },
    "Diabolus (Vampire), 4 HD": {

        "armorclass": "14 (m)",
        "attackbonus": 4,
        "damage": "2d6+4",
        "description": [
            "The Diabolus:",
            "When a vampire is starved of blood for an extended period it may degenerate into the form known as a diabolus.  The vampire becomes gaunt and even more pallid than before, and whatever hair it had falls out; its intelligence fades, replaced by vicious animal cunning.  The arms and legs seem to stretch weirdly, making it taller, though as they tend to walk in a hunched pose this may not be obvious.  Its jaws protrude and its fangs elongate, while its protruding eyes glow crimson.  The diabolus attacks living creatures with little concern for its own safety.",
            "A vampire must consume blood from a living creature at least once per month, draining at least one life energy level when doing so.  Each month the vampire cannot fulfill this need it must make a saving throw vs. Death Ray, with failure resulting in the vampire becoming a diabolus.  Within the first month after this transformation, the creature can be restored to its previous form by consuming at least as many energy levels as it has hit dice; after that period, no amount of blood can restore a diabolus to the normal vampiric state.",
            "A diabolus retains the normal abilities and weaknesses of a vampire, but loses any and all abilities listed above under Special Vampiric Abilities.  If the diabolus had a character class and level, it loses all access to all class features and statistics.  It gains one hit die over its previous vampiric form.  A diabolus no longer uses weapons, attacking only with its bite; it has a Morale of 12, and gains 20 feet of movement per round.  Other statistics remain the same as before its transformation.  It can resist damage from both sunlight and running fresh water for one round before taking damage as any other vampire.",
            "The creature also demonstrates a limited ability to change its shape, being able to sprout wings from its back over the course of two rounds, granting it limited flight (20').  It can also conceal itself within deep shadows, becoming 75% undetectable (similar to the thief ability Hide)."
        ],
        "hitdice": "4*",
        "hitdiceroll": [
            4,
            8,
            0
        ],
        "morale": "12",
        "movement": "50' or 60' Fly 20' (special)",
        "name": "Diabolus (Vampire), 4 HD",
        "noappearing": "1",
        "noapproll": [
            0,
            0,
            1
        ],
        "noattacks": "1 bite",
        "saveas": "Fighter: 4",
        "specialbonus": 1,
        "treasure": "None",
        "xp": "280"
    },
    "Diabolus (Vampire), 5 HD": {

        "armorclass": "15 (m)",
        "attackbonus": 5,
        "damage": "2d6+4",
        "description": [
            "The Diabolus:",
            "When a vampire is starved of blood for an extended period it may degenerate into the form known as a diabolus.  The vampire becomes gaunt and even more pallid than before, and whatever hair it had falls out; its intelligence fades, replaced by vicious animal cunning.  The arms and legs seem to stretch weirdly, making it taller, though as they tend to walk in a hunched pose this may not be obvious.  Its jaws protrude and its fangs elongate, while its protruding eyes glow crimson.  The diabolus attacks living creatures with little concern for its own safety.",
            "A vampire must consume blood from a living creature at least once per month, draining at least one life energy level when doing so.  Each month the vampire cannot fulfill this need it must make a saving throw vs. Death Ray, with failure resulting in the vampire becoming a diabolus.  Within the first month after this transformation, the creature can be restored to its previous form by consuming at least as many energy levels as it has hit dice; after that period, no amount of blood can restore a diabolus to the normal vampiric state.",
            "A diabolus retains the normal abilities and weaknesses of a vampire, but loses any and all abilities listed above under Special Vampiric Abilities.  If the diabolus had a character class and level, it loses all access to all class features and statistics.  It gains one hit die over its previous vampiric form.  A diabolus no longer uses weapons, attacking only with its bite; it has a Morale of 12, and gains 20 feet of movement per round.  Other statistics remain the same as before its transformation.  It can resist damage from both sunlight and running fresh water for one round before taking damage as any other vampire.",
            "The creature also demonstrates a limited ability to change its shape, being able to sprout wings from its back over the course of two rounds, granting it limited flight (20').  It can also conceal itself within deep shadows, becoming 75% undetectable (similar to the thief ability Hide)."
        ],
        "hitdice": "5*",
        "hitdiceroll": [
            5,
            8,
            0
        ],
        "morale": "12",
        "movement": "50' or 60' Fly 20' (special)",
        "name": "Diabolus (Vampire), 5 HD",
        "noappearing": "1",
        "noapproll": [
            0,
            0,
            1
        ],
        "noattacks": "1 bite",
        "saveas": "Fighter: 5",
        "specialbonus": 1,
        "treasure": "None",
        "xp": "405"
    },
    "Diabolus (Vampire), 6 HD": {

        "armorclass": "16 (m)",
        "attackbonus": 6,
        "damage": "2d6+4",
        "description": [
            "The Diabolus:",
            "When a vampire is starved of blood for an extended period it may degenerate into the form known as a diabolus.  The vampire becomes gaunt and even more pallid than before, and whatever hair it had falls out; its intelligence fades, replaced by vicious animal cunning.  The arms and legs seem to stretch weirdly, making it taller, though as they tend to walk in a hunched pose this may not be obvious.  Its jaws protrude and its fangs elongate, while its protruding eyes glow crimson.  The diabolus attacks living creatures with little concern for its own safety.",
            "A vampire must consume blood from a living creature at least once per month, draining at least one life energy level when doing so.  Each month the vampire cannot fulfill this need it must make a saving throw vs. Death Ray, with failure resulting in the vampire becoming a diabolus.  Within the first month after this transformation, the creature can be restored to its previous form by consuming at least as many energy levels as it has hit dice; after that period, no amount of blood can restore a diabolus to the normal vampiric state.",
            "A diabolus retains the normal abilities and weaknesses of a vampire, but loses any and all abilities listed above under Special Vampiric Abilities.  If the diabolus had a character class and level, it loses all access to all class features and statistics.  It gains one hit die over its previous vampiric form.  A diabolus no longer uses weapons, attacking only with its bite; it has a Morale of 12, and gains 20 feet of movement per round.  Other statistics remain the same as before its transformation.  It can resist damage from both sunlight and running fresh water for one round before taking damage as any other vampire.",
            "The creature also demonstrates a limited ability to change its shape, being able to sprout wings from its back over the course of two rounds, granting it limited flight (20').  It can also conceal itself within deep shadows, becoming 75% undetectable (similar to the thief ability Hide)."
        ],
        "hitdice": "6*",
        "hitdiceroll": [
            6,
            8,
            0
        ],
        "morale": "12",
        "movement": "50' or 60' Fly 20' (special)",
        "name": "Diabolus (Vampire), 6 HD",
        "noappearing": "1",
        "noapproll": [
            0,
            0,
            1
        ],
        "noattacks": "1 bite",
        "saveas": "Fighter: 6",
        "specialbonus": 1,
        "treasure": "None",
        "xp": "555"
    },
    "Diabolus (Vampire), 7 HD": {

        "armorclass": "17 (m)",
        "attackbonus": 7,
        "damage": "2d6+4",
        "description": [
            "The Diabolus:",
            "When a vampire is starved of blood for an extended period it may degenerate into the form known as a diabolus.  The vampire becomes gaunt and even more pallid than before, and whatever hair it had falls out; its intelligence fades, replaced by vicious animal cunning.  The arms and legs seem to stretch weirdly, making it taller, though as they tend to walk in a hunched pose this may not be obvious.  Its jaws protrude and its fangs elongate, while its protruding eyes glow crimson.  The diabolus attacks living creatures with little concern for its own safety.",
            "A vampire must consume blood from a living creature at least once per month, draining at least one life energy level when doing so.  Each month the vampire cannot fulfill this need it must make a saving throw vs. Death Ray, with failure resulting in the vampire becoming a diabolus.  Within the first month after this transformation, the creature can be restored to its previous form by consuming at least as many energy levels as it has hit dice; after that period, no amount of blood can restore a diabolus to the normal vampiric state.",
            "A diabolus retains the normal abilities and weaknesses of a vampire, but loses any and all abilities listed above under Special Vampiric Abilities.  If the diabolus had a character class and level, it loses all access to all class features and statistics.  It gains one hit die over its previous vampiric form.  A diabolus no longer uses weapons, attacking only with its bite; it has a Morale of 12, and gains 20 feet of movement per round.  Other statistics remain the same as before its transformation.  It can resist damage from both sunlight and running fresh water for one round before taking damage as any other vampire.",
            "The creature also demonstrates a limited ability to change its shape, being able to sprout wings from its back over the course of two rounds, granting it limited flight (20').  It can also conceal itself within deep shadows, becoming 75% undetectable (similar to the thief ability Hide)."
        ],
        "hitdice": "7*",
        "hitdiceroll": [
            7,
            8,
            0
        ],
        "morale": "12",
        "movement": "50' or 60' Fly 20' (special)",
        "name": "Diabolus (Vampire), 7 HD",
        "noappearing": "1",
        "noapproll": [
            0,
            0,
            1
        ],
        "noattacks": "1 bite",
        "saveas": "Fighter: 7",
        "specialbonus": 1,
        "treasure": "None",
        "xp": "735"
    },
    "Diabolus (Vampire), 8 HD": {

        "armorclass": "18 (m)",
        "attackbonus": 8,
        "damage": "2d6+4",
        "description": [
            "The Diabolus:",
            "When a vampire is starved of blood for an extended period it may degenerate into the form known as a diabolus.  The vampire becomes gaunt and even more pallid than before, and whatever hair it had falls out; its intelligence fades, replaced by vicious animal cunning.  The arms and legs seem to stretch weirdly, making it taller, though as they tend to walk in a hunched pose this may not be obvious.  Its jaws protrude and its fangs elongate, while its protruding eyes glow crimson.  The diabolus attacks living creatures with little concern for its own safety.",
            "A vampire must consume blood from a living creature at least once per month, draining at least one life energy level when doing so.  Each month the vampire cannot fulfill this need it must make a saving throw vs. Death Ray, with failure resulting in the vampire becoming a diabolus.  Within the first month after this transformation, the creature can be restored to its previous form by consuming at least as many energy levels as it has hit dice; after that period, no amount of blood can restore a diabolus to the normal vampiric state.",
            "A diabolus retains the normal abilities and weaknesses of a vampire, but loses any and all abilities listed above under Special Vampiric Abilities.  If the diabolus had a character class and level, it loses all access to all class features and statistics.  It gains one hit die over its previous vampiric form.  A diabolus no longer uses weapons, attacking only with its bite; it has a Morale of 12, and gains 20 feet of movement per round.  Other statistics remain the same as before its transformation.  It can resist damage from both sunlight and running fresh water for one round before taking damage as any other vampire.",
            "The creature also demonstrates a limited ability to change its shape, being able to sprout wings from its back over the course of two rounds, granting it limited flight (20').  It can also conceal itself within deep shadows, becoming 75% undetectable (similar to the thief ability Hide)."
        ],
        "hitdice": "8*",
        "hitdiceroll": [
            8,
            8,
            0
        ],
        "morale": "12",
        "movement": "50' or 60' Fly 20' (special)",
        "name": "Diabolus (Vampire), 8 HD",
        "noappearing": "1",
        "noapproll": [
            0,
            0,
            1
        ],
        "noattacks": "1 bite",
        "saveas": "Fighter: 8",
        "specialbonus": 1,
        "treasure": "None",
        "xp": "945"
    },
    "Diabolus (Vampire), 9 HD": {

        "armorclass": "19 (m)",
        "attackbonus": 8,
        "damage": "2d6+4",
        "description": [
            "The Diabolus:",
            "When a vampire is starved of blood for an extended period it may degenerate into the form known as a diabolus.  The vampire becomes gaunt and even more pallid than before, and whatever hair it had falls out; its intelligence fades, replaced by vicious animal cunning.  The arms and legs seem to stretch weirdly, making it taller, though as they tend to walk in a hunched pose this may not be obvious.  Its jaws protrude and its fangs elongate, while its protruding eyes glow crimson.  The diabolus attacks living creatures with little concern for its own safety.",
            "A vampire must consume blood from a living creature at least once per month, draining at least one life energy level when doing so.  Each month the vampire cannot fulfill this need it must make a saving throw vs. Death Ray, with failure resulting in the vampire becoming a diabolus.  Within the first month after this transformation, the creature can be restored to its previous form by consuming at least as many energy levels as it has hit dice; after that period, no amount of blood can restore a diabolus to the normal vampiric state.",
            "A diabolus retains the normal abilities and weaknesses of a vampire, but loses any and all abilities listed above under Special Vampiric Abilities.  If the diabolus had a character class and level, it loses all access to all class features and statistics.  It gains one hit die over its previous vampiric form.  A diabolus no longer uses weapons, attacking only with its bite; it has a Morale of 12, and gains 20 feet of movement per round.  Other statistics remain the same as before its transformation.  It can resist damage from both sunlight and running fresh water for one round before taking damage as any other vampire.",
            "The creature also demonstrates a limited ability to change its shape, being able to sprout wings from its back over the course of two rounds, granting it limited flight (20').  It can also conceal itself within deep shadows, becoming 75% undetectable (similar to the thief ability Hide)."
        ],
        "hitdice": "9* (+8)",
        "hitdiceroll": [
            9,
            8,
            0
        ],
        "morale": "12",
        "movement": "50' or 60' Fly 20' (special)",
        "name": "Diabolus (Vampire), 9 HD",
        "noappearing": "1",
        "noapproll": [
            0,
            0,
            1
        ],
        "noattacks": "1 bite",
        "saveas": "Fighter: 9",
        "specialbonus": 1,
        "treasure": "None",
        "xp": "1150"
    },
    "Diabolus (Vampire), 10 HD": {

        "armorclass": "20 (m)",
        "attackbonus": 9,
        "damage": "2d6+4",
        "description": [
            "The Diabolus:",
            "When a vampire is starved of blood for an extended period it may degenerate into the form known as a diabolus.  The vampire becomes gaunt and even more pallid than before, and whatever hair it had falls out; its intelligence fades, replaced by vicious animal cunning.  The arms and legs seem to stretch weirdly, making it taller, though as they tend to walk in a hunched pose this may not be obvious.  Its jaws protrude and its fangs elongate, while its protruding eyes glow crimson.  The diabolus attacks living creatures with little concern for its own safety.",
            "A vampire must consume blood from a living creature at least once per month, draining at least one life energy level when doing so.  Each month the vampire cannot fulfill this need it must make a saving throw vs. Death Ray, with failure resulting in the vampire becoming a diabolus.  Within the first month after this transformation, the creature can be restored to its previous form by consuming at least as many energy levels as it has hit dice; after that period, no amount of blood can restore a diabolus to the normal vampiric state.",
            "A diabolus retains the normal abilities and weaknesses of a vampire, but loses any and all abilities listed above under Special Vampiric Abilities.  If the diabolus had a character class and level, it loses all access to all class features and statistics.  It gains one hit die over its previous vampiric form.  A diabolus no longer uses weapons, attacking only with its bite; it has a Morale of 12, and gains 20 feet of movement per round.  Other statistics remain the same as before its transformation.  It can resist damage from both sunlight and running fresh water for one round before taking damage as any other vampire.",
            "The creature also demonstrates a limited ability to change its shape, being able to sprout wings from its back over the course of two rounds, granting it limited flight (20').  It can also conceal itself within deep shadows, becoming 75% undetectable (similar to the thief ability Hide)."
        ],
        "hitdice": "10* (+9)",
        "hitdiceroll": [
            10,
            8,
            0
        ],
        "morale": "12",
        "movement": "50' or 60' Fly 20' (special)",
        "name": "Diabolus (Vampire), 10 HD",
        "noappearing": "1",
        "noapproll": [
            0,
            0,
            1
        ],
        "noattacks": "1 bite",
        "saveas": "Fighter: 10",
        "specialbonus": 1,
        "treasure": "None",
        "xp": "1390"
    },
    "Diabolus (Vampire), 11 HD": {

        "armorclass": "21 (m)",
        "attackbonus": 9,
        "damage": "2d6+4",
        "description": [
            "The Diabolus:",
            "When a vampire is starved of blood for an extended period it may degenerate into the form known as a diabolus.  The vampire becomes gaunt and even more pallid than before, and whatever hair it had falls out; its intelligence fades, replaced by vicious animal cunning.  The arms and legs seem to stretch weirdly, making it taller, though as they tend to walk in a hunched pose this may not be obvious.  Its jaws protrude and its fangs elongate, while its protruding eyes glow crimson.  The diabolus attacks living creatures with little concern for its own safety.",
            "A vampire must consume blood from a living creature at least once per month, draining at least one life energy level when doing so.  Each month the vampire cannot fulfill this need it must make a saving throw vs. Death Ray, with failure resulting in the vampire becoming a diabolus.  Within the first month after this transformation, the creature can be restored to its previous form by consuming at least as many energy levels as it has hit dice; after that period, no amount of blood can restore a diabolus to the normal vampiric state.",
            "A diabolus retains the normal abilities and weaknesses of a vampire, but loses any and all abilities listed above under Special Vampiric Abilities.  If the diabolus had a character class and level, it loses all access to all class features and statistics.  It gains one hit die over its previous vampiric form.  A diabolus no longer uses weapons, attacking only with its bite; it has a Morale of 12, and gains 20 feet of movement per round.  Other statistics remain the same as before its transformation.  It can resist damage from both sunlight and running fresh water for one round before taking damage as any other vampire.",
            "The creature also demonstrates a limited ability to change its shape, being able to sprout wings from its back over the course of two rounds, granting it limited flight (20').  It can also conceal itself within deep shadows, becoming 75% undetectable (similar to the thief ability Hide)."
        ],
        "hitdice": "11* (+9)",
        "hitdiceroll": [
            11,
            8,
            0
        ],
        "morale": "12",
        "movement": "50' or 60' Fly 20' (special)",
        "name": "Diabolus (Vampire), 11 HD",
        "noappearing": "1",
        "noapproll": [
            0,
            0,
            1
        ],
        "noattacks": "1 bite",
        "saveas": "Fighter: 11",
        "specialbonus": 1,
        "treasure": "None",
        "xp": "1670"
    },
    "Diabolus (Vampire), 12 HD": {
        "armorclass": "21 (m)",
        "attackbonus": 10,
        "damage": "2d6+4",
        "description": [
            "The Diabolus:",
            "When a vampire is starved of blood for an extended period it may degenerate into the form known as a diabolus.  The vampire becomes gaunt and even more pallid than before, and whatever hair it had falls out; its intelligence fades, replaced by vicious animal cunning.  The arms and legs seem to stretch weirdly, making it taller, though as they tend to walk in a hunched pose this may not be obvious.  Its jaws protrude and its fangs elongate, while its protruding eyes glow crimson.  The diabolus attacks living creatures with little concern for its own safety.",
            "A vampire must consume blood from a living creature at least once per month, draining at least one life energy level when doing so.  Each month the vampire cannot fulfill this need it must make a saving throw vs. Death Ray, with failure resulting in the vampire becoming a diabolus.  Within the first month after this transformation, the creature can be restored to its previous form by consuming at least as many energy levels as it has hit dice; after that period, no amount of blood can restore a diabolus to the normal vampiric state.",
            "A diabolus retains the normal abilities and weaknesses of a vampire, but loses any and all abilities listed above under Special Vampiric Abilities.  If the diabolus had a character class and level, it loses all access to all class features and statistics.  It gains one hit die over its previous vampiric form.  A diabolus no longer uses weapons, attacking only with its bite; it has a Morale of 12, and gains 20 feet of movement per round.  Other statistics remain the same as before its transformation.  It can resist damage from both sunlight and running fresh water for one round before taking damage as any other vampire.",
            "The creature also demonstrates a limited ability to change its shape, being able to sprout wings from its back over the course of two rounds, granting it limited flight (20').  It can also conceal itself within deep shadows, becoming 75% undetectable (similar to the thief ability Hide)."
        ],
        "hitdice": "12* (+10)",
        "hitdiceroll": [
            12,
            8,
            0
        ],
        "morale": "12",
        "movement": "50' or 60' Fly 20' (special)",
        "name": "Diabolus (Vampire), 12 HD",
        "noappearing": "1",
        "noapproll": [
            0,
            0,
            1
        ],
        "noattacks": "1 bite",
        "saveas": "Fighter: 12",
        "specialbonus": 1,
        "treasure": "None",
        "xp": "1975"
    },
    "Diabolus (Vampire), 13 HD": {
        "armorclass": "21 (m)",
        "attackbonus": 10,
        "damage": "2d6+4",
        "description": [
            "The Diabolus:",
            "When a vampire is starved of blood for an extended period it may degenerate into the form known as a diabolus.  The vampire becomes gaunt and even more pallid than before, and whatever hair it had falls out; its intelligence fades, replaced by vicious animal cunning.  The arms and legs seem to stretch weirdly, making it taller, though as they tend to walk in a hunched pose this may not be obvious.  Its jaws protrude and its fangs elongate, while its protruding eyes glow crimson.  The diabolus attacks living creatures with little concern for its own safety.",
            "A vampire must consume blood from a living creature at least once per month, draining at least one life energy level when doing so.  Each month the vampire cannot fulfill this need it must make a saving throw vs. Death Ray, with failure resulting in the vampire becoming a diabolus.  Within the first month after this transformation, the creature can be restored to its previous form by consuming at least as many energy levels as it has hit dice; after that period, no amount of blood can restore a diabolus to the normal vampiric state.",
            "A diabolus retains the normal abilities and weaknesses of a vampire, but loses any and all abilities listed above under Special Vampiric Abilities.  If the diabolus had a character class and level, it loses all access to all class features and statistics.  It gains one hit die over its previous vampiric form.  A diabolus no longer uses weapons, attacking only with its bite; it has a Morale of 12, and gains 20 feet of movement per round.  Other statistics remain the same as before its transformation.  It can resist damage from both sunlight and running fresh water for one round before taking damage as any other vampire.",
            "The creature also demonstrates a limited ability to change its shape, being able to sprout wings from its back over the course of two rounds, granting it limited flight (20').  It can also conceal itself within deep shadows, becoming 75% undetectable (similar to the thief ability Hide)."
        ],
        "hitdice": "13* (+10)",
        "hitdiceroll": [
            13,
            8,
            0
        ],
        "morale": "12",
        "movement": "50' or 60' Fly 20' (special)",
        "name": "Diabolus (Vampire), 13 HD",
        "noappearing": "1",
        "noapproll": [
            0,
            0,
            1
        ],
        "noattacks": "1 bite",
        "saveas": "Fighter: 13",
        "specialbonus": 1,
        "treasure": "None",
        "xp": "2285"
    },
}


# end of file.
