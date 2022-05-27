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
    <단어 빈도수 구해서 DB에 저장>

- 웹페이지의 단어 빈도수를 구해서 DB에 저장하는 python code 작성
  . 웹페이지(영문) : https://en.wikipedia.org/wiki/Web_crawler
  . wikipedia 메뉴 제외 

    1. 이 페이지에서 문장들만 우선 추출
  . 예를 들어 <p> … </p> 부분 추출
  . 다른 html tag들도 분석하여 beautifulsoup을 사용하여 문장 추출
2. 단어들의 빈도수 계산
  . 하나의 문장을 split()함수를 사용하여 조각냄
  . space나 tab은 빈도수 계산에 들어가지 않도록 주의
  . 특수 기호 (마침표, 콤마 등)는 제거
  . 단어와 빈도수로 구성된 dictionary 생성
3. 처리한 결과를 DB 에 저장
  . 관계형DB(RDB) / NoSQL 중 자유롭게 선택
  . index name : web
  . type: words
  . 저장될 내용들 (NoSQL - JSON document format with the following fields / RDB: ORM or your own table creation with relevant index and reasoning)
    - url : 웹페이지 주소
    - words: ["the", "have", "has", "is" … ]
    - frequencies: [ 2341, 234, 56, 878, … ]
    * words리스트와 frequencies리스트의 길이는 동일하여야 함
    * frequencies는 각 단어가 몇번 나타났는지 빈도수를 저장하는 리스트
    '''