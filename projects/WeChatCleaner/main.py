import os


def clear_wechat_files():

    os.system(r'taskkill /f /im WeChat.exe')

    user = os.path.expandvars('$HOMEPATH')

    with open(r'C:' + user + '\\AppData\\Roaming\\Tencent\\WeChat\\All Users\\config\\3ebffe94.ini') as config:
        if config.read() == 'MyDocument:':
            location = r'C:' + user + r'\Documents\WeChat Files'
        else:
            location = config.read() + r'WeChat Files'

    files = os.listdir(location)

    logs = open('logs.txt', 'a', encoding='gbk')

    for item in files:
        if os.path.exists(location + '\\' + item + r'\Msg'):
            os.system('del /f /s /q "%s\\*.*"' % (location + '\\' + item + r'\Msg'))
            logs.write('DELETE\t' + (location + '\\' + item + r'\Msg'))
            logs.write('\n')

        if os.path.exists(location + '\\' + item + r'\FileStorage\Image'):
            os.system('del /f /s /q "%s\\*.*"' % (location + '\\' + item + r'\FileStorage\Image'))
            logs.write('DELETE\t' + (location + '\\' + item + r'\FileStorage\Image'))
            logs.write('\n')

        if os.path.exists(location + '\\' + item + r'\FileStorage\Video'):
            os.system('del /f /s /q "%s\\*.*"' % (location + '\\' + item + r'\FileStorage\Video'))
            logs.write('DELETE\t' + (location + '\\' + item + r'\FileStorage\Video'))
            logs.write('\n')

        if os.path.exists(location + '\\' + item + r'\FileStorage\File'):
            os.system('del /f /s /q "%s\\*.*"' % (location + '\\' + item + r'\FileStorage\File'))
            logs.write('DELETE\t' + (location + '\\' + item + r'\FileStorage\File'))
            logs.write('\n')


def clear_browser():
    pass


if __name__ == '__main__':
    clear_wechat_files()
    pass
