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


dungeon_encounters = {
    "1": [
        (1, "monster",  "Bee, Giant"),
        (1, "monster",  "Goblin"),
        (1, "monster",  "Jelly, Green (Green Slime)"),
        (1, "monster",  "Kobold"),
        (1, "npc",      "Adventurer"),
        (1, "npc",      "Bandit"),
        (1, "monster",  "Orc"),
        (1, "monster",  "Stirge"),
        (1, "monster",  "Skeleton"),
        (1, "monster",  "Snake, Spitting Cobra"),
        (1, "monster",  "Spider, Giant Crab"),
        (1, "monster",  "Wolf"),
    ],
    "2": [
        (1, "monster",  "Beetle, Giant Bombardier"),
        (1, "monster",  "Fly, Giant"),
        (1, "monster",  "Ghoul"),
        (1, "monster",  "Gnoll"),
        (1, "monster",  "Jelly, Gray (Gray Ooze)"),
        (1, "monster",  "Hobgoblin"),
        (1, "monster",  "Lizard Man, Common"),
        (1, "npc",     "Adventurer"),
        (1, "monster",  "Snake, Pit Viper (and Rattlesnake)"),
        (1, "monster",  "Spider, Giant Black Widow"),
        (1, "monster",  "Lizard Man, Subterranean (Troglodyte)"),
        (1, "monster",  "Zombie"),
    ],
    "3": [
        (1, "monster",  "Ant, Giant"),
        (1, "monster",  "Ape, Carnivorous"),
        (1, "monster",  "Beetle, Giant Tiger"),
        (1, "monster",  "Bugbear"),
        (1, "monster",  "Doppleganger"),
        (1, "monster",  "Gargoyle"),
        (1, "monster",  "Jelly, Glass (Gelatinous Cube)"),
        (1, "monster",  "Lycanthrope, Wererat"),
        (1, "monster",  "Ogre"),
        (1, "monster",  "Shadow"),
        (1, "monster",  "Tentacle Worm"),
        (1, "monster",  "Wight"),
    ],
    "4": [
        (1, "monster",  "Bear, Cave"),
        (1, "monster",  "Caecilia, Giant"),
        (1, "monster",  "Cockatrice"),
        (1, "monster",  "Doppleganger"),
        (1, "monster",  "Jelly, Gray (Gray Ooze)"),
        (1, "monster",  "Hellhound"),
        (1, "monster",  "Rust Monster"),
        (1, "monster",  "Lycanthrope, Werewolf"),
        (1, "monster",  "Minotaur"),
        (1, "monster",  "Jelly, Ochre"),
        (1, "monster",  "Owlbear"),
        (1, "monster",  "Wraith"),
    ],
    "6": [
        (1, "monster",  "Basilisk, Common"),
        (1, "monster",  "Jelly, Black (Black Pudding)"),
        (1, "monster",  "Caecilia, Giant"),
        (1, "monster",  "Deceiver (Panther-Hydra)"),
        (1, "monster",  "Hydra, 6 Headed"),
        (1, "monster",  "Rust Monster"),
        (1, "monster",  "Lycanthrope, Weretiger"),
        (1, "monster",  "Mummy"),
        (1, "monster",  "Owlbear"),
        (1, "monster",  "Scorpion, Giant"),
        (1, "monster",  "Spectre"),
        (1, "monster",  "Troll"),
    ],
    "7": [
        (1, "monster",  "Basilisk, Common"),
        (1, "monster",  "Jelly, Black (Black Pudding)"),
        (1, "monster",  "Caecilia, Giant"),
        (1, "monster",  "Deceiver (Panther-Hydra)"),
        (1, "monster",  "Hydra, 7 Headed"),
        (1, "monster",  "Rust Monster"),
        (1, "monster",  "Lycanthrope, Weretiger"),
        (1, "monster",  "Mummy"),
        (1, "monster",  "Owlbear"),
        (1, "monster",  "Scorpion, Giant"),
        (1, "monster",  "Spectre"),
        (1, "monster",  "Troll"),
    ],
    "8": [
        (1, "monster",  "Basilisk, Greater"),
        (1, "monster",  "Chimera"),
        (1, "monster",  "Greater Deceiver"),
        (1, "monster",  "Giant, Hill"),
        (1, "monster",  "Giant, Stone"),
        (1, "monster",  "Hydra, 8 Headed"),
        (1, "monster",  "Jelly, Black (Black Pudding)"),
        (1, "monster",  "Lycanthrope, Wereboar"),
        (1, "monster",  "Purple Worm, 11 HD"),
        (1, "monster",  "Salamander, Flame"),
        (1, "monster",  "Salamander, Frost"),
        (1, "monster",  "Vampire, 7 HD"),
    ],
}

dungeon_encounters["5"] = dungeon_encounters["4"]

