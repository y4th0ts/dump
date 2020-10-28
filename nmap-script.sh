#!/bin/bash

# This is a simple script that will automate the process of doing an nmap scan by simply scanning
# the target for open ports and directing the output to another nmap scan with -sV -sC flag for
# Service/Version detection and scanning using default scripts.

if [ $# -eq 0 ]
  then
    echo -e "\e[31m[-] Usage: ./nmap-script <IP-ADDRESS>\e[39m"
    exit 1
fi

if [[ $1 =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
	mkdir nmap-scan
	echo -e "\e[32m[*] Initiating port scan on target.\e[39m"
	echo -e "\e[32m[*] Results will be saved to nmap-scan/$1.portscan file.\e[39m"
	ports=$(nmap -oN nmap-scan/$1.portscan $1 | grep open | cut -d"/" -f1 | tr '\n' ',' | sed 's/.$//');
	if [ -z "$ports" ]; then
		echo -e "\e[31m[-] Port scan failed. Host seems to be down.\e[39m"
		exit 1
	fi
	echo -e "\e[32m[*] Discovered open ports\e[0m:\e[0m";
	echo -e "\e[92m$(cat nmap-scan/$1.portscan | grep open | sed 's/ open / -/')\e[39m"; else
	echo -e "\e[31m[-] Usage: ./nmap-script <IP-ADDRESS>\e[39m"
	exit 1
fi
echo ""
echo -e "\e[32m[*] Initiating service scan on discovered open ports.\e[39m"
nmap -sVC -oN nmap-scan/$1.sVsC-scan $1 -p $ports
echo -e "\e[32m[*] Done! Results are saved to nmap-scan/$1.sVsC-scan file.\e[39m"
