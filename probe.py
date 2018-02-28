#!/usr/bin/python

import argparse
from scapy.all import *

target = sys.argv[1]

parser = argparse.ArgumentParser()
parser.add_argument("target", help="target")
parser.add_argument("--timeout", type=int, default=3, help="timeout for scapy sr1")
parser.add_argument("--debug", action="store_true", default=False, help="debug output")
args = parser.parse_args()

memcached_stats = "\x00\x01\x00\x00\x00\x01\x00\x00\x73\x74\x61\x74\x73\x0d\x0a"
ans = sr1(IP(dst=args.target)/UDP(sport=12345, dport=11211)/memcached_stats, timeout=args.timeout, verbose=False)
if ans and ans.haslayer(UDP) and (str(ans.payload).find("STAT version") > -1):
	print "memcached response detected from %s" % target
	if args.debug:
		print ans.summary()
