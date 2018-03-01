# memcached-probe

## Disclamer

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.

## Overview

Tool can be used to check set of IPv4 addresses for existence of memcached
service in potentialy vulnerable configuration allowing reflected amplified
DDoS attack with UDP protocol [1].

[1] https://isc.sans.edu/forums/diary/How+did+this+Memcache+thing+happen/23391/

## Install

```
git clone repository
apt-get install python-netaddr scapy
```

## Run

```
./enumips.py a.b.c.d/e > 00list
./go.sh 00list > 00results
```
