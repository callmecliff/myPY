# -*- coding:utf-8 -*-

import requests as req
import json
import re

org_url = 'https://p.comments.youku.com/ycp/comment/pc/commentList?jsoncallback=n_commentList&app=100-DDwODVkv&objectId=895731766&objectType=1&listType=0&currentPage=1&pageSize=30&sign=9a888691cfd1839a3944722fd978af2f&time=1528810781'
resp = req.get(org_url)
res = re.findall('n_commentList\((.*?)\)',resp.content.decode(),re.S)

###res = json.loads(re.findall('n_commentList\((.*?)\)',resp.content,re.S))###

print resp.content
print res[0]
res_dict = json.loads(res[0])

print res_dict['code']
