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


import random
from . import Spells, Dice, Tables, ODT, Formatter


# *******************************************************************************************************
# Table Definitions

# character classes are often represented as indexes
# 0 = cleric, 1 = fighter, 2 = magic-user, 3 = thief
classnames = ( "Cleric", "Fighter", "Magic-User", "Thief" )
primes = [ 2, 0, 1, 3 ]
statnames = (
    ( "STR", "Strength" ),
    ( "INT", "Intelligence" ),
    ( "WIS", "Wisdom" ),
    ( "DEX", "Dexterity" ),
    ( "CON", "Constitution" ),
    ( "CHA", "Charisma" ),
)

levels = (
    ( 0, 0, 0, 0 ),
    ( 1, 1, 1, 1 ),
    ( 2, 2, 1, 2 ),
    ( 3, 3, 2, 3 ),
    ( 4, 4, 3, 4 ),
    ( 5, 5, 4, 5 ),
    ( 6, 6, 5, 6 ),
    ( 7, 7, 6, 7 ),
    ( 8, 8, 7, 8 ),
    ( 9, 9, 8, 10 ),
    ( 11, 10, 9, 11 ),
)


# names are courtesy of the Dragonsfoot Book of Names available from www.dragonsfoot.org

names = ( "A'kk", "Aarkosh", "Aarne", "Aazad", "Aban", "Abbad", "Abbas", "Abednego", "Abniki", "Adar",
"Adib", "Adiba", "Adjo", "Aedan", "Aelyina", "Aengus", "Aeron", "Afaf", "Affan", "Afia",
"Afifa", "Afrikaisi", "Agon", "Ahlam", "Ailbe", "Ailill", "Aimo", "Aina", "Aino", "Aisheisha",
"Ajwad", "Akana", "Akaro", "Akhom", "Ako", "Akori", "Akorit", "Alan", "Alauna", "Alazon",
"Albarez", "Alderon", "Aleksanteri", "Aleksi", "Allam", "Allan", "Allanor", "Allsie", "Almas", "Aloli",
"Alopex", "Alquraishi", "Alroy", "Alsheimer", "Alu", "Aluvian", "Alva", "Amaco", "Amahte", "Amal",
"Amaya", "Ambalo", "Amenemhet", "Amenhotep", "Amenitra", "Amir", "Amira", "Amisi", "Ammar", "Amonit",
"Amvalo", "Anbar", "Ancarr", "Andar", "Anden", "Ander", "Andrax", "Andronicus", "Anemro", "Angus",
"Anhamant", "Anhuri", "Anhurit", "Aniq", "Anja", "Ankhesenamen", "Annika", "Annuka", "Anok", "Antar",
"Anu", "Aodhan", "Apoqulis", "Appppil", "Aramath", "Arborius", "Arcan", "Ardan", "Areej", "Arilea",
"Arkadeus", "Arlock", "Armas", "Armo", "Armstrong", "Arn", "Arolian", "Arregala", "Arrowind", "Art",
"Artaxus", "Artimoff", "Arto", "Arttu", "Arturo", "Arvo", "Arwa", "Arwarh", "Ashai", "Ashier",
"Ashraf", "Asif", "Asil", "Asir", "Askari", "Astacoe", "Athar", "Atheos", "Ati", "Auken",
"Aurelio", "Aurora", "Avar", "Avenida", "Aversa", "Awan", "Awi", "Awwab", "Axeblade", "Ayaz",
"Ayham", "Ayman", "Ayrseer", "Azhaar", "Azhar", "Azizah", "Azra", "Azus", "B'yak", "Baariq",
"Baba", "Badr", "Badriya", "Bahia", "Bahija", "Bahja", "Bai", "Baki", "Bakir", "Bakit",
"Bakker", "Bakkon", "Baligha", "Balorik", "Balt", "Banafrit", "Banan", "Banner", "bar'Kazor", "Baraka",
"Bari", "Barirah", "Barit", "Barlathotep", "Barros", "Bartholomer", "Bartleby", "Bartley", "Basha'ir", "Bashasha",
"Bashira", "Basil", "Basim", "Basima", "Bathallas", "Batul", "Baz", "Beatrijs", "bel Callan", "Belladonna",
"belTrajan", "Benipe", "Beorn", "Bergeroi", "Bergethus", "Betuke", "Biddleriggs", "BigPig", "Bilqis", "Bimblebomb",
"Bisi", "Biti", "Bjarnni", "Blackgem", "Blaise", "Blasto", "Blumbo", "Bofur", "Boki", "Bolen",
"Bork", "Bortoka", "Bower", "Bradan", "Brak", "Bral", "Brand", "Branna", "Breandan", "Brecca",
"Brenden", "Briar", "Bronn", "Brovus", "Bubu", "Buckley", "Budur", "Buikhu", "Burdalane", "Burok",
"Bushra", "Bweengar", "Bylo", "Cabhan", "Cabral", "Cadron", "Cagbral", "Calanor", "Cale", "Caledon",
"Calvin/Kalvin", "Canas", "Cander", "Canice", "Carantha", "Cardax", "Cark", "Carnby", "Carney", "Caronal",
"Carrick", "Cartmange", "Castenada", "Cathal", "Cearney", "Cearul", "Cellini", "Cellowyn", "Chadmister", "Chalcis",
"Chambers", "Chanda", "Charduush", "Chlorianna", "Cian", "Ciaran", "Cillian", "Cioffi", "Cirak", "Clarice",
"Clearie", "Climmie", "Clooney", "Clyte", "Coilin", "Coinneach", "Colita", "Colm", "Colmcille", "Colum",
"Columba", "Conan", "Conlaoch", "Conleth", "Connla", "Connor", "Cooley", "Cord", "Cordain", "Corethal",
"Cormac", "Corwin", "Coussan", "Crill", "Crine", "Cronan", "Crow", "Cumberground", "Cuo", "Cuthalion",
"Cybill", "Cynoweth", "Cynthia", "D'Avalon", "D'Haveral", "D'Nav", "Dain", "Dainna", "Daire", "Daithi",
"Dalaigh", "Dalal", "Dalgar", "Dao", "Dar", "Dara", "Darcy", "Dargon", "Darian", "Darius",
"Darkblade", "Daro", "Davanir", "Davin", "de Vries", "Deaglan", "Deathbreaker", "Delvalle", "Den", "Denari",
"denCadal", "Dendro", "Derbren", "Dergo", "Derik", "Dern", "Derry", "Dertucken", "Derwin", "Desmond",
"Devon", "Dholgir", "Dhonjen", "Diarmuid", "Diggins", "Dillon", "Din", "Dinoia", "Diwan", "Djabenusiri",
"Djadao", "DjaDja", "Djal", "Djeserit", "Donal", "Donar", "Donnamira", "Donncha", "Doomis", "Dorian",
"Dracul", "Dragoncrest", "Dragonfang", "Drake", "Drako", "Drashen", "Drithelm", "Drizzen", "Drogo", "Drumble",
"Du'Shkar", "Dubhlain", "Ducky", "Dumystor", "Durriyah", "Duvera", "Dwine", "Dye", "Eamon", "Earth-fast",
"Eastwoods", "Ebe", "Ebio", "Ebonrain", "Ecthelander", "Eero", "Effington", "Eirnin", "Eizenga", "Ekibe",
"Elden", "Elderon", "Eldfather", "Eldmother", "Eljas", "Elvengrond", "Embranglement", "Emmet", "Emu", "Emuishe",
"Enda", "Endil", "Endra", "Endrallion", "Ennis", "Enoch", "Ensio", "Eoghan", "Eohyl", "Eoras",
"Ephrata", "Erikmund", "Erkki", "Erno", "Eron", "Escrill", "Esho", "Esperanza", "Eujue", "Evenhood",
"Faber", "Fadwa", "Faelon", "Faiq", "Faiqa", "Faiza", "Fakih", "Faldren", "Fante", "Faolan",
"Faqih", "Farah", "Fargon", "Farha", "Faryal", "Fatema", "Fatih", "Faustimagus", "Feidhelm", "Felga",
"Fellbottom", "Felth", "Fen", "Feng", "Fengaris", "Fenix", "Ferdia", "Fergal", "Fergus", "Feringald",
"Fernelius", "Fero", "Finbar", "Finister", "Fintan", "Fionn", "Firdaus", "Flade", "Fleabo", "Forge",
"Forswunk", "Foutch", "Foxglove", "Frans", "Fredrik", "Frits", "Frizzle", "Furbottom", "Gabryl", "Galadhremin",
"Galadin", "Galahra", "Galyn", "Garag", "Gatlin", "Gautreau", "Gearoid", "Gedreka", "Gegor", "Geledeth",
"Germariliz", "Gerronalyde", "Ghada", "Ghunwah", "Gimbalim", "Gino", "Girn", "Glafira", "Glendon", "Gloramir",
"Goldenstaff", "Gore", "Goreic", "Gou", "Gowl", "Grandy", "Grantier", "Grasseyes", "Graveolent", "Greenleaf",
"Greensmith", "Greyforn", "Griff", "Grilloch", "Grog", "Grom", "Grond", "Gronnon", "Gruel", "Guilbeau",
"Gull", "Gulliver", "Gulnar", "Gurek", "Gwynhynyr", "Haaver", "Hafgar", "Hafsa", "Hagatha", "Haidar",
"Haitham", "Hajar", "Haji", "Halden", "Hallden", "Hamdan", "Hamu", "Hamza", "Hannes", "Hannu",
"Hardel", "Hare", "Harg", "Hariz", "Harri", "Hasan", "Hashim", "Havard", "Hawk", "Hawkeye",
"Hawwa", "Healingwinds", "Heath", "Hebony", "Hehepsit", "Hehepsu", "Heikki", "Heino", "Helka", "Hella",
"Hellspike", "Helmi", "Helo-os", "Hemlock", "Henk", "Henriikka", "Henrikki", "Henry", "Hermanni", "Hermiston",
"Hesekiel", "Highpocket", "Hildron", "Hilja", "Hillevi", "Hime", "Hind", "Hiplak", "Hisham", "Hiunelray",
"Hoelzel", "Hortenberry", "Hrog", "Hugh", "Huiley", "Humam", "Huriya", "Husain", "Husna", "Iabi",
"Ialu", "Ibenre", "Ibon", "Ibtihaj", "Ibtihal", "Ibtisam", "Iffat", "Iika", "Iines", "Iiro",
"Iisakki", "Ilham", "Iliff", "Illmillio", "Ilmari", "Ilona", "Ilse", "Ilthmier", "Ilusia", "Imad",
"Impi", "Inas", "Indira", "Inka", "Inkeri", "Intisar", "Iollan", "Iqbal", "Irisi", "Irja",
"Irma", "Ironhead", "Ironshield", "Isam", "Ishraq", "Islemount", "Ismo", "Itafe", "Itennu", "Ithimar",
"Itidal", "Itimad", "Itran", "Izlldorf", "Jaakko", "Jacob", "Jadren", "Jalal", "Jalmari", "Jamal",
"Jamil", "Jamila", "Jan", "Jang", "Janisak", "Janna", "Jansen", "Jari", "Jarlath", "Jasim",
"Jasmin", "Jawhara", "Jawwad", "Jax", "Jelanie", "Jesper", "Jolosh", "Jonathon", "Joonas", "Jorgos",
"Jos", "Joszef", "Joth", "Jouko", "Juha", "Jukka", "Juleis", "Justin", "Juwairiyah", "Jyri",
"Kahotep", "Kai", "Kaija", "Kalevi", "Kalle", "Kalythalas", "Kamenwati", "Kamil", "Kamila", "Kappo",
"Kargas", "Karjos", "Karn", "Karva", "Kauko", "Kaur", "Kausar", "Kazatelli", "Kchime", "Kebi",
"Kegroller", "Kellin", "Kelp", "Kemamonit", "Kemisi", "Kemnebi", "Kemosiri", "Kemreit", "Kemsa", "Kemse",
"Ken", "Kensen", "Kepi", "Kerning", "Kerttu", "Kettwig", "Kevan", "Khadeeja", "Khai", "Khait",
"Khansa", "Khawlah", "Khenti", "Khurin", "Kiara", "Kifi", "Kijoran", "Kimmin", "Kino", "Kiwu",
"Koebel", "Kohout", "Korben", "Kordon", "Korr", "Korrin", "Korvola", "Kothar", "Kratel", "Kray",
"Kremble", "Krezak", "Krimdabar", "Krisella", "Kristian", "Kryllan", "Kufu", "Kurbis", "Kyron", "Labib",
"Lacayan", "Lagramar", "Laila", "Laith", "Lalonde", "Lanasa", "Lanaxis", "Lance", "Lanefan", "Lanken",
"Lapierre", "Larilyne", "Laris", "Larn", "Lars", "Lasherr", "Lathan", "Laulunen", "Lee", "LeMoore",
"Lempi", "Leonidas", "Lerone", "Lerrad", "Lexington", "Liam", "Lilly", "Linden", "Linke", "Llkuth",
"Lochlan", "Logan", "Lohann", "Londenberg", "Longfoot", "Lonth", "Lorak", "Lorcan", "Lorendal", "Lottinville",
"Lucien", "Lugrom", "Lulua", "Lupinus", "Lynesius", "Lyssa", "Ma'ali", "Maarit", "Macabranse", "Macayan",
"Machette", "Magness", "Magnus", "Mahasin", "Mahdi", "Maimbled", "Maimuna", "Mainio", "Mais", "Maisa",
"Maisara", "Maisun", "Makar", "Makarim", "Malachi", "Malak", "Malaki", "Malcom", "Malika", "Maliki",
"Malise", "Malison", "Mammix", "Manal", "Manar", "Mandrax", "Mansur", "Manu", "Maram", "Marcus",
"Mariha", "Marillia", "Marja", "Marjaana", "Marjami", "Marjo", "Marjukka", "Marko", "Marlez", "Martti",
"Marvene", "Marwan", "Marya", "Maryam", "Masquit", "Matias", "Mauri", "Mawahib", "Maxamillion", "Maximus",
"Mayesa", "Maynard", "Mayovsky", "McElreath", "Mclimans", "Mdjai", "Mede", "Meelath", "Megaron", "Mehnit",
"Meldros", "Melkiresha", "Melodra", "Melum", "Menetnashte", "Meri", "Merit", "Meskenit", "Mesmer", "Meti",
"Metit", "Mhotep", "Mie", "Mika", "Mikael", "Mikko", "Ming", "Miradonna", "Miranda", "Miu",
"Mkalbuti", "Mkhai", "Mkhait", "Mkit", "Mkitiris", "Mnoti", "Moffle", "Mogrim", "Mohot", "Moonthorn",
"Mophat", "Mor", "Moreno", "Morg", "Morganish", "Moricantu", "Mosha", "Mosto", "Mshai", "Mtidja",
"Muaz", "Mume", "Muna", "Muniba", "Munira", "Munsif", "Muntasir", "Muntuhotep", "Murad", "Murtagh",
"Muslih", "Myr", "Nadar", "Nafre", "Nafretiri", "Nafretiti", "Nafrini", "Nafrit", "Nail", "Nane",
"Nanu", "Nardak", "Nathan", "Nazar", "Neal", "Neb", "Nebi", "Nebibi", "Nebibit", "Nebit",
"Nebt", "Nebtawi", "Nebti", "Neckritz", "Nehru", "Nel", "Neomund", "Neshmal", "Nevara", "Nevin",
"Nex", "Niall", "Niamh", "Nieto", "Nifen-Ankh", "Niina", "Niko", "Nildhevin", "Nimblefingers", "Nivek",
"Nodo", "Nofrotete", "Nollaig", "Nomti", "Northcrosse", "Nsu", "Nubi", "Nubit", "Nubiti", "Oakshield",
"Oakworthy", "Oba", "Occosleus", "Odhran", "Odji", "Odjit", "Ogg", "Ogunyli", "Oillyan", "Oisin",
"Oiva", "Olavi", "Onni", "Onyg", "Or", "Oran", "Orian", "Orin", "Orvokki", "Orzo",
"Oshairana", "Oskari", "Osmund", "Otto", "Oweyn", "Owyn", "Paavo", "Padraic", "Pallenstein", "Palz",
"Panahasi", "Paniwi", "Pantego", "Paranor", "Parrino", "Passel", "Peadar", "Pearse", "Pekka", "Penguin",
"Pete", "Petra", "Petri", "Phelp", "Phi", "Phillip", "Phireal", "Pirkko", "Plaisance", "Pollari",
"Popehn", "Porphyriel", "Proinsias", "Ptermtec", "Quaddy", "Que'flnrnl", "Queachy", "Quellius", "Queq", "Quickfoot",
"Quicksword", "Quinlan", "Quinlivan", "Raakel", "Radiant", "Radivarl", "Radugish", "Rae", "Rael", "Raeneriac",
"Ragnar", "Raimo", "Rakeisha", "Ralus", "Ramfthar", "Rami", "Rasilitip", "Rasui", "Rath", "Rathwynn",
"Ravenzen", "Redmond", "Redwood", "Reino", "Reko", "Relentine", "Rellellalora", "Relmorak", "Remmao", "Renaldo",
"Renger", "Ressinfyr", "Revlis", "Revum", "Riika", "Rikard", "Rikhard", "Riley", "Rimsa", "Rimson",
"Rindle", "Ristan", "Risto", "Riveness", "Robideau", "Rockthorn", "Rodedaugh", "Rodger", "Rogan", "Roma",
"Romali", "Ronan", "Rondor", "Rooks", "Roope", "Roth", "Rourke", "Ruari", "Ruuben", "Ryfilke",
"Sabber", "Sabe", "Sadji", "Sadric", "Saini", "Sakari", "Sakke", "Salidji", "Salomon", "Sampson",
"Sancherok", "Sanieqwa", "Santtu", "Sari", "Saris", "Sarpkin", "Saugus", "Saul", "Sautner", "Savanna",
"Savic", "Scales", "Seafi", "Seafoam", "Seamus", "Sean", "Sebi", "Seini", "Selene", "Semni",
"Senja", "Seppo", "Sera", "Serella", "Serioge", "Seti", "Severi", "Severn", "Shadrach", "Shai",
"Shai-nefer", "Shalam", "Shambla", "Shamise", "Shantefeire", "Sharana", "Sharshell", "Shashaiti", "She", "Shea",
"Sheba", "Shebi", "Shel'lecryn", "Shelanier", "Shemeit", "Sheni", "Shenti", "Shepsit", "Sheriti", "Shinicle",
"Sho", "Shobog", "Shoshana", "Shun", "Shushu", "Silbach", "Silja", "Silverblade", "Silvereye", "Silverleaf",
"Silversword", "Simo", "Simon", "Sinikka", "Sinuhe", "Sinvus", "Sisko", "Sisu", "Skarrakas", "Skaug",
"Skeeth", "Skor", "Skotia", "Skullspitter", "Skyboot", "Slade", "Slaugulond", "Slickbark", "Slimp", "Slone",
"Sloom", "Slyderia", "Smeke", "Snick", "Snugbreeches", "Sohvi", "Soini", "Sokkwi", "Sol", "Solan",
"Solomoriah", "Sothak", "Sparrow", "Spendler", "Spuddle", "Spyrcrist", "Stefan", "Steng", "Stiv", "Stonebrow",
"Stonefist", "Stormraven", "Strall", "Sulumyn", "Suoma", "Suten", "Suvi", "Swiftblade", "Syluz", "Taavetti",
"Taavi", "Tadhg", "Taelin", "Tagledash", "Tahvo", "Taisto", "Talimor", "Tameri", "Tanafriti", "Taneli",
"Tanja", "Tantlinger", "Taralthas", "Taravil", "Targas", "Tarixi", "Tarmo", "Tartaglia", "Tasil", "Tasseldale",
"Tauno", "Teenik", "Tenbar", "Teneyck", "Tennon", "Teodore", "Terger", "Tero", "Terron", "Terrox",
"Teuvo", "Tezzerell", "Thassius", "Thelone", "Thenraine", "Therandili", "Therion", "Thesis", "Thiric", "Thistle",
"Thistletoe", "Thomas", "Thoril", "Thorus", "Thrull", "Thunderhammer", "Thunderhead", "Thundra", "Thye", "Tiankhit",
"Tierney", "Tierza", "Tilbor", "Tinubiti", "Tinythalas", "Titinius", "Toivo", "Toliver", "Tomas", "Tor",
"Torag", "Torlo", "Torsti", "Toupin", "Trenellan", "Tuerezo", "Tular", "Tullamore", "Tuomas", "Tuomo",
"Turgan", "Turgon", "Turlach", "Turlough", "Twight", "Tybrin", "Udjai", "Ultan", "Umlaut", "Unger",
"Unwanted", "Ureel", "Urho", "Urias", "Uriel", "Urndale", "Uro", "Urshe", "Ursula", "Usko",
"Utmebar", "Vaino", "Valmore", "Valterri", "Valto", "Valvinder", "van Veen", "Vanamo", "Vanauken", "Vandel",
"Vandenbossette", "Vanguard", "Varl", "Vasha", "Vaught", "Vectrasik", "Veepo", "Vega", "Veikko", "Velox",
"Venieal", "Verseth", "Vesu", "Victran", "Vidor", "Vilden", "Vilhelmi", "Vilho", "Vilmar", "Vin",
"Voitto", "Vorbutin", "Vortiel", "Voxvax", "Vuokko", "Wakhakwi", "Wakhashem", "Wanderer", "Wat", "Wati",
"Wayland", "Wedfellow", "Weemhoff", "Wendel", "Westra", "Whilehead", "Whingle", "Wiles", "Willow", "Willum",
"Wimbly", "Wixem", "Wofare", "Wolfmoon", "Wolfram", "Wolvenmore", "Woodrider", "Woodrow", "Woserit", "Wrine",
"Wyllymyr", "Wynnich", "Yar", "Yato", "Yazzi", "Ynywyth", "Yrjana", "Yrjo", "Ysbrand", "Yuiel",
"Zaagan", "Zarine", "Zatelli", "Zeuth", "Zilas", "Zinnebor", "Zook", "Zorill", "Zyggy" )


