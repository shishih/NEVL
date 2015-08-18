# -*- coding: utf-8 -*-

import json
import re
import sys,os, urllib, urllib2, time, random, cookielib
from bs4 import BeautifulSoup
from collections import OrderedDict
import string, time

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
            # print file,jsondata
            data = json.loads(jsondata)
            movList.append(data)
    return movList

def get_score():
    pass
    
    



def main():
    json2movie()

if __name__ == '__main__':
    main()