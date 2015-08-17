# -*- coding: utf-8 -*-

import json
import re
import sys,os, urllib, urllib2, time, random, cookielib
from bs4 import BeautifulSoup



# write movielist to json
def movie2json(movName,movId,movDate):
    data = {
        'movName':movName,
        'movId':movId,
        'movDate':movDate,
    }
    json_str = json.dumps(data)
    return json_str

def get_movList():
    # url='http://www.imdb.com/calendar/?ref_=nv_mv_cal_5'
    # html=urllib2.urlopen(url)
    # data=html.read()
    # with open('html.txt','a') as f:
    #     f.write(data)

    with open('html.txt') as f:
        data=f.read()

    soup=BeautifulSoup(data,'html.parser')
    main=soup.find(id="main")

    for item in main.find_all('h4'):
        print item
        print item.next_sibling()
        

    # with open('data.txt', 'a') as f:
    #     f.write(main.contents)





def main():
    get_movList()

if __name__ == '__main__':
    main()