hitdice = (
    ( 6, 1 ),
    ( 8, 2 ),
    ( 4, 1 ),
    ( 4, 2 ),
)

statbonuses = (
    0, 0, 0,
    -3,
    -2, -2,
    -1, -1, -1,
    0, 0, 0, 0,
    1, 1, 1,
    2, 2,
    3
)

meleeweapons = [
    [ 0,
        [ 3, "warhammer", 1, "1d6" ],
        [ 8, "mace", 1, "1d8" ],
        [ 1, "maul", 2, "1d10" ]
    ],
    [ 0,
        [ 2, "great axe", 2, "1d10" ],
        [ 7, "battle axe", 1, "1d8" ],
        [ 6, "shortsword", 1, "1d6" ],
        [ 14, "longsword", 1, "1d8" ],
        [ 2, "scimitar", 1, "1d8" ],
        [ 2, "two-handed sword", 2, "1d10" ],
        [ 1, "pole arm", 2, "1d10" ],
        [ 2, "spear", 2, "1d6" ]
    ],
    [ 0,
        [ 1, "dagger", 1, "1d4" ],
        [ 1, "walking staff", 2, "1d4" ]
    ],
    [ 0,
        [ 7, "battle axe", 1, "1d8" ],
        [ 6, "shortsword", 1, "1d6" ],
        [ 14, "longsword", 1, "1d8" ],
        [ 2, "scimitar", 1, "1d8" ]
    ]
]

