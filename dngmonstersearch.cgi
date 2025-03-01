#!/usr/bin/python3

# Basic Fantasy RPG DungeoneerNG Suite
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


import cgi, time, traceback, sys

try:
    sys.path.append(".")
    from DungeoneerNG import Monsters
    form = cgi.FieldStorage()
    target = form.getfirst("target", "").lower()
    rc = []
    if target:
        keys = sorted(Monsters.monsters.keys())
        for key in keys:
            if key.lower().startswith(target):
                m = Monsters.monsters[key]
                dngnoapp = [ "one" ]
                if "noapprolldungeon" in m:
                    dngnoapp.append("dungeon")
                if "noapprolllair" in m:
                    dngnoapp.append("lair")
                if "noapprollwild" in m:
                    dngnoapp.append("wild")
                rc.append((key, ",".join(dngnoapp)))
            if len(rc) == 10:
                break
    print("Content-type: text/html\n")
    print("\n".join(map(lambda s: "<option value='%s' data-noapp='%s'>%s</option>" % (s[0], s[1], s[0]), rc)))

except:
    print("Content-type: text/plain\n")
    print("<pre>")
    traceback.print_exc(file = sys.stdout)
    print("</pre>")


# end of file.
