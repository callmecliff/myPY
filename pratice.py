# -*- coding:utf-8 -*-
import math,sys
import re
import requests as req


old_url = 'http://www.jikexueyuan.com/course/android/?pageNum=2'

total_page = 20

'''for i in range(2,total_page+1):
    new_link = re.sub('pageNum=\d+','pageNum=%d'%i,old_url,re.S)
    print new_link'''

f = open('source.txt','r')
html = f.read()
f.close()

info = re.findall(('<div class="lessonimg-box">.*?<a href=.*?<img src="(.*?)" class="lessonimg".*?</a>.*?'
                   '<div class="lesson-infor".*?<h2 class="lesson-info-h2"><a.*?>(.*?)</a></h2>'),html,re.S)

#str(s[0]).decode(‘string_escape‘)
'''for each in info:
    print str(each[1]).decode('string_escape') + each[0]'''

for each in info:
    print 'now loading' + each[1]
    pic = req.get(each[0])
    fp = open(unicode('material\\pic\\' + each[1] + '.jpg','utf-8'),'wb')
    fp.write(pic.content)
    fp.close()