meleeweaponbonus = [
    0,
    [ 40, "+1" ],
    [ 10, "+2" ],
    [  5, "+3" ],
    [  2, "+4" ],
    [  1, "+5" ],
    [ 17, "+1, +2 vs. special enemy" ],
    [ 10, "+1, +3 vs. special enemy" ]
]

armortypes = [
    [ 0,
        [  9, "leather armor", 13, 30 ],
        [ 19, "chain mail", 15, 20 ],
        [ 15, "plate mail", 17, 20 ]
    ],
    [ 0,
        [  9, "leather armor", 13, 30 ],
        [ 19, "chain mail", 15, 20 ],
        [ 15, "plate mail", 17, 20 ]
    ],
    [ 0,
        [  1, "", 11, 40 ]
    ],
    [ 0,
        [  1, "leather armor", 13, 30 ]
    ]
]

defaultarmor = [
    [ "plate mail", 17, 20 ],
    [ "plate mail", 17, 20 ],
    [ "", 11, 40 ],
    [ "leather armor", 13, 30 ]
]

armorbonus = [
    0,
    [ 50, 1 ],
    [ 30, 2 ],
    [ 10, 3 ]
]

ringprobonus = [
    0,
    [ 9, 1 ],
    [ 4, 2 ],
    [ 1, 3 ]
]

