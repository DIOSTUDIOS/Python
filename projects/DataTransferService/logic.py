import pyodbc
import pymysql
from datetime import datetime


def record(text):
    with open('logs.txt', 'a', encoding='utf-8') as logs:
        logs.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S\t' + text + '\n'))
    pass

def generate_sw_erp_tdjbxx():
    connectionString = (f'DRIVER={{SQL Server}};'
                        f'SERVER=192.168.1.23;'
                        f'DATABASE=cwbase7;'
                        f'UID=lc0079999;'
                        f'PWD=aaaaaa;'
                        f'TrustServerCertificate=yes')

    connect = pyodbc.connect(connectionString)

    if connect:
        print('沈闻ERP 2数据库连接成功')
        record('沈闻ERP 2数据库连接成功')

        cursor = connect.cursor()
        cursor.execute(r"SELECT count(*) FROM sysobjects WHERE name='JYBB_FX_2023_B10_TDJBXX'")
        isExistTable = cursor.fetchone()

        if isExistTable[0] == 1:
            print('数据表 JYBB_FX_2023_B10_TDJBXX 存在')
            record('数据表 JYBB_FX_2023_B10_TDJBXX 存在')

            cursor.execute(r'DROP TABLE JYBB_FX_2023_B10_TDJBXX')
            print('数据表 JYBB_FX_2023_B10_TDJBXX 删除成功')
            record('数据表 JYBB_FX_2023_B10_TDJBXX 删除成功')

            print('数据表 JYBB_FX_2023_B10_TDJBXX 数据转存中...')
            cursor.execute(r'SELECT * INTO JYBB_FX_2023_B10_TDJBXX FROM VIEW_JYBB_FX_2023_B10_TDJBXX')
            print('数据表 JYBB_FX_2023_B10_TDJBXX 数据转存完成')
            record('数据表 JYBB_FX_2023_B10_TDJBXX 数据转存完成')

            cursor.commit()
            cursor.close()
            connect.close()
        else:
            print('数据表 JYBB_FX_2023_B10_TDJBXX 不存在')
            record('数据表 JYBB_FX_2023_B10_TDJBXX 不存在')

            print('数据表 JYBB_FX_2023_B10_TDJBXX 数据转存中...')
            cursor.execute(r'SELECT * INTO JYBB_FX_2023_B10_TDJBXX FROM VIEW_JYBB_FX_2023_B10_TDJBXX')
            print('数据表 JYBB_FX_2023_B10_TDJBXX 数据转存完成')
            record('数据表 JYBB_FX_2023_B10_TDJBXX 数据转存完成')

            cursor.commit()
            cursor.close()
            connect.close()
    else:
        connect.close()
        print('沈闻ERP 2数据库无法连接')
        record('沈闻ERP 2数据库无法连接')
    pass

def generate_tx_erp_tdjbxx():
    connectionString = (f'DRIVER={{SQL Server}};'
                        f'SERVER=192.168.1.23;'
                        f'DATABASE=cwbase6;'
                        f'UID=lc0069999;'
                        f'PWD=aaaaaa;'
                        f'TrustServerCertificate=yes')

    connect = pyodbc.connect(connectionString)

    if connect:
        print('天翔ERP 2数据库连接成功')
        record('天翔ERP 2数据库连接成功')

        cursor = connect.cursor()
        cursor.execute(r"SELECT count(*) FROM sysobjects WHERE name='JYBB_FX_2023_B10_TDJBXX'")
        isExistTable = cursor.fetchone()

        if isExistTable[0] == 1:
            print('数据表 JYBB_FX_2023_B10_TDJBXX 存在')
            record('数据表 JYBB_FX_2023_B10_TDJBXX 存在')

            cursor.execute(r'DROP TABLE JYBB_FX_2023_B10_TDJBXX')
            print('数据表 JYBB_FX_2023_B10_TDJBXX 删除成功')
            record('数据表 JYBB_FX_2023_B10_TDJBXX 删除成功')

            print('数据表 JYBB_FX_2023_B10_TDJBXX 数据转存中...')
            cursor.execute(r'SELECT * INTO JYBB_FX_2023_B10_TDJBXX FROM VIEW_JYBB_FX_2023_B10_TDJBXX')
            print('数据表 JYBB_FX_2023_B10_TDJBXX 数据转存完成')
            record('数据表 JYBB_FX_2023_B10_TDJBXX 数据转存完成')

            cursor.commit()
            cursor.close()
            connect.close()
        else:
            print('数据表 JYBB_FX_2023_B10_TDJBXX 不存在')
            record('数据表 JYBB_FX_2023_B10_TDJBXX 不存在')

            print('数据表 JYBB_FX_2023_B10_TDJBXX 数据转存中...')
            cursor.execute(r'SELECT * INTO JYBB_FX_2023_B10_TDJBXX FROM VIEW_JYBB_FX_2023_B10_TDJBXX')
            print('数据表 JYBB_FX_2023_B10_TDJBXX 数据转存完成')
            record('数据表 JYBB_FX_2023_B10_TDJBXX 数据转存完成')

            cursor.commit()
            cursor.close()
            connect.close()
    else:
        connect.close()
        print('天翔ERP 2数据库无法连接')
        record('天翔ERP 2数据库无法连接')
    pass

