from w3lib.url import url_query_parameter

res=url_query_parameter("product.html?id=200&foo=bar", "id")
print(res)


from  urllib.parse import urlparse

url = 'http://kuaixun.stcn.com/2017/1220/13847580.shtml'
o = urlparse(url).path.split('.')

print(o[0])

res=urlparse('http://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html').path.split('/')
print(res[-2])

 #
import re
prog = re.compile(r'[\w]+?://([\w\.]+)/')

result = prog.match('http://kuaixun.stcn.com/2017/1221/13849148.shtml')
print(result)