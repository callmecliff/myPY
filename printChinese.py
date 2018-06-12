import urlparse

unicodeStr = '\u5F88\u660E\u663E\u771F\u6B63\u7684\u97E9\u4FE1\u90FD\u52A8\u8111\u7684\uFF01\u8FD9\u91CC\u7684\u97E9\u4FE1\u5C31\u662F\u4E00\u4E2A\u5F20\u98DE\uFF01\u4E5F\u96BE\u602A\u540D\u5B57\u53EB\u5929\u610F\uFF01\u4E5F\u5C31\u662F\u8BF4\u8FD9\u91CC\u7684\u97E9\u4FE1\u5168\u7279\u4E48\u9760\u8FD0\u6C14\u6D3B\u5230\u6700\u540E\u4E00\u96C6\u7684\u662F\u5427\uFF1F'
###unicodeStr = '\u5F8';

print(unicodeStr.decode("unicode_escape").encode("UTF-8"))

urlStr = 'http://p.comments.youku.com/ycp/comment/pc/commentList?jsoncallback=n_commentList&app=100-DDwODVkv&objectId=894713139&objectType=1&listType=0&currentPage=1&pageSize=30&sign=8f3cfc76e2e93de150a0998684abc2df&time=1528124089'
###https://p.comments.youku.com/ycp/comment/pc/commentList?jsoncallback=n_commentList&app=100-DDwODVkv&objectId=895731766&objectType=1&listType=0&currentPage=1&pageSize=30&sign=9a888691cfd1839a3944722fd978af2f&time=1528810781
print(urlparse.unquote(urlStr))
