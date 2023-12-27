import time
from configparser import ConfigParser


def print_log(content, end='\n'):
    t = time.strftime("[%m-%d %H:%M:%S]", time.localtime())
    print(t, content, end=end)


def check_config():
    config = ConfigParser()
    config.read('user.conf', encoding='UTF-8')
    user = config['user']
    for item in user:
        if user[item] == '':
            print_log('配置信息不完整')
            return False
    return True
