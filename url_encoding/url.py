#!/usr/bin/python
# -*- coding: utf-8 -*-

import alfred
import urllib

(cmd, rawstring) = alfred.args()

if cmd == 'en':
    handled = urllib.quote(rawstring)
elif cmd == 'de':
    handled = urllib.unquote(rawstring)
else:
    handled = rawstring

results = [alfred.Item(
    attributes= {'uid': alfred.uid(0), 'arg': handled},
    title=handled,
    subtitle=u'Enter to copy to clipboard'
)]
xml = alfred.xml(results)
alfred.write(xml)
