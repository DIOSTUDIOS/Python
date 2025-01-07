import cx_Oracle
import configparser
from datetime import datetime


def get_database_config():
    config = configparser.ConfigParser()
    config.read('conf.ini', encoding='utf-8')

    databaseInfo = {
        'host': config.get('database', 'host'),
        'port': config.get('database', 'port'),
        'sid': config.get('database', 'sid'),
        'username': config.get('database','user'),
        'password': config.get('database','password')
    }

    return databaseInfo


# 判断流程是否存在
def is_exist_process(processName):
    databaseInfo = get_database_config()

    connect = cx_Oracle.connect(user=databaseInfo['username'],
                                password=databaseInfo['password'],
                                dsn=cx_Oracle.makedsn(host=databaseInfo['host'],
                                                      port=databaseInfo['port'],
                                                      sid=databaseInfo['sid']))
    cursor = connect.cursor()

    cursor.execute(r'''
    SELECT COUNT(*) AS RESUTL FROM PROCESS_BUSINESS WHERE BUSINESS_NAME='{0}'
    '''.format(processName))

    result = cursor.fetchone()

    if result[0] == 0:
        cursor.close()
        connect.close()

        return False
    else:
        cursor.close()
        connect.close()

        return True


# 展示流程标识
def show_process_id(processName):
    databaseInfo = get_database_config()

    connect = cx_Oracle.connect(user=databaseInfo['username'],
                                password=databaseInfo['password'],
                                dsn=cx_Oracle.makedsn(host=databaseInfo['host'],
                                                      port=databaseInfo['port'],
                                                      sid=databaseInfo['sid']))
    cursor = connect.cursor()

    cursor.execute(r'''
    SELECT ID FROM PROCESS_BUSINESS WHERE BUSINESS_NAME='{0}'
    '''.format(processName))

    result = cursor.fetchall()

    ids = []

    for item in result:
        ids.append(item[0])

    return ids


# 展示流程相关信息
def show_process_info(processID):
    databaseInfo = get_database_config()

    connect = cx_Oracle.connect(user=databaseInfo['username'],
                                password=databaseInfo['password'],
                                dsn=cx_Oracle.makedsn(host=databaseInfo['host'],
                                                      port=databaseInfo['port'],
                                                      sid=databaseInfo['sid']))
    cursor = connect.cursor()

    cursor.execute(r'''
    SELECT YWLX,YWMC,JDMC,LCMC,DQBB FROM VIEW_DY_XX_YWLLCBBXXB WHERE LCID='{0}'
    '''.format(processID))

    details = cursor.fetchall()

    cursor.close()
    connect.close()

    return details


# 流程是否为最新版本
def is_newest_version(processID, processVersion):
    databaseInfo = get_database_config()

    connect = cx_Oracle.connect(user=databaseInfo['username'],
                                password=databaseInfo['password'],
                                dsn=cx_Oracle.makedsn(host=databaseInfo['host'],
                                                      port=databaseInfo['port'],
                                                      sid=databaseInfo['sid']))
    cursor = connect.cursor()

    cursor.execute(r'''
    SELECT PROCESS_DEFINITION_ID FROM PROCESS_BUSINESS WHERE ID='{0}'
    '''.format(processID))

    result = cursor.fetchone()

    if result[0] == processVersion:
        cursor.close()
        connect.close()

        return True
    else:
        cursor.close()
        connect.close()

        return False


# 更新业务链阶段流程
def update_phase_process(processName, processID, processVersion):
    databaseInfo = get_database_config()

    connect = cx_Oracle.connect(user=databaseInfo['username'],
                                password=databaseInfo['password'],
                                dsn=cx_Oracle.makedsn(host=databaseInfo['host'],
                                                      port=databaseInfo['port'],
                                                      sid=databaseInfo['sid']))
    cursor = connect.cursor()

    try:
        cursor.execute(r'''
        UPDATE BC_STAGE_PROCESS
        SET PROCESS_BUSINESS_VERSION='{0}'
        WHERE PROCESS_BUSINESS_ID='{1}'
        '''.format(processVersion, processID))

        connect.commit()

        with open('logs.txt', 'a', encoding='gbk') as logs:
            logs.write(datetime.now().strftime('%Y-%m-%d') + '\t更新阶段流程 {0} 版本为 {1}\n'.format(processName, processVersion))
            logs.close()
    except cx_Oracle.DatabaseError:
        cursor.rollback()
    finally:
        cursor.close()
        connect.close()


# 更新业务链前驱流程
def update_pre_process(processName, processID, processVersion):
    databaseInfo = get_database_config()

    connect = cx_Oracle.connect(user=databaseInfo['username'],
                                password=databaseInfo['password'],
                                dsn=cx_Oracle.makedsn(host=databaseInfo['host'],
                                                      port=databaseInfo['port'],
                                                      sid=databaseInfo['sid']))
    cursor = connect.cursor()

    try:
        cursor.execute(r'''
        UPDATE BC_CONFIG_P_DUAD
        SET PRE_PROCESS_VERSION='{0}'
        WHERE PRE_PROCESS='{1}'
        '''.format(processVersion, processID))

        connect.commit()

        with open('logs.txt', 'a', encoding='gbk') as logs:
            logs.write(datetime.now().strftime('%Y-%m-%d') + '\t更新前驱流程 {0} 版本为 {1}\n'.format(processName, processVersion))
            logs.close()
    except cx_Oracle.DatabaseError:
        cursor.rollback()
    finally:
        cursor.close()
        connect.close()


# 更新业务链后继流程
def update_next_process(processName, processID, processVersion):
    databaseInfo = get_database_config()

    connect = cx_Oracle.connect(user=databaseInfo['username'],
                                password=databaseInfo['password'],
                                dsn=cx_Oracle.makedsn(host=databaseInfo['host'],
                                                      port=databaseInfo['port'],
                                                      sid=databaseInfo['sid']))
    cursor = connect.cursor()

    try:
        cursor.execute(r'''
        UPDATE BC_CONFIG_P_DUAD
        SET NEXT_PROCESS_VERSION='{0}'
        WHERE NEXT_PROCESS='{1}'
        '''.format(processVersion, processID))

        connect.commit()

        with open('logs.txt', 'a', encoding='gbk') as logs:
            logs.write(datetime.now().strftime('%Y-%m-%d') + '\t更新后继流程 {0} 版本为 {1}\n'.format(processName, processVersion))
            logs.close()
    except cx_Oracle.DatabaseError:
        cursor.rollback()
    finally:
        cursor.close()
        connect.close()


if __name__ == '__main__':
    pass
