#!/usr/bin/env python
"""Read the 'show_ip_bgp_summ.txt' file into your program. From this BGP output obtain the
first and last lines of the output.
From the first line use the string .split() method to obtain the local AS number.
From the last line use the string .split() method to obtain the BGP peer IP address.
Print both local AS number and the BGP peer IP address to the screen.
"""
from __future__ import print_function, unicode_literals

with open("show_ip_bgp_summ.txt") as f:
    bgp_summ = f.readlines()

first = bgp_summ[0]
last = bgp_summ[-1]

asn = first.split()[-1]
bgp_peer = last.split()[0]
print("Local AS Number: {}".format(asn))
print("BGP Peer IP Address: {}".format(bgp_peer))
