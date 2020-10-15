# -*- coding:utf-8 -*-
# @project : test_sq
# @author : admin
# @file : 远程控制linux.py
# @ide : PyCharm
# @time : 2020/10/14 10:32
import paramiko
#--1 创建ssh 对象
ssh = paramiko.SSHClient()
#--2  设置连接方式
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#--3连接  ip  端口   用户名  密码
ssh.connect("192.168.3.112",22,"root","123456")
#--4  输入命令
#标准文件三兄弟
"""
stdin = chan.makefile("wb",bufsize)  以二进制格式写入文件
stdout = chan.makefile("r",bufsize)   以二进制格式读取文件
stderr = chan.makefile_stderr("r",bufsize)  以二进制格式读取文件的错误信息
"""

stdin,stdout,stderr = ssh.exec_command("less cd /home/logs/domain.log.2020-10-15.0.log")
# print(stdin)
# print(stdout.read().decode("utf8"))
newStr = stdout.read().decode("utf8")

with open("./a.txt","w",encoding="utf-8") as f:
    f.write(newStr)
# print(stderr.read())
# stdin,stdout,stderr = ssh.exec_command("pwd")
# print(stdout.read().decode("utf8"))
ssh.close()