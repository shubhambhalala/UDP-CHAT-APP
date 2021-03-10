#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket as sk
import threading
import os

s = sk.socket(sk.AF_INET , sk.SOCK_DGRAM )
s.bind(('192.168.99.106',5555))
print("CHAT SERVICE UP AND RUNNING")
print("Enter q or quit to end the session")
name = input("Enter your name (press enter to take system name): ") or sk.gethostname()
connect = '192.168.99.102'


def send():
    while True:
        msg = input()
        if msg == "quit" or msg == 'q':
            msg = "{0} : {1}".format("CHAT BOT","Your partner choose to exit, Bye!")
            s.sendto(str.encode(msg),(connect,5555))
            os._exit(1)
        else:
            msgfinal = "{} : {}".format(name,msg)
            s.sendto(str.encode(msgfinal),(connect,5555))

def recv():
    while True:
        msg = s.recvfrom(1024)
        print("\t\t\t\t"+msg[0].decode())
        if msg[0].decode("utf-8") == "CHAT BOT : Your partner choose to exit, Bye!":
            os._exit(1)

x1 = threading.Thread(target = send)
x2 = threading.Thread(target = recv)

x1.start()
x2.start()


# In[ ]:




