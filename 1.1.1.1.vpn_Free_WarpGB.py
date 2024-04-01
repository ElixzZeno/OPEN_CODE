"""
    @ Reverse By ---( MD Raj )---
    @ Follow Our Github : Ahmed-XD
"""
import urllib.request
import json
import datetime
import random
import string
import time
import os
import sys
if os.name == 'posix':
    os.system('clear')
else:
    os.system('cls')

print('''
\x1b[38;5;82m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
\x1b[38;5;82m┃\x1b[38;5;82m___  _    ____ ____ _  _    ___  ____ _  _ _ _┃\x1b[38;5;84mCEO : \033[1;93mPRINCE LIKHON\x1b[38;5;82m┃
\x1b[38;5;82m┃\x1b[38;5;83m|__] |    |__| |    |_/     |  \ |___ |  | | |\x1b[38;5;84m┃FB  : \x1b[38;5;82mLikhon       \x1b[38;5;82m┃
\x1b[38;5;82m┃\x1b[38;5;84m|__] |___ |  | |___ | \_    |__/ |___  \/  | |┃GIT : \033[1;95mMrDevilEx    \x1b[38;5;82m┃
\x1b[38;5;82m┣━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
\x1b[38;5;82m┃ TOOL : \x1b[38;5;84m Warp + GB\x1b[38;5;82m┃ WP : +966578146776┃ \x1b[38;5;84m VERSION :\033[1;91m 0.1 \x1b[38;5;82m           ┃
\x1b[38;5;82m╚━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝
[+] ABOUT SCRIPT:
[-] With this script, you can getting unlimited GB on Warp+.
[-] Version: 0.0.1
--------
[+] THIS SCRIPT CODDED BY MAHADI
[-] SITE: MrDevilEx.github.com
[-] TELEGRAM: MrDevilEx
--------''')
referrer = input("\x1b[38;5;82m[#] Enter the WARP+ ID:")

def genString(stringLength):
	try:
		letters = string.ascii_letters + string.digits
		return "".join(random.choice(letters) for i in range(stringLength))
	except Exception as error:
		print(error)

def digitString(stringLength):
	try:
		digit = string.digits
		return "".join((random.choice(digit) for i in range(stringLength)))
	except Exception as error:
		print(error)

def run():
	try:
		install_id = genString(22)
		url=(f'https://api.cloudflareclient.com/v0a{digitString(3)}/reg')
		body={
			"key": "{}=".format(genString(43)),
			"install_id": install_id,
			"fcm_token": "{}:APA91b{}".format(install_id, genString(134)),
			"referrer": referrer,
			"warp_enabled": False,
			"tos": datetime.datetime.now().isoformat()[:-3] + "+02:00",
			"type": "Android",
			"locale": "es_ES",
		}
		data = json.dumps(body).encode('utf8')
		headers={
			'Content-Type': 'application/json; charset=UTF-8',
			'Host': 'api.cloudflareclient.com',
			'Connection': 'Keep-Alive',
			'Accept-Encoding': 'gzip',
			'User-Agent': 'okhttp/3.12.1',
		}
		req = urllib.request.Request(url, data, headers)
		response = urllib.request.urlopen(req)
		status_code = response.getcode()
		return(status_code)
	except Exception as error:
		print(error)
g = 0
b = 0

while True:
	result  = run()
	if result == 200:
		g+=1
		if os.name == 'posix':
			os.system('clear')
		else:
			os.system('cls')
		print("\x1b[38;5;82m")
		print("                  WARP-PLUS-CLOUDFLARE (script)" + " By MAHADI\n")
		animation = ["[■□□□□□□□□□] 10%", "[■■□□□□□□□□] 20%", "[■■■□□□□□□□] 30%", "[■■■■□□□□□□] 40%", "[■■■■■□□□□□] 50%", "[■■■■■■□□□□] 60%", "[■■■■■■■□□□] 70%", "[■■■■■■■■□□] 80%", "[■■■■■■■■■□] 90%", "[■■■■■■■■■■] 100%"]
		for i in range(len(animation)):
			time.sleep(0.5)
			sys.stdout.write("\r[+] Preparing... " + animation[i % len(animation)])
			sys.stdout.flush()
		print(f"\n [-] WORK ON ID: {referrer}")
		print(f" [:)] {g} GB has been successfully added to your account.")
		print(f" [#] Total: {g} Good {b} Bad")
		print(f" [*] After 18 seconds, a new request will be sent.")
		time.sleep(18)
		continue
	else:
		b+=1
		if os.name == 'posix':
			os.system('clear')
		else:
			os.system('cls')
		print("\x1b[38;5;82m")
		print("                  WARP-PLUS-CLOUDFLARE (script)" + " By MAHADI\n")
		print("[:(] Error when connecting to server.")
		print(f"[#] Total: {g} Good {b} Bad")
		continue