# -*- coding: utf-8 -*-
# Author : xy_cloud
import json
import os
import socket
import sys

args = sys.argv
if not '-b' in args:
    os.chdir('run')


def is_port_free(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind(('', port))
        s.close()
        return True
    except OSError:
        return False


def find_free_port():
    for port in range(80, 65536):
        if is_port_free(port):
            return port
    return -1


print('假如您想高度自定义配置(如端口)，请勿使用简单启动！')
p = find_free_port()
if p == -1:
    print('您的电脑没有可用端口(范围:80-65535)')
    exit(-1)
print(f'您的服务器将在 {p} 端口运行')
AllowConnect = input('是否对公网开放?(需要有公网ip)(y/n):')
while AllowConnect.upper() != 'Y' and AllowConnect.upper() != 'N':
    AllowConnect = input('是否对公网开放?(需要有公网ip)(y/n):')
if AllowConnect.upper() == 'Y':
    AllowConnect = True
else:
    AllowConnect = False
with open('../config/server.json', 'r', encoding='utf-8') as f:
    j = json.loads(f.read())
    j["AllowConnect"] = AllowConnect
    j["Port"] = p
with open('../config/server.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(j))
os.system(r'Run.bat')
