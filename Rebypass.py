#Coding By Hannan
#Coding UTF-8
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass 
try:
    import requests
except ImportError:
    os.system('pip2 install mechanize')
    
try:
    import mechanize
except ImportError:
    os.system('pip2 install request')
    time.sleep(1)
    os.system('Then type: python2 Love.py')
 
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
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]
 
def exit():
	print 'CHAL BH***KE.'
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
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;91m"+o),;sys.stdout.flush();time.sleep(1)
 
 

vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

def ban():
jalan ('\033[1;94m███████╗███████╗
jalan ('\033[1;94m╚════██║██╔════╝
jalan ('\033[1;94m░░███╔═╝█████╗░░
jalan ('\033[1;94m██╔══╝░░██╔══╝░░
jalan ('\033[1;94m███████╗██║░░░░░
jalan ('\033[1;94m╚══════╝╚═╝░░░░░
def ok():
	os.system('clear')
	ban()
	jalan ('\033[1;91m[\033[1;97m1\033[1;91m] \033[1;96m~~~~~RAJA')
	jalan ('\033[1;91m[\033[1;97m2\033[1;91m] \033[1;92m~~~~~~ADF')
	jalan ('\033[1;91m[\033[1;97m3\033[1;91m] \033[1;93m~~~~~~~JUTT(1)')
	jalan ('\033[1;91m[\033[1;97m4\033[1;91m] \033[1;95m~~~~~~~~JUTT(2)')
	print (' ')
	haha = raw_input('\033[1;91m[\033[1;97m~\033[1;91m] \033[1;92mChoose: \033[1;97m')
	if haha =='':
		ok()
	elif haha =='1':
		os.system('python2 raja.py')
	elif haha =='2':
		os.system('python Adf.py')
	elif haha =='3':
		os.system('python number.py')
	elif haha =='4':
		os.system('python Juttbrand.py')
	else:
		ok()
		
ok()
		
                                                             
                                                             
                                                             
                                                             
                                                             
                                                             
