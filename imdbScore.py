# -*- coding: utf-8 -*-

import json
import re
import sys,os, urllib, urllib2, time, random, cookielib
from bs4 import BeautifulSoup
from collections import OrderedDict
import string, time, random

path='F:/Research/Video/Program/NEVL/file/'
movList=[]

# write movielist to json
def json2movie():
    localU=time.strftime('%U',time.localtime(time.time()))
    localy=time.strftime('%y',time.localtime(time.time()))
    
    filelist=os.listdir(path)
    if int(localU) >1:
        jsonread=str(int(localU)-1)+'_'+localy
    else:
        jsonread=str(53)+'_'+str(int(localy)-1)

    for file in filelist:
        if file.find(jsonread)==0:
            jsonreadfile=file
        with open(path+file, 'r') as f:
            jsondata=f.read()
            jsondata=jsondata.strip()
    
            data = json.loads(jsondata)
            movList.append(data)
    return movList

def get_score(movList):
    url='http://www.imdb.com'

    movScore={}

    for mov in movList:
        source_url=url+mov['movId']
        html=urllib2.urlopen(source_url)
        data=html.read()

        soup=BeautifulSoup(data,'html.parser')
        tag=soup.find(class_='titlePageSprite star-box-giga-star')
        if tag:
            score=tag.contents[0]
            print score
            movScore[mov['movName']]=score
        print 'sleep'
        time.sleep(random.uniform(9,30))
        

    return movScore

def get_keyword(movScore):
    keyword=[]
    dict= sorted(movScore.iteritems(), key=lambda d:d[1], reverse = True)

    length=len(dict)
    if length<20:
        num=length/2        
    else:
        num=10

    for i in range(0,num):
        keyword.append(dict[i][0])
    for i in range(length-num,length):
        keyword.append(dict[i][0])

    return keyword


def main():
    movList=json2movie()
    movScore=get_score(movList)
    keyword=get_keyword(movScore)
    print keyword

if __name__ == '__main__':
    main()