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


content_body = None


def document(s):
    global content_body
    if content_body is None:
        fp = open("content.static")
        content_body = fp.read()
        fp.close()
    return s.join(content_body.split("@text@"))


def boxedtext(s):
    return '''<text:p text:style-name="BoxedText">%s</text:p>''' % s


def columns(s):
    return '''<text:section text:style-name="Sect1" text:name="Section1">%s</text:section>''' % s


def hpcheckboxes(s):
    return '''<text:p text:style-name="HPCheckBoxes">%s</text:p>''' % s


def hpchecksend(s):
    return '''<text:p text:style-name="HPChecksEnd">%s</text:p>''' % s


def mapkeyheading(s):
    return '''<text:h text:style-name="MapKeyHeading" text:outline-level="3">%s</text:h>''' % s


def monsterblock(s):
    return '''<text:p text:style-name="MonsterBlock">%s</text:p>''' % s


def subheading(s):
    return '''<text:h text:style-name="SubHeading" text:outline-level="2">%s</text:h>''' % s


def textbody(s):
    return '''<text:p text:style-name="P21">%s</text:p>''' % s


def wanderingmonsterbody(s):
    return '''<text:p text:style-name="WanderingMonsterBody">%s</text:p>''' % s


def wanderingmonsterend(s):
    return '''<text:p text:style-name="WanderingMonsterEnd">%s</text:p>''' % s


# end of file.
