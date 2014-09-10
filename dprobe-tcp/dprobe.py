#!/usr/bin/env python

import re
hex_digit_pattern = r"[\dA-Fa-f]"

pat = r"\d+: " + \
      r"(?P<local_addr>HEX+):(?P<local_port>HEX+) " + \
      r"(?P<rem_addr>HEX+):(?P<rem_port>HEX+) " + \
      r"(?P<foo1>HEX+) " + \
      r"(?P<foo2>HEX+:HEX+) " + \
      r"(?P<foo3>HEX+:HEX+) " + \
      r"(?P<foo4>HEX+) +" + \
      r"(?P<foo5>\d+) +" + \
      r"(?P<foo6>\d+) " + \
      r"(?P<inode>\d+)" + \
      r"(?P<foo7>\d+) " + \
      r"(?P<foo8>HEX+) " + \
      r"(?P<foo9>\d+) " + \
      r"(?P<foo10>\d+) " + \
      r"(?P<foo11>\d+) " + \
      r"(?P<foo12>\d+) " + \
      r"(?P<foo13>-?\d+) "
pat = pat.replace("HEX", hex_digit_pattern)


f = open('/proc/net/tcp')
for line in f.readlines():
    if line.split()[0] == 'sl':
        continue
    values = re.search(pat, line).groupdict()
    print values
f.close()
