from scapy.all import *

from scapy.layers.inet import TCP, IP

sport = random.randint(1024, 65535)
SYN = TCP(sport=sport, dport=22345, flags='S', seq=123451000)
ip = IP(dst="127.0.0.1")
sr1(ip / SYN)
