# Basic Fantasy RPG Dungeoneer Suite
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


monsters = {
"Camel": {
    "armorclass": "13",
    "attackbonus": 2,
    "damage": "1 point bite, 1d4 hoof",
    "description": [
        "Camels are large animals found in arid environments that bear distinctive fatty",
        "deposits known as \"humps\" on their backs. There are two relevant species of",
        "camel described here: the far more common one-humped dromedary, and the",
        "two-humped Bactrian camel.  Statistics presented above are for the dromedary;",
        "the Bactrian camel is slower and its movement is given in brackets.  A light",
        "load for a camel is up to 400 pounds; a heavy load, up to 800 pounds."
    ],
    "hitdice": "2",
    "hitdiceroll": [
        2,
        8,
        0
    ],
    "morale": "7",
    "movement": "50' (10') [ 40' (10') ]",
    "name": "Camel",
    "officialname": "Camel",
    "noappearing": "Wild 2d4",
    "noapprollwild": [
        2,
        4,
        0
    ],
    "noattacks": "1 bite, 1 hoof",
    "saveas": "Fighter: 2",
    "specialbonus": 0,
    "xp": "75"
},
"Donkey": {
    "armorclass": "13",
    "attackbonus": 2,
    "damage": "1d2 bite",
    "description": [
        "Donkeys are hoofed mammals in the same family as the horse.  They are smaller,",
        "but are strong and hardy.  Burros are a similar species, and the statistics",
        "herein can be used for either; both varieties are capable of being taken into",
        "dungeons as pack animals.  A light load for a donkey is up to 70 pounds; a",
        "heavy load, up to 140 pounds."
    ],
    "hitdice": "2",
    "hitdiceroll": [
        2,
        8,
        0
    ],
    "morale": "7",
    "movement": "40' (10')",
    "name": "Donkey",
    "officialname": "Donkey",
    "noappearing": "Wild 2d4",
    "noapprollwild": [
        2,
        4,
        0
    ],
    "noattacks": "1 bite",
    "saveas": "Fighter: 2",
    "specialbonus": 0,
    "xp": "75"
},
"Horse, Draft": {
    "armorclass": "13",
    "attackbonus": 3,
    "damage": "1d4 hoof",
    "description": [
        "Draft Horses are large horses bred to be working animals doing hard tasks such",
        "as plowing and other farm labor. There are a number of breeds, with varying",
        "characteristics, but all share common traits of strength, patience, and a",
        "docile temperament.  A light load for a draft horse is up to 350 pounds; a",
        "heavy load, up to 700 pounds."
    ],
    "hitdice": "3",
    "hitdiceroll": [
        3,
        8,
        0
    ],
    "morale": "7",
    "movement": "60' (10')",
    "name": "Draft Horse",
    "officialname": "Horse, Draft",
    "noappearing": "domestic only",
    "noattacks": "2 hooves",
    "saveas": "Fighter: 3",
    "specialbonus": 0,
    "xp": "145"
},
"Horse, Riding": {
    "armorclass": "13",
    "attackbonus": 2,
    "damage": "1d4 hoof",
    "description": [
        "Riding Horses are smaller horses bred and trained for riding.  They cannot",
        "effectively fight while the rider is mounted.  A light load for a riding horse",
        "is up to 250 pounds; a heavy load, up to 500 pounds."
    ],
    "hitdice": "2",
    "hitdiceroll": [
        2,
        8,
        0
    ],
    "morale": "7",
    "movement": "80' (10')",
    "name": "Riding Horse",
    "officialname": "Horse, Riding",
    "noappearing": "Wild 10d10",
    "noapprollwild": [
        10,
        10,
        0
    ],
    "noattacks": "2 hooves",
    "saveas": "Fighter: 2",
    "specialbonus": 0,
    "xp": "75"
},
"Horse, War": {
    "armorclass": "13",
    "attackbonus": 3,
    "damage": "1d6 hoof",
    "description": [
        "War Horses are large, powerful horses which are both bred for their size,",
        "strength, and combat ability and trained to tolerate the sounds and stresses of",
        "battle.  They are able to attack while the rider is mounted due to their",
        "training.  A light load for a warhorse is up to 350 pounds; a heavy load, up to",
        "700 pounds."
    ],
    "hitdice": "3",
    "hitdiceroll": [
        3,
        8,
        0
    ],
    "morale": "9",
    "movement": "60' (10')",
    "name": "War Horse",
    "officialname": "Horse, War",
    "noappearing": "domestic only",
    "noattacks": "2 hooves",
    "saveas": "Fighter: 3",
    "specialbonus": 0,
    "xp": "145"
},
"Mule": {
    "armorclass": "13",
    "attackbonus": 2,
    "damage": "1d4 kick, 1d2 bite",
    "description": [
        "Mules are a domestic equine hybrid between a donkey and a horse.  Mules vary",
        "widely in size, and may be of any color.  They are more patient, hardier and",
        "longer-lived than horses, and are perceived as less obstinate and more",
        "intelligent than donkeys.  Like donkeys, they are capable of being taken into",
        "dungeons as pack animals.  A light load for a mule is up to 300 pounds; a heavy",
        "load, up to 600 pounds."
    ],
    "hitdice": "2",
    "hitdiceroll": [
        2,
        8,
        0
    ],
    "morale": "7",
    "movement": "40' (10')",
    "name": "Mule",
    "officialname": "Mule",
    "noappearing": "domestic only",
    "noattacks": "1 kick or 1 bite",
    "saveas": "Fighter: 2",
    "specialbonus": 0,
    "xp": "75"
},
"Pony": {
    "armorclass": "13",
    "attackbonus": 1,
    "damage": "1d4 bite",
    "description": [
        "A Pony is a variety of small horse. Compared to a larger horse, a pony may have",
        "a thicker coat, mane and tail, with proportionally shorter legs, a wider",
        "barrel, heavier bone, a thicker neck and a shorter, broader head.  Ponies can",
        "be trained for war, and the morale in parentheses above is for a war pony; this",
        "does not allow them to fight while a rider is mounted, however.  A light load",
        "for a pony is up to 275 pounds; a heavy load, up to 550 pounds."
    ],
    "hitdice": "1",
    "hitdiceroll": [
        1,
        8,
        0
    ],
    "morale": "6 (9)",
    "movement": "40' (10')",
    "name": "Pony",
    "officialname": "Pony",
    "noappearing": "domestic only",
    "noattacks": "1 bite",
    "saveas": "Fighter: 1",
    "specialbonus": 0,
    "xp": "25"
},
}


# end of file.
