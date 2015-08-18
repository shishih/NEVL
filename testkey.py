# -*- coding: utf-8 -*-

import json
import re
import sys,os, urllib, urllib2, time, random, cookielib
from bs4 import BeautifulSoup
from collections import OrderedDict
import string, time, random

def main():
    dic={'a':3,'b':1,'c':2}
    dict= sorted(dic.iteritems(), key=lambda d:d[1], reverse = True)
    print len(dict)
    print dict[1].key

if __name__ == '__main__':
    main()