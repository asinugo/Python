# Example of running a OS command from Python
import os
from time import sleep

# Create string with the OS Command this is optional,  but useful for more complex commands
ip_to_ping = "8.8.8.8" # Google's public DNS
# List the directory contents. All of them.
cmd = "ls -a -l"
os.system(cmd)

# Ping the ip address specified by ip_to_ping
cmd = "ping -c 5 %s" % ip_to_ping
os.system(cmd)
sleep(5)

