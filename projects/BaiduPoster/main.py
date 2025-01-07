import requests
import re
import time


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36,',
    'Host': 'data.zz.baidu.com',
    'Content-Length': '83'
}


def get_links():
    with open('links.txt', 'r') as file:
        links = file.read()

        file.close()

    return links


def post_links():
    links = get_links()
    api = r'http://data.zz.baidu.com/urls?site=https://www.diostudio.cn&token=IXUROgLSmZjHZm6P'

    response = requests.post(url=api, headers=headers, timeout=5, data=links).text

    return response


def print_result():
    result = post_links()

    success_num = re.findall('"success":(.*)}', result).pop()
    remain_num = re.findall('"remain":(.*),"', result).pop()

    with open('result.txt', 'a') as file:
        file.write('{0} 成功推送{1}条，今日剩余{2}条。\n'.format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), success_num, remain_num))

        file.close()

        print('{0} 成功推送{1}条，今日剩余{2}条。\n'.format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), success_num, remain_num))


if __name__ == '__main__':
    print_result()