potiontable = [
    0,
    [ 3, "clairaudience", -1 ],
    [ 4, "clairvoyance", -1 ],
    [ 3, "animal control", -1 ],
    [ 3, "dragon control", -1 ],
    [ 3, "giant control", -1 ],
    [ 3, "human control", -1 ],
    [ 3, "plant control", -1 ],
    [ 3, "undead control", -1 ],
    [ 3, "diminution", -1 ],
    [ 4, "mind reading", -1 ],
    [ 4, "fire resistance", -1 ],
    [ 4, "flying", -1 ],
    [ 4, "gaseous form", -1 ],
    [ 4, "giant strength", -1 ],
    [ 4, "growth", -1 ],
    [ 4, "healing", -1 ],
    [ 5, "heroism", 1 ],
    [ 4, "invisibility", -1 ],
    [ 4, "invulnerability", -1 ],
    [ 4, "levitation", -1 ],
    [ 4, "longevity", -1 ],
    [ 2, "poison", -1 ],
    [ 3, "polymorph self", -1 ],
    [ 8, "speed", -1 ],
    [ 3, "treasure finding", -1 ],
    [ 7, "delusion", -1 ],
]

scrolltable = [
    [ 0,
        [  3, (0, 1), ],
        [  3, (0, 2), ],
        [  2, (0, 3), ],
        [  1, (0, 4), ],
        [  5, "cursed scroll" ],
        [  6, "scroll of protection from elementals" ],
        [ 10, "scroll of protection from lycanthropes" ],
        [  5, "scroll of protection from magic" ],
        [ 13, "scroll of protection from undead" ],
        [ 10, "map to treasure type A" ],
        [  4, "map to treasure type E" ],
        [  3, "map to treasure type G" ],
        [  8, "map to 1d4 magic items" ]
    ],
    [ 0,
        [  5, "cursed scroll" ],
        [  6, "scroll of protection from elementals" ],
        [ 10, "scroll of protection from lycanthropes" ],
        [  5, "scroll of protection from magic" ],
        [ 13, "scroll of protection from undead" ],
        [ 10, "map to treasure type A" ],
        [  4, "map to treasure type E" ],
        [  3, "map to treasure type G" ],
        [  8, "map to 1d4 magic items" ]
    ],
    [ 0,
        [  6, (2, 1), ],
        [  5, (2, 2), ],
        [  5, (2, 3), ],
        [  4, (2, 4), ],
        [  3, (2, 5), ],
        [  2, (2, 6), ],
        [  1, (2, 7), ],
        [  5, "cursed scroll" ],
        [  6, "scroll of protection from elementals" ],
        [ 10, "scroll of protection from lycanthropes" ],
        [  5, "scroll of protection from magic" ],
        [ 13, "scroll of protection from undead" ],
        [ 10, "map to treasure type A" ],
        [  4, "map to treasure type E" ],
        [  3, "map to treasure type G" ],
        [  8, "map to 1d4 magic items" ]
    ],
    [ 0,
        [  5, "cursed scroll" ],
        [  6, "scroll of protection from elementals" ],
        [ 10, "scroll of protection from lycanthropes" ],
        [  5, "scroll of protection from magic" ],
        [ 13, "scroll of protection from undead" ],
        [ 10, "map to treasure type A" ],
        [  4, "map to treasure type E" ],
        [  3, "map to treasure type G" ],
        [  8, "map to 1d4 magic items" ]
    ]
]

