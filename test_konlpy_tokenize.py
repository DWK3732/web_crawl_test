#!/usr/bin/python
#-*- coding: utf-8 -*-

from konlpy.tag import Kkma
from konlpy.utils import pprint

if __name__ == '__main__':
    mystring = u'오늘은 날씨가 좋습니다. 내일은 눈이 온다고 합니다. 모레는 오늘보다 춥습니다.'
    kkma = Kkma()
    print(kkma.sentences(mystring))