wilderness_encounters = {
    "desert": [
        ( 6, "monster", "Dragon, Desert (Blue Dragon)"),
        (12, "monster", "Hellhound"),
        (18, "monster", "Giant, Fire"),
        ( 2, "monster", "Purple Worm, 11 HD"),
        ( 3, "monster", "Purple Worm, 12 HD"),
        ( 3, "monster", "Purple Worm, 13 HD"),
        ( 3, "monster", "Purple Worm, 14 HD"),
        ( 3, "monster", "Purple Worm, 15 HD"),
        ( 3, "monster", "Purple Worm, 16 HD"),
        ( 2, "monster", "Purple Worm, 17 HD"),
        ( 2, "monster", "Purple Worm, 18 HD"),
        ( 2, "monster", "Purple Worm, 19 HD"),
        ( 1, "monster", "Purple Worm, 20 HD"),
        (30, "monster", "Fly, Giant"),
        (30, "monster", "Scorpion, Giant"),
        (36, "monster", "Camel"),
        (36, "monster", "Spider, Giant Tarantula"),
        (36, "npc",     "Merchant"),
        (30, "monster", "Hawk"),
        (30, "npc",     "Bandit"),
        (24, "monster", "Ogre"),
        (18, "monster", "Griffon"),
        (12, "monster", "Gnoll"),
        ( 6, "monster", "Dragon, Mountain (Red Dragon)"),
    ],
    "grass": [
        (1, "monster",  "Dragon, Plains (Yellow Dragon)"),
        (2, "monster",  "Troll"),
        (3, "monster",  "Fly, Giant"),
        (4, "monster",  "Scorpion, Giant"),
        (5, "npc",      "Bandit"),
        (5, "monster",  "Lion"),
        (6, "monster",  "Boar"),
        (6, "npc",      "Merchant"),
        (6, "monster",  "Wolf"),
        (5, "monster",  "Bee, Giant"),
        (5, "monster",  "Gnoll"),
        (4, "monster",  "Goblin"),
        (3, "monster",  "Blink Dog (Flicker Beast)"),
        (2, "monster",  "Wolf, Dire"),
        (1, "monster",  "Giant, Hill"),
    ],
    "inhabited-x": [
        (36, "npc",     "Merchant"),
    ],
    "inhabited": [
        ( 6, "monster", "Dragon, Cloud"),
        (12, "monster", "Ghoul"),
        (18, "monster", "Bugbear"),
        (24, "monster", "Goblin"),
        (30, "monster", "Centaur"),
        (30, "npc",     "Bandit"),
        (36, "npc",     "Merchant"),
        (36, "npc",     "Pilgrim"),
        (36, "npc",     "Noble"),
        (30, "monster", "Dog"),
        (30, "monster", "Gargoyle"),
        (24, "monster", "Gnoll"),
        (18, "monster", "Ogre"),
        (12, "monster", "Minotaur"),
        ( 3, "monster", "Vampire, 7 HD"),
        ( 2, "monster", "Vampire, 8 HD"),
        ( 1, "monster", "Vampire, 9 HD"),
    ],
    "jungle": [
        ( 6, "monster", "Dragon, Forest (Green Dragon)"),
        (12, "npc",     "Bandit"),
        (18, "monster", "Goblin"),
        (24, "monster", "Hobgoblin"),
        (30, "monster", "Centipede, Giant"),
        (30, "monster", "Snake, Python"),
        (36, "monster", "Elephant, Asiatic"),
        (36, "monster", "Antelope"),
        (36, "monster", "Jaguar"),
        (30, "monster", "Stirge"),
        (30, "monster", "Beetle, Giant Tiger"),
        (24, "monster", "Caecilia, Giant"),
        (18, "monster", "Shadow"),
        (12, "npc",     "Merchant"),
        ( 6, "monster", "Lycanthrope, Weretiger"),
    ],
    "mountains": [
        ( 6, "monster", "Dragon, Ice (White Dragon)"),
        ( 6, "monster", "Roc"),
        ( 4, "monster", "Roc, Large"),
        ( 2, "monster", "Roc, Giant"),
        (18, "monster", "Deceiver (Panther-Hydra)"),
        (24, "monster", "Lycanthrope, Werewolf"),
        (30, "monster", "Mountain Lion"),
        (30, "monster", "Wolf"),
        (36, "monster", "Spider, Giant Crab"),
        (36, "monster", "Hawk"),
        (36, "monster", "Orc"),
        (30, "monster", "Giant Bat"),
        (30, "monster", "Hawk, Giant"),
        (24, "monster", "Giant, Hill"),
        (18, "monster", "Chimera"),
        (12, "monster", "Wolf, Dire"),
        ( 6, "monster", "Dragon, Mountain (Red Dragon)"),
    ],
    "ocean": [
        ( 6, "monster", "Dragon, Sea (Gray Dragon)"),
        ( 2, "monster", "Hydra, 5 Headed"),
        ( 2, "monster", "Hydra, 6 Headed"),
        ( 2, "monster", "Hydra, 7 Headed"),
        ( 2, "monster", "Hydra, 8 Headed"),
        ( 1, "monster", "Hydra, 9 Headed"),
        ( 1, "monster", "Hydra, 10 Headed"),
        ( 1, "monster", "Hydra, 11 Headed"),
        ( 1, "monster", "Hydra, 12 Headed"),
        (18, "monster", "Whale, Sperm"),
        (24, "monster", "Crocodile, Giant"),
        (30, "monster", "Crab, Giant"),
        (30, "monster", "Whale, Killer"),
        (36, "monster", "Octopus, Giant"),
        (36, "monster", "Shark, Mako"),
        (36, "npc",     "Merchant Ship"),
        (30, "npc",     "Pirate"),
        (30, "monster", "Shark, Bull"),
        (15, "monster", "Roc, Large"),
        ( 9, "monster", "Roc, Giant"),
        (18, "monster", "Shark, Great White"),
        (12, "monster", "Mermaid"),
        ( 6, "monster", "Sea Serpent"),
    ],
    "river": [
        ( 6, "monster", "Dragon, Swamp (Black Dragon)"),
        (12, "monster", "Fish, Giant Piranha"),
        (18, "monster", "Stirge"),
        (24, "monster", "Fish, Giant Bass"),
        (30, "npc",     "Merchant Ship"),
        (30, "monster", "Lizard Man, Common"),
        (36, "monster", "Crocodile"),
        (36, "monster", "Frog, Giant"),
        (36, "monster", "Fish, Giant Catfish"),
        (30, "npc",     "Buccaneer"),
        (30, "monster", "Troll"),
        (24, "monster", "Jaguar"),
        (18, "monster", "Nixie"),
        ( 4, "monster", "Water Termite, Giant, 1 HD"),
        ( 3, "monster", "Water Termite, Giant, 2 HD"),
        ( 3, "monster", "Water Termite, Giant, 3 HD"),
        ( 2, "monster", "Water Termite, Giant, 4 HD"),
        ( 6, "monster", "Dragon, Forest (Green Dragon)"),
    ],
    "swamp": [
        ( 6, "monster", "Dragon, Swamp (Black Dragon)"),
        (12, "monster", "Shadow"),
        (18, "monster", "Troll"),
        (24, "monster", "Lizard, Giant Draco"),
        (30, "monster", "Centipede, Giant"),
        (30, "monster", "Leech, Giant"),
        (36, "monster", "Lizard Man, Common"),
        (36, "monster", "Crocodile"),
        (36, "monster", "Stirge"),
        (30, "monster", "Orc"),
        (30, "monster", "Toad, Giant"),
        (24, "monster", "Lizard Man, Subterranean (Troglodyte)"),
        (18, "monster", "Blood Rose"),
        (12, "monster", "Hangman Tree"),
        ( 6, "monster", "Basilisk, Common"),
    ],
    "forest": [
        ( 6, "monster", "Dragon, Forest (Green Dragon)"),
        (12, "monster", "Alicorn"),
        (18, "monster", "Treant"),
        (24, "monster", "Orc"),
        (30, "monster", "Boar"),
        (30, "monster", "Bear, Black"),
        (36, "monster", "Hawk, Giant"),
        (36, "monster", "Antelope"),
        (36, "monster", "Wolf"),
        (30, "monster", "Ogre"),
        (30, "monster", "Bear, Grizzly (or Brown)"),
        (24, "monster", "Wolf, Dire"),
        (18, "monster", "Giant, Hill"),
        (12, "monster", "Owlbear"),
        ( 6, "monster", "Unicorn"),
    ],
}

