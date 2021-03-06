#!/usr/bin/python
#-*- coding: utf-8 -*-

import re
from regex import W
import requests
from bs4 import BeautifulSoup
# txt 
import sys

def process( soup_selction_list ):
    global DATA_dic
    for content in soup_selction_list:
        sentence = re.findall(r"(?i)\b[a-z]+\b", content.get_text())
        # sentence = list(content.get_text().split())
        for word in sentence:
            if DATA_dic.get(word)==None:
                DATA_dic[word] = 1
            else :
                DATA_dic[word] += 1


if __name__ == '__main__':
    url = u'https://en.wikipedia.org/wiki/Web_crawler'
    res = requests.get(url)

    # printing in txt file
    out = open('output.txt','w')
    out2 = open('output2.txt','w')
    out3 = open("output3.txt",'w')
    #print(res.content,file=out)

    # implement BeautifulSoup
    soup = BeautifulSoup(res.content,"html.parser")

    # DATA_dic as dictionary of { "word" : frequency }
    global DATA_dic
    DATA_dic = {}
    
    # check for each types
    title = soup.select('h1#firstHeading')
    sub_t = soup.select('div#siteSub')
    p_in_soup = soup.select('div.mw-parser-output > p')
    note_in_soup = soup.select('div.mw-parser-output > div.hatnote')
    h1_in_soup = soup.select('div.mw-parser-output h1')
    h2_in_soup = soup.select('div.mw-parser-output h2')
    h3_in_soup = soup.select('div.mw-parser-output h3')
    h4_in_soup = soup.select('div.mw-parser-output h4')
    h5_in_soup = soup.select('div.mw-parser-output h5')
    h6_in_soup = soup.select('div.mw-parser-output h6')
    list_in_soup = soup.select('div.mw-parser-output > ul > li')
    content = ( title, sub_t, p_in_soup, note_in_soup, h1_in_soup, h2_in_soup, h3_in_soup, h4_in_soup, h5_in_soup, h6_in_soup, list_in_soup )
    # get words and frequencies
    for lists in content:
        process(lists)
    words = list(DATA_dic.keys())
    frequencies = list(DATA_dic.values())
    
    for i in range(len(words)):
        print("{} {}".format(words[i],frequencies[i]),file=out)
    #for tp in h5_in_soup:
    #    print(tp.get_text().split(),file=out)
    print(soup.prettify(),file=out2)
    print("{}\n{}".format(soup.find_all("h1"),soup.find_all("div",role="note")),file=out3)

    '''
    <?????? ????????? ????????? DB??? ??????>

- ??????????????? ?????? ???????????? ????????? DB??? ???????????? python code ??????
  . ????????????(??????) : https://en.wikipedia.org/wiki/Web_crawler
  . wikipedia ?????? ?????? 

    1. ??? ??????????????? ???????????? ?????? ??????
  . ?????? ?????? <p> ??? </p> ?????? ??????
  . ?????? html tag?????? ???????????? beautifulsoup??? ???????????? ?????? ??????
2. ???????????? ????????? ??????
  . ????????? ????????? split()????????? ???????????? ?????????
  . space??? tab??? ????????? ????????? ???????????? ????????? ??????
  . ?????? ?????? (?????????, ?????? ???)??? ??????
  . ????????? ???????????? ????????? dictionary ??????
3. ????????? ????????? DB ??? ??????
  . ?????????DB(RDB) / NoSQL ??? ???????????? ??????
  . index name : web
  . type: words
  . ????????? ????????? (NoSQL - JSON document format with the following fields / RDB: ORM or your own table creation with relevant index and reasoning)
    - url : ???????????? ??????
    - words: ["the", "have", "has", "is" ??? ]
    - frequencies: [ 2341, 234, 56, 878, ??? ]
    * words???????????? frequencies???????????? ????????? ??????????????? ???
    * frequencies??? ??? ????????? ?????? ??????????????? ???????????? ???????????? ?????????
    '''