miscmagictable = [
    0,
    [ 4, "amulet of proof against detection and location" ],
    [ 2, "bag of devouring" ],
    [ 6, "bag of holding" ],
    [ 5, "boots of levitation" ],
    [ 5, "boots of speed" ],
    [ 5, "boots of traveling and leaping" ],
    [ 1, "bowl commanding water elementals" ],
    [ 1, "brazier commanding fire elementals" ],
    [ 6, "broom of flying" ],
    [ 1, "censer commanding air elementals" ],
    [ 3, "cloak of displacement" ],
    [ 4, "crystal ball" ],
    [ 2, "crystal ball with clairaudience" ],
    [ 1, "drums of panic" ],
    [ 1, "efreeti bottle" ],
    [ 7, "elven boots" ],
    [ 7, "elven cloak" ],
    [ 2, "flying carpet" ],
    [ 7, "gauntlets of ogre power" ],
    [ 2, "girdle of giant strength" ],
    [ 6, "helm of reading languages and magic" ],
    [ 1, "helm of telepathy" ],
    [ 1, "helm of teleportation" ],
    [ 1, "horn of blasting" ],
    [ 9, "medallion of mind reading" ],
    [ 1, "mirror of life trapping" ],
    [ 5, "rope of climbing" ],
    [ 3, "scarab of protection" ],
    [ 1, "stone commanding earth elementals" ]
]


