# -*- coding: utf-8 -*-
from urllib import request
import socket
hosts = ''
rfile = open('/other/domain.txt','r')
rfile.write(hosts)
domain = str(rfile.read(),'UTF-8').splitlines()
rfile.close()
for index in range(len(domain)):
    print(domain[index])
    try:
      ip = socket.gethostbyname(domain[index])
    except:
      ip = "unknow"
      print("解析失败" + domain[index])
    hosts = hosts + ip + " " + domain[index]+"\r\n"
wfile = open('hosts.txt','w')
wfile.write(hosts)
wfile.close()