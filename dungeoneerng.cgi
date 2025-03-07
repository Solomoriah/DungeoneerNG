#!/usr/bin/python3

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


import os, sys, cgi

sys.stderr = sys.stdout
sys.stdout.write("Content-type: text/plain\n")

sys.path.append(".")
from DungeoneerNG import Stocker, ODT

sys.stderr = sys.stdout

def safeint(s, b):
    try:
        return int(s)
    except:
        return b

try:
    # generate the dungeon

    form = cgi.FieldStorage()

    level = safeint(form.getfirst("level", 1), 1)
    first = safeint(form.getfirst("first", 1), 1)
    rooms = safeint(form.getfirst("rooms", 1), 1)

    dungeon = Stocker.DungeonFactory(level, rooms, first)

    odt = "".join(map(lambda o: o.to_odt(), dungeon))

    fn = ODT.saveodt(odt, stem = "dng",
        savedir = "DNGdata",
        defcontent = "DungeoneerNG/content.static",
        base = "DungeoneerNG/base.odt")

    print("Content-type: text/html\n")
    print("\n".join(map(lambda o: o.to_html(), dungeon)))
    
except:

    import traceback

    print("Content-type: text/plain\n")

    print("<pre>")
    traceback.print_exc(file=sys.stdout)
    print("</pre>")
    

# end of file.
