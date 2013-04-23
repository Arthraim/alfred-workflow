#!/usr/bin/python
# -*- coding: utf-8 -*-

import alfred
import urllib

(cmd, rawstring) = alfred.args()

if cmd == 'en':
    handled = urllib.quote(rawstring)
    icon = '703B65EB-7EA7-40D9-8860-4BA3D2CF48A9.png'
elif cmd == 'de':
    handled = urllib.unquote(rawstring)
    icon = 'AA6E0037-6E59-499D-ABE1-8C5BC0BC48B4.png'
else:
    handled = rawstring
    icon = 'icon.png'

results = [alfred.Item(
    attributes= {'uid': alfred.uid(0), 'arg': handled},
    title=handled,
    subtitle=u'Enter to copy to clipboard',
    icon=icon
)]
xml = alfred.xml(results)
alfred.write(xml)
