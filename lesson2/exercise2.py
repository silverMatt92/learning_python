#!/usr/bin/env python
"""Create a list of five IP addresses.
Use the .append() method to add an IP address onto the end of the list. Use the .extend()
method to add two more IP addresses to the end of the list.
Use list concatenation to add two more IP addresses to the end of the list.
Print out the entire list of ip addresses. Print out the first IP address in the list. Print out
the last IP address in the list.
Using the .pop() method to remove the first IP address in the list and the last IP address in
the list.
Update the new first IP address in the list to be '2.2.2.2'. Print out the new first IP address
in the list.
"""
from __future__ import print_function, unicode_literals

ip_list = ['192.168.1.1', '10.0.10.1', '54.34.67.5', '172.31.49.8', '8.8.8.8']
ip_list.append('1.1.1.1')
ip_list.extend(['198.80.80.80', '45.64.9.8'])
ip_list = ip_list + ['10.10.10.10', '3.3.3.3']
print(ip_list)
print(ip_list[0])
print(ip_list[-1])
ip_list.pop(0)
ip_list.pop()
ip_list[0] = '2.2.2.2'
print(ip_list[0])

