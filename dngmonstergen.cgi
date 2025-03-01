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


import cgi, time, traceback, sys, json, zipfile, io

__checkbox = "&#9744;"
__hpblock = __checkbox * 5


def checkline(n):
    blks = n // 5
    remn = n % 5
    return " ".join(([ __hpblock ] * blks) + [ __checkbox * remn ])


try:
    sys.path.append(".")
    from DungeoneerNG import Monsters
    from ODTGenerator import content
    fp = open("ODTGenerator/content.static")
    content.content_body = fp.read()
    fp.close()

    form = cgi.FieldStorage()
    mode = form.getfirst("mode", "")
    monster = form.getfirst("monster", "")
    try:
        m = Monsters.Monster(monster, mode)
    except:
        print("Content-type: text/html\n")
        print("Error: Monster generation failed.")
        sys.exit(0)

    odt = []
    rc = []
    mblock = []
    if m.noapp > 1:
        rc.append("<p><b>%s %s:</b> " % (m.noapp, m.names))
        mblock.append(content.bold("%s %s:") % (m.noapp, m.names))
    else:
        rc.append("<p><b>%s:</b> " % m.name)
        mblock.append(content.bold(m.name))

    rc.append("AC %s, HD %s, #At %s, Dam %s, Mv %s,"
        % (m.armorclass, m.hitdice, m.noattacks, m.damage, m.movement))
    mblock.append("AC %s, HD %s, #At %s, Dam %s, Mv %s,"
        % (m.armorclass, m.hitdice, m.noattacks, m.damage, m.movement))

    rc.append("Sv %s, ML %s, XP %s" % (m.saveas, m.morale, m.xp))
    mblock.append("Sv %s, ML %s, XP %s" % (m.saveas, m.morale, m.xp))

    odt.append(content.monsterblock(" ".join(mblock)))

    rc = [ "".join(rc) ]

    hponce = "HP"
    hpblocks = []
    for hp in m.hitpoints:
        n = min(20, hp)
        rhp = hp - n
        rc.append("%s\t%d\t%s" % (hponce, hp, checkline(n)))
        hpblocks.append("%s%s%d%s%s" % (hponce, content.tab(), hp, content.tab(), checkline(n)))
        hponce = ""
        while rhp:
            n = min(20, rhp)
            rhp -= n
            rc.append("\t\t%s" % checkline(n))
            hpblocks.append("%s%s%s" % (content.tab(), content.tab(), checkline(n)))

    for i in range(len(hpblocks)-1):
        odt.append(content.hpcheckboxes(hpblocks[i]))
    if hpblocks:
        odt.append(content.hpchecksend(hpblocks[-1]))

    fp = open("ODTGenerator/base.odt", "rb")
    memfp = io.BytesIO(fp.read())
    fp.close()
    zipfp = zipfile.ZipFile(memfp, "a")
    zipfp.writestr("content.xml", content.document("\n".join(odt)))
    zipfp.close()

    fn = time.strftime("DNGdata/mgen%Y%m%d%H%M%S.odt")
    fp = open(fn, "wb")
    fp.write(memfp.getvalue())
    fp.close()

    rc.append("<a href='%s'>Download</a>" % fn)

    print("Content-type: application/json\n")
    print(json.dumps({
        "html": "<p>\n".join(rc),
        "odt": fn,
    }))

except:
    print("Content-type: text/plain\n")
    print("<pre>")
    traceback.print_exc(file = sys.stdout)
    print("</pre>")


# end of file.