# *******************************************************************************************************
# Convenience Functions

def statstring(stats, abbrev = 0):
    rc = []
    for i in range(6):
        sb = statbonuses[stats[i]]
        if not abbrev or sb != 0:
            rc.append(statnames[i][0])
            rc.append(str(stats[i]))
            if sb > 0:
                rc.append("(+%d)" % sb)
            elif sb < 0:
                rc.append("(%d)" % sb)
    return " ".join(rc)


# *******************************************************************************************************
# Object Constructors

class Character:

    def __init__(self, level, clas, actuallevel = 0, outfit = 1):

        self.category = "character"

        if Dice.D(1, 100) <= 25: # 2 names
            self.name = "%s %s" % (random.choice(names), random.choice(names))
        else: # 1 name
            self.name = random.choice(names)
        self.noapp = 1

        self.clas = clas
        self.classname = classnames[self.clas]

        self.hitpoints = [ ]

        self.spells = None

        self.level = level
        if not actuallevel:
            if Dice.D(1, 100) <= 30:
                self.level = max(Dice.D(1, self.level), Dice.D(1, self.level))
            self.level = levels[self.level][clas]

        self.specialbonus = 0
        if self.clas in (0, 2) and self.level >= 5:
            self.specialbonus = 1

        self.xp = Tables.xpcalc("%d%s" % (self.level, "***"[:self.specialbonus]))

        self.attackbonus = Tables.characterab[self.level][self.clas]

        self.stats = [
            Dice.D(3, 6), Dice.D(3, 6), Dice.D(3, 6),
            Dice.D(3, 6), Dice.D(3, 6), Dice.D(3, 6)
        ]

        # boost prime if it's not good.
        self.stats[primes[clas]] = max(self.stats[primes[clas]], Dice.D(3, 6), 9)
        # boost constitution if it's not good.
        self.stats[4] = max(self.stats[4], Dice.D(3, 6))

        self.race = "Human"

        if Dice.D(1, 100) <= 25:
            # this character will be a demi-human if the stats allow
            eligible = []
            if self.stats[4] >= 9:
                if self.clas != 2:
                    eligible.append("Dwarf")
            if self.stats[1] >= 9:
                eligible.append("Elf")
            if self.stats[3] >= 9:
                if self.clas != 2:
                    eligible.append("Halfling")
            if eligible:
                race = random.choice(eligible)
                if race == "Dwarf":
                    if self.stats[5] > 17:
                        self.stats[5] = 17
                if race == "Elf":
                    if self.stats[4] > 17:
                        self.stats[4] = 17
                if race == "Halfling":
                    if self.stats[0] > 17:
                        self.stats[0] = 17
                self.race = race

        self.movement = 40
        self.morale = 9

        self.armor = ""
        self.armorvalue = 0
        self.meleeweapon = "pointy stick"
        self.damage = "1d6"

        self.shield = ""
        self.shieldvalue = 0
        self.ringpro = 0
        self.potion = ""
        self.scroll = ""

        self.rollhp()

        if outfit:
            self.outfit()
        self.calc()

    def rollhp(self):
        self.hitpoints = []
        for j in range(self.noapp):
            hp = 0
            for i in range(min(self.level, 9)):
                roll = Dice.D(1, hitdice[self.clas][0]) + statbonuses[self.stats[4]]
                hp = hp + max(roll, 1)
            if self.level > 9:
                hp = hp + (hitdice[self.clas][1] * (self.level - 9))
            self.hitpoints.append(hp)

    def calc(self):
        self.armorclass = self.armorvalue + self.shieldvalue + statbonuses[self.stats[3]] + self.ringpro

    # generate items for an adventurer NPC
    def outfit(self):

        a = genarmor(self.clas, self.level)
        self.armor = a[0]
        self.armorvalue = a[1]
        self.movement = a[2]

        m = genmeleeweapon(self.clas, self.level)
        self.meleeweapon = m[0]
        self.damage = m[2]

        if m[1] < 2:
            s = genshield(self.clas, self.level)
            self.shield = s[1]
            self.shieldvalue = s[2]

        if self.clas == 2:
            if Dice.D(1, 100) < min(95, self.level * 4):
                self.ringpro = Dice.tableroller(ringprobonus)[1]

        self.potion = genpotion(self.clas, self.level)
        self.scroll = genscroll(self.clas, self.level)

        if self.clas == 0 or self.clas == 2: # generate spells
            self.spells = Spells.genspells(self.clas, self.level)

        self.calc()

    def to_odt(self):

        odt = []

        rcl = "%s %s %d" % (self.race, self.classname, self.level)
        if self.name:
            mblock = [ "%s, %s:" % (ODT.bold(self.name), rcl) ]
        else:
            mblock = [ ODT.bold("%s %s:") % (self.noapp, rcl) ]

        xpea = ''
        if self.noapp > 1:
            xpea = ' ea.'

        mblock.append(ODT.nonbreak("AC %d," % self.armorclass))
        mblock.append(ODT.nonbreak("AB +%d," % self.attackbonus))
        mblock.append("%s%s," % (ODT.nonbreak("#At 1 "), Formatter.fixbold(self.meleeweapon.lower())))
        mblock.append(ODT.nonbreak("Dam %s," % self.damage))
        mblock.append(ODT.nonbreak("Mv %d'," % self.movement))
        mblock.append(ODT.nonbreak("ML %d," % self.morale))
        mblock.append(ODT.nonbreak("XP %d%s" % (self.xp, xpea)))

        odt.append(ODT.monsterblock(" ".join(mblock)))

        ss = statstring(self.stats, 1).strip()
        if ss:
            odt.append(ODT.monsterblock(ss))

        if self.spells is not None:
            spells = map(lambda s: ODT.bold(s.lower()), self.spells)
            odt.append(ODT.monsterblock("Spells: %s" % ", ".join(spells)))

        items = []
        if self.armor:
            if "+" in self.armor:
                items.append(ODT.bold(self.armor.lower()))
            else:
                items.append(self.armor.lower())
        if self.shield:
            if "+" in self.shield:
                items.append(ODT.bold(self.shield.lower()))
            else:
                items.append(self.shield.lower())
        if "+" in self.meleeweapon:
            items.append(ODT.bold(self.meleeweapon.lower()))
        else:
            items.append(self.meleeweapon.lower())
        if self.ringpro > 0:
            items.append(ODT.bold("ring of protection +%d" % self.ringpro))
        if self.potion:
            items.append(ODT.bold("potion of %s" % self.potion))
        if self.scroll:
            if "scroll" in self.scroll:
                items.append(ODT.bold(self.scroll))
            else:
                items.append(self.scroll)
        if items:
            odt.append(ODT.monsterblock("Equipment: %s" % (", ".join(items))))

        hplist = Formatter.hpblocks(self.hitpoints)

        for i in range(len(hplist)-1):
            odt.append(ODT.hpcheckboxes(ODT.tab.join(hplist[i].split('\t'))))
        if hplist:
            odt.append(ODT.hpchecksend(ODT.tab.join(hplist[-1].split('\t'))))

        return "".join(odt)

    def to_html(self):

        res = [ "<p>" ]

        rcl = "%s %s %d" % (self.race, self.classname, self.level)
        if self.name:
            res.append("<b>%s</b>, %s:" % (self.name, rcl))
        else:
            res.append("<b>%d %s:</b>" % (self.noapp, rcl))
        xpea = ''
        if self.noapp > 1:
            xpea = ' ea.'
        res.append("AC %d, AB +%d, #At 1 %s, Dam %s, Mv %d', ML %d, XP %d%s"
            % (self.armorclass, self.attackbonus, self.meleeweapon.lower(),
               self.damage, self.movement, self.morale, self.xp, xpea)
        )
        ss = statstring(self.stats, 1).strip()
        if ss:
            res.append("<p>%s" % ss)
        if self.spells is not None:
            res.append("<p>Spells:")
            res.append("<b>%s</b>" % (", ".join(map(lambda s: s.lower(), self.spells))))
        items = []
        if self.armor:
            items.append(self.armor)
        if self.shield:
            items.append(self.shield)
        items.append(self.meleeweapon)
        if self.ringpro > 0:
            items.append("<b>ring of protection +%d</b>" % self.ringpro)
        if self.potion:
            items.append("<b>potion of %s</b>" % self.potion)
        if self.scroll:
            if "scroll" in self.scroll:
                items.append("<b>%s</b>" % self.scroll)
            else:
                items.append(self.scroll)
        if items:
            res.append("<p>Equipment:")
        res.append(", ".join(items))

        res.append(htmlhitpointblock(self.hitpoints))

        return "\n".join(res)


