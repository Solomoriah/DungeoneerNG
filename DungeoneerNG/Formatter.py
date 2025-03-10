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

    def __init__(self, text, style = "Text Body"):
        self.category = "paragraph"
        self.text = text
        self.style = style

    def to_odt(self):
        return ODT.genericparagraph(fixbold(self.text), self.style)

    def to_html(self):
        return "<p>\n%s" % self.text


# end of file.
