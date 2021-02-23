"""
获取api的json数据
"""
import json
from urllib.request import Request, urlopen

# zb网站获取数据Api
url = "https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN"
# 包装头部
firefox_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
# 构建请求
request = Request(url, headers=firefox_headers)
html = urlopen(request)
# 获取数据
data = html.read()
# 转换成字符串
strs = str(data)
print('strs:', strs)
print(type(strs))
# 转换成JSON
datas = json.dumps(strs[2:-1])
print(datas)
# 转换成字典数据
data_dict = json.loads(datas)
print(data_dict)
print(type(data_dict))  # 应该是dict，可他就变成了str，真是蠢
data_dict=data_dict.replace('true', 'True') # python的真是True，字符串里面有true
print(data_dict)
data_result=eval(data_dict)
print(data_result["images"][0]['url'])