def genmeleeweapon(cclass, level):

    # choose a weapon type
    wpn = Dice.tableroller(meleeweapons[cclass])

    # is it magical?
    chance = 5
    if cclass == 2:
        chance = 3
    bonus = ""
    damage = wpn[3]
    if Dice.D(1, 100) < min(95, level * chance):
        row = Dice.tableroller(meleeweaponbonus)
        bonus = row[1]
        damage = damage + bonus

    if bonus:
        return [ "<b>%s %s</b>" % (wpn[1], bonus), wpn[2], damage ]
    else:
        return [ wpn[1] + bonus, wpn[2], damage ]


def genpotion(cclass, level):
    rc = [ 0, "", 0 ]
    if Dice.D(1, 100) < (level * 2):
        rc = Dice.tableroller(potiontable)
        while rc[2] != -1 and rc[2] != cclass:
            rc = Dice.tableroller(potiontable)
        if rc[1] == "Delusion":
            rc2 = Dice.tableroller(potiontable)
            rc = [ rc[0], "Delusion (%s)" % rc2[1], rc[2] ]
    return rc[1]


def genscroll(cclass, level):
    if Dice.D(1, 100) < (level * 3):
        scroll = Dice.tableroller(scrolltable[cclass])[1]
        if type(scroll) is tuple:
            scrollspells = Spells.genscroll(scroll[0], scroll[1])
            scroll = "scroll of %s spells: %s" \
                   % (classnames[cclass].lower(), ", ".join(scrollspells))
        return scroll
    return ""


