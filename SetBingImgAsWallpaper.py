"""
抓取必应每日图片设为桌面
"""
import os
import urllib.request
import ctypes
import requests


def save_img(url, dir):
    try:
        if not os.path.exists(dir):
            print('Dir ', dir, ' is not exist,rebuilding.')
            os.mkdir(dir)
        basename = "bingImg"
        filepath = os.path.join(dir, basename)
        urllib.request.urlretrieve(url, filepath)
        return filepath
    except IOError as e:
        print('IO exception：', e)
    except Exception as e:
        print('Exception: ', e)


def get_url(image_api_url="https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN"):
    import json
    from urllib.request import Request, urlopen

    # zb网站获取数据Api
    # url = "https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN"
    # 包装头部
    firefox_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    # 构建请求
    request = Request(image_api_url, headers=firefox_headers)
    html = urlopen(request)
    # 获取数据
    data = html.read()
    # 转换成字符串
    strs = str(data)
    # 转换成JSON
    datas = json.dumps(strs[2:-1])
    # 转换成字典数据
    data_dict = json.loads(datas)
    # print(type(data_dict))  # 应该是dict，可他就变成了str，真是蠢
    data_dict = data_dict.replace('true', 'True')  # python的真是True，字符串里面有true
    data_result = eval(data_dict)
    result = "https://cn.bing.com" + data_result["images"][0]['url']
    return result


def set_img_asWallPaper(filepath):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, filepath, 0)


if __name__ == '__main__':
    dirname = "F:\\BingAsWallpaper"
    img_url = get_url()
    filepath = save_img(img_url, dirname)
    set_img_asWallPaper(filepath)
