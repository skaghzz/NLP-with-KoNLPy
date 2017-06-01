#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from collections import Counter
import urllib
import random
import webbrowser
from konlpy.utils import pprint
from konlpy.tag import Komoran
import pytagcloud # requires Korean font support
import sys

if sys.version_info[0] >= 3:
    urlopen = urllib.request.urlopen
else:
    urlopen = urllib.urlopen

r = lambda: random.randint(0,255)
color = lambda: (r(),r(),r())

def getText(text):
    f = open(text)
    return f.read().decode('utf-8')

def get_tags(text, ntags=30):
    h = Komoran()
    nouns = h.nouns(text)
    #pprint(nouns)
    count = Counter(nouns)
    pprint(count.most_common(ntags))
    return (pytagcloud.make_tags(count.most_common(ntags),maxsize=100))

def draw_cloud(tags, filename, fontname='dodamM', size=(800, 600)):
    pytagcloud.create_tag_image(tags, filename, fontname=fontname, size=size, rectangular=False)
    #webbrowser.open(filename)

text = getText('mb.txt')
tags = get_tags(text)
pprint(tags)
draw_cloud(tags, 'wordcloudMB.png')
text = getText('park.txt')
tags = get_tags(text)
pprint(tags)
draw_cloud(tags, 'wordcloudPark.png')
text = getText('mun.txt')
tags = get_tags(text)
#print(tags)
draw_cloud(tags, 'wordcloudMun.png')