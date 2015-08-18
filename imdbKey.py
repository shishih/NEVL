# -*- coding: utf-8 -*-

import json
import re
import sys,os, urllib, urllib2, time, random, cookielib
from bs4 import BeautifulSoup
import string, time



# write movielist to json
def movie2json(movName,movId,movDate,i):
    data = {
                'movName':movName,
                'movId':movId,
                'movDate':movDate,
            }
    local=time.strftime('%U_%y',time.localtime(time.time()))
    jsonwritefile='file/'+local+'_'+str(i)+'.json'
    with open(jsonwritefile, 'a+') as f:
        json.dump(data, f)
    # json_str = json.dumps(data)
    # return json_str

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

    idList=[]
    movDateList=[]
    cont=[]

    patternh4=re.compile(r'\<h4\>.+?\<\/h4\>')
    patterna=re.compile(r'\<a.+?\<\/a\>')

    length= len(main.contents)
    for i in range(length):
        h4= BeautifulSoup(str(main.contents[i]),'html.parser').find('h4')
        a=BeautifulSoup(str(main.contents[i]),'html.parser').find_all('a')
        if h4:
            print h4.contents
            movDate=h4.contents[0]
            i=0
        if a:
            for item in a:
                movId= item['href']

                if movId in idList:
                    pass
                else:
                    idList.append(movId)
                    i=idList.index(movId)
                    movName= item.contents[0]
                    movie2json(movName,movId,movDate,i)

def main():
    get_movList()

if __name__ == '__main__':
    main()