def genarmor(cclass, level):

    if cclass == 2:
        return defaultarmor[cclass]

    # is it magical?  (overrides armor type choice)
    chance = 5
    if cclass == 2:
        chance = 4
    if Dice.D(1, 100) < min(95, level * chance):
        typ = Dice.tableroller(armortypes[cclass])
        row = Dice.tableroller(armorbonus)
        return [ "<b>%s +%d</b>" % (typ[1], row[1]), typ[2] + row[1], min(typ[3] + 10, 40) ]

    return defaultarmor[cclass]


def genshield(cclass, level):

    if cclass > 1:
        return [ 0, "", 0 ]

    arm = [ 0, "shield", 1 ]

    # is it magical?
    if Dice.D(1, 100) < min(95, level * 5):
        row = Dice.tableroller(armorbonus)
        arm[1] = "<b>%s +%d</b>" % (arm[1], row[1])
        arm[2] = arm[2] + row[1]

    return arm


# factory function to create an entire adventurer party according to the
# standard rules.

def generate(level):

    ftrs = Dice.D(1, 3)
    thfs = Dice.D(1, 2)
    clrs = Dice.D(1, 2)
    mus = Dice.D(1, 2) - 1

    party = []
    totlvl = 0

    for i in range(clrs):
        character = Character(level, 0)
        totlvl += character.level
        party.append(character)

    for i in range(ftrs):
        character = Character(level, 1)
        totlvl += character.level
        party.append(character)

    for i in range(mus):
        character = Character(level, 2)
        totlvl += character.level
        party.append(character)

    for i in range(thfs):
        character = Character(level, 3)
        totlvl += character.level
        party.append(character)

    return party


def htmlhitpointblock(hplst):

    if type(hplst) is int:
        hplst = [ hplst ]

    rc = [ ]

    for hp in hplst:

        hprows = []

        # hit point boxes
        n = hp // 5
        r = hp % 5

        hprow = []
        while n:
            hprow.append("&#9744;" * 5)
            n -= 1
            if len(hprow) > 3:
                hprows.append(" ".join(hprow))
                hprow = []
        if r:
            hprow.append("&#9744;" * r)

        if hprow:
            hprows.append(" ".join(hprow))

        if hprows:
            hprows[0] = "".join([
                "<tr><td style='width: 2em;'>HP</td>",
                "<td style='width: 3em; text-align: right; padding-right: 1em;'>%d</td>" % hp,
                "<td>%s</td></tr>" % hprows[0],
            ])
            for i in range(1, len(hprows)):
                hprows[i] = "<tr><td></td><td></td><td>%s</td></tr>" % hprows[i]
            hprows = [ "<table>\n%s\n</table>" % "\n".join(hprows) ]

        rc.append("\n".join(hprows))

    return "\n".join(rc)


# end of file.
