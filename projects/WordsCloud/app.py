import jieba
import stylecloud
import sqlite3
import random
import os
from removebg import RemoveBg


def get_key_words():
    stopWords = [line.strip() for line in open('./config/常见中文停用词表.txt', 'r', encoding='gbk').readlines()]
    stopWords.append(' ')

    dbLink = sqlite3.connect(database=r'C:\DIOSTUDIO\Private\Diostudio\diostudio.sqlite')
    dbCsor = dbLink.cursor()
    keyWordsList = dbCsor.execute(r"SELECT type,key_words FROM articles_list")

    writeFile = open('keywords.txt', 'w', encoding='utf-8')

    for keyWord in keyWordsList:
        for item in keyWord:
            writeFile.writelines(item + '\r')

    writeFile.close()

    dbCsor.close()

    readFile = open(file='keywords.txt', mode='r', encoding='utf-8')
    textBeforeCut = readFile.read().split()

    readFile.close()

    textAfterCut = jieba.lcut(str(textBeforeCut))

    keyWords = [x for x in textAfterCut if len(x) > 1 and x not in stopWords]

    print('关键词获取成功！！！')
    # print(keyWords)

    return ' '.join(keyWords)


def generate_word_cloud(icon_name):
    keyWords = get_key_words()

    stylecloud.gen_stylecloud(text=keyWords,
                              palette='cartocolors.qualitative.Pastel_5',
                              size=768,
                              colors=None,
                              background_color='white',
                              icon_name=icon_name,
                              font_path='simhei.ttf',
                              output_name=r'C:\Users\王志强\Desktop\wordsCloud.png')

    # Image.open('wordsCloud.png')

    print('词云图生成成功！！！')


def remove_image_background():
    api_key = 'PWVXVndaWCdpM7Gb8MNwPgc2'

    rmbg = RemoveBg(api_key=api_key, error_log_file='./logs/error.log')
    rmbg.remove_background_from_img_file(r'C:\Users\王志强\Desktop\wordsCloud.png')
    print('图片去背景成功！！！')

    os.remove(r'C:\Users\王志强\Desktop\wordsCloud.png')
    print('删除原文件成功！！！')
    os.rename(r'C:\Users\王志强\Desktop\wordsCloud.png_no_bg.png', r'C:\Users\王志强\Desktop\wordsCloud.png')
    print('文件重命名成功！！！')


iconName = [
'fas fa-brain',
'fas fa-cloud',
'fas fa-comments',
'fas fa-feather',
'fas fa-filter',
'fas fa-fire',
'fas fa-fish',
'fas fa-flag',
'fas fa-heart',
'fas fa-infinity',
'fas fa-leaf',
'fas fa-lemon',
'fas fa-lightbulb',
'fas fa-magnet',
'fas fa-piggy-bank',
'fas fa-rocket',
'fas fa-star',
'fas fa-video'
]


if __name__ == '__main__':
    i = random.randint(1, 18)

    generate_word_cloud(iconName[i-1])

    remove_image_background()
