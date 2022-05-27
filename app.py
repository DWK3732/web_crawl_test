#!/usr/bin/python
#-*- coding: utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

url = u'https://ko.wikipedia.org/wiki/웹_크롤러'
res = requests.get(url)

html = BeautifulSoup(res.content,"html.parser")
        
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html", parsed_page=html)