city_encounters = {
    "day": [
        ( 6, "monster", "Doppleganger"),
        (12, "npc",     "Noble"),
        (18, "npcenc",  "Thief"),
        (24, "npcenc",  "Bully"),
        (30, "npcenc",  "City Watch"),
        (30, "npcenc",  "Merchant"),
        (30, "npcenc",  "Beggar"),
        (24, "npcenc",  "Priest"),
        (18, "npcenc",  "Mercenary"),
        (12, "npcenc",  "Wizard"),
        ( 6, "monster", "Lycanthrope, Wererat"),
    ],
    "night": [
        ( 6, "monster", "Doppleganger"),
        (12, "monster", "Shadow"),
        (18, "npcenc",  "Press Gang"),
        (24, "npcenc",  "Beggar"),
        (30, "npcenc",  "Thief"),
        (30, "npcenc",  "Bully"),
        (30, "npcenc",  "Merchant"),
        (24, "monster", "Rat, Giant"),
        (18, "npcenc",  "City Watch"),
        (12, "npcenc",  "Wizard"),
        ( 6, "monster", "Lycanthrope, Wererat"),
    ],
}

if __name__ == "__main__":
    from _CoreMonsters import monsters
    import _BeastsOfBurden
    for key in _BeastsOfBurden.monsters:
        monsters[key] = _BeastsOfBurden.monsters[key]
    for key in sorted(dungeon_encounters.keys()):
        for odds, typ, name in dungeon_encounters[key]:
            if typ == "monster":
                if name not in monsters:
                    print("dungeon", key, name)
    for key in sorted(wilderness_encounters.keys()):
        for odds, typ, name in wilderness_encounters[key]:
            if typ == "monster":
                if name not in monsters:
                    print("wilderness", key, name)
    for key in sorted(city_encounters.keys()):
        for odds, typ, name in city_encounters[key]:
            if typ == "monster":
                if name not in monsters:
                    print("wilderness", key, name)


# end of file.