def generate_sjpt_cpmx():
    connect = pymysql.connect(host='192.168.1.40',
                              database='cyfm',
                              user='dp',
                              password='Tianxv12345.',
                              charset='utf8')

    if connect:
        print('报表平台数据库连接成功')
        record('报表平台数据库连接成功')

        cursor = connect.cursor()
        cursor.execute(r"SELECT count(*) FROM information_schema.TABLES WHERE TABLE_NAME='JYBB_FX_2023_B08_CPMX'")
        isExistTable = cursor.fetchone()

        if isExistTable[0] == 1:
            print('数据表 JYBB_FX_2023_B08_CPMX 存在')
            record('数据表 JYBB_FX_2023_B08_CPMX 存在')

            cursor.execute(r'DROP TABLE JYBB_FX_2023_B08_CPMX')
            print('数据表 JYBB_FX_2023_B08_CPMX 删除成功')
            record('数据表 JYBB_FX_2023_B08_CPMX 删除成功')

            print('数据表 JYBB_FX_2023_B08_CPMX 数据转存中...')
            cursor.execute(r'CREATE TABLE JYBB_FX_2023_B08_CPMX (SELECT * FROM VIEW_JYBB_FX_2023_B08_CPMX)')
            print('数据表 JYBB_FX_2023_B08_CPMX 数据转存完成')
            record('数据表 JYBB_FX_2023_B08_CPMX 数据转存完成')

            connect.commit()

            cursor.close()
            connect.close()
        else:
            print('数据表 JYBB_FX_2023_B08_CPMX 不存在')
            record('数据表 JYBB_FX_2023_B08_CPMX 不存在')

            print('数据表 JYBB_FX_2023_B08_CPMX 数据转存中...')
            cursor.execute(r'CREATE TABLE JYBB_FX_2023_B08_CPMX (SELECT * FROM VIEW_JYBB_FX_2023_B08_CPMX)')
            print('数据表 JYBB_FX_2023_B08_CPMX 数据转存完成')
            record('数据表 JYBB_FX_2023_B08_CPMX 数据转存完成')

            connect.commit()

            cursor.close()
            connect.close()
    else:
        connect.close()
        print('报表平台数据库无法连接')
        record('报表平台数据库无法连接')
    pass

def generate_sjpt_htmx():
    connect = pymysql.connect(host='192.168.1.40',
                              database='cyfm',
                              user='dp',
                              password='Tianxv12345.',
                              charset='utf8')

    if connect:
        print('报表平台数据库连接成功')
        record('报表平台数据库连接成功')

        cursor = connect.cursor()
        cursor.execute(r"SELECT count(*) FROM information_schema.TABLES WHERE TABLE_NAME='JYBB_FX_2023_B06_HTMX'")
        isExistTable = cursor.fetchone()

        if isExistTable[0] == 1:
            print('数据表 JYBB_FX_2023_B06_HTMX 存在')
            record('数据表 JYBB_FX_2023_B06_HTMX 存在')

            cursor.execute(r'DROP TABLE JYBB_FX_2023_B06_HTMX')
            print('数据表 JYBB_FX_2023_B06_HTMX 删除成功')
            record('数据表 JYBB_FX_2023_B06_HTMX 删除成功')

            print('数据表 JYBB_FX_2023_B06_HTMX 数据转存中...')
            cursor.execute(r'CREATE TABLE JYBB_FX_2023_B06_HTMX (SELECT * FROM VIEW_JYBB_FX_2023_B06_HTMX)')
            print('数据表 JYBB_FX_2023_B06_HTMX 数据转存完成')
            record('数据表 JYBB_FX_2023_B06_HTMX 数据转存完成')

            connect.commit()

            cursor.close()
            connect.close()
        else:
            print('数据表 JYBB_FX_2023_B06_HTMX 不存在')
            record('数据表 JYBB_FX_2023_B06_HTMX 不存在')

            print('数据表 JYBB_FX_2023_B06_HTMX 数据转存中...')
            cursor.execute(r'CREATE TABLE JYBB_FX_2023_B06_HTMX (SELECT * FROM VIEW_JYBB_FX_2023_B06_HTMX)')
            print('数据表 JYBB_FX_2023_B06_HTMX 数据转存完成')
            record('数据表 JYBB_FX_2023_B06_HTMX 数据转存完成')

            connect.commit()

            cursor.close()
            connect.close()
    else:
        connect.close()
        print('报表平台数据库无法连接')
        record('报表平台数据库无法连接')
    pass


if __name__ == '__main__':
    # generate_sw_erp_tdjbxx()
    # generate_tx_erp_tdjbxx()
    # generate_sjpt_cpmx()
    # generate_sjpt_htmx()
    pass
