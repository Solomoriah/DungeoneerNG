#!/usr/bin/python3

# Basic Fantasy RPG Dungeoneer Next Generation Suite
# Copyright 2007-2012, 2024-2025 Chris Gonnerman
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

    from DungeoneerNG import Adventurer, ODT

    form = cgi.FieldStorage()

    try:
        level = int(form.getfirst("level", "1"))
    except:
        level = 1

    level = min(10, max(1, level))

    party = Adventurer.generate(level)

    odt = []
    for chr in party:
        odt.append(chr.to_odt())
    odt = "".join(odt)

    fn = ODT.saveodt(odt, stem = "adv",
        savedir = "DNGdata",
        defcontent = "DungeoneerNG/content.static",
        base = "DungeoneerNG/base.odt")

    sys.stdout.write("Content-type: text/html\n\n")

    myid = "div%f" % time.time()
    print("<div class=npcblock id='%s'>" % myid)
    print("<div style='float: right;'>")
    print("""<button class=redbutton onclick='$("%s").remove();'>X</button>""" % myid)
    print("</div>")
    for chr in party:
        sys.stdout.write(chr.to_html())
    print("<p><a href='%s'>Download</a>" % fn)
    print("</div>")

except:
    sys.stdout.write("Content-type: text/plain\n\n")
    sys.stdout.write("<pre>\n")
    traceback.print_exc(file = sys.stdout)
    sys.stdout.write("</pre>\n")


# end of file.
