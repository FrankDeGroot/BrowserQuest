#!/usr/bin/env python
import json

from lxml import etree

def process(el, tagname):
    attrs = dict(el.attrib)
    for a in attrs.keys():
        if attrs[a].isdigit():
            attrs[a] = int(attrs[a])
    children = el.getchildren()
    if len(children) > 1:
        sibs = {}
        for c in children:
            if c.tag not in sibs:
                sibs[c.tag] = []
            sibs[c.tag].append(process(c, False))
        for k in sibs.keys():
            attrs.update({k: sibs[k]})
    else:
        for c in children:
            attrs.update(process(c, True))
    if tagname:
        return {el.tag: attrs}
    else:
        return attrs

def convertTmx2Json(srcFile, destFile):
    tmx = open(srcFile)
    dest = open(destFile, 'w')
    res = {}
    root = etree.parse(tmx).getroot()
    el = root
    res = process(el, True)
    dest.write(json.dumps(res))
    tmx.close()
    dest.close()
    print "Finished converting TMX to JSON."
