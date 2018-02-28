#!/usr/bin/python

import netaddr
import sys

for h in netaddr.IPNetwork(sys.argv[1]).iter_hosts():
	print h
