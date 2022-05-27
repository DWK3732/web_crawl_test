#!/usr/bin/python
#-*- coding: utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup
# from konlpy.tag import Twitter
from konlpy.tag import Kkma

def hfilter(s):
    return re.sub(u'[^ \.\,\?\!\u3130-\u318f\uac00-\ud7a3]+','',s)

if __name__ == '__main__':

    posTagger = Kkma()
    #posTagger = Twitter()
    word_d = {}
    req = requests.get('https://ko.wikipedia.org/')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    my_para = soup.select('body > div')
    for para in my_para:
        hsent = hfilter(para.getText())

        wlist = posTagger.pos(hsent)
        for w in wlist:
            if w[1]=="NNG":
            # if w[1]=="Noun":
                if w[0] not in word_d:
                    word_d[w[0]]=0
                word_d[w[0]] += 1
    for w,c in sorted(word_d.items(), key = lambda x:x[1], reverse=False):
        print(w,c)