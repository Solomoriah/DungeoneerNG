# ODT Generator for Basic Fantasy Dungeoneer Suite
# Copyright 2025 Chris Gonnerman
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


from . import ODT, Adventurer


__checkbox = "&#9744;"
__hpblock = __checkbox * 5


def checkline(n):
    blks = n // 5
    remn = n % 5
    return " ".join(([ __hpblock ] * blks) + [ __checkbox * remn ])


# expects a list of hitpoints values
# returns a list of lines

def hpblocks(hitpoints):
    hponce = "HP"
    hplist = []
    for hp in hitpoints:
        n = min(20, hp)
        rhp = hp - n
        hplist.append("%s\t%d\t%s" % (hponce, hp, checkline(n)))
        hponce = ""
        while rhp:
            n = min(20, rhp)
            rhp -= n
            hplist.append("\t\t%s" % (checkline(n)))
    return hplist


def fixbold(s):
    if not s.startswith('<b'):
        return s
    s = s.split('>')[1].split('<')[0]
    return ODT.bold(ODT.nonbreak(s))


class Paragraph:

    def __init__(self, text, style = "Text_20_body"):
        self.category = "paragraph"
        self.text = text
        self.style = style

    def to_odt(self):
        return ODT.genericparagraph(fixbold(self.text), self.style)

    def to_html(self):
        style = "".join(self.style.split()).lower()
        return "<p class=%s>\n%s" % (style, self.text)


class TwoColStart:
    def to_odt(self):
        return ODT.twocolumnstart()
    def to_html(self):
        return ''


class TwoColEnd:
    def to_odt(self):
        return ODT.twocolumnend()
    def to_html(self):
        return ''


def htmlhitpointblock(hplst):

    if type(hplst) is int:
        hplst = [ hplst ]

    rc = [ ]

    hponce = "HP"

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
                "<tr><td style='width: 2em;'>%s</td>" % hponce,
                "<td style='width: 3em; text-align: right; padding-right: 1em;'>%d</td>" % hp,
                "<td>%s</td></tr>" % hprows[0],
            ])
            for i in range(1, len(hprows)):
                hprows[i] = "<tr><td></td><td></td><td>%s</td></tr>" % hprows[i]
            hprows = [ "<table>\n%s\n</table>" % "\n".join(hprows) ]
            hponce = ""

        rc.append("\n".join(hprows))

    return "\n".join(rc)


# end of file.
