# Code for getting list of wifi clients (mac addresses) from your router
# This code is made and tested for Keenetic Giga 2 (Keenetic Giga II)
# Router firmware v2.06(AAFS.0)C3
# I could only find a way to get arp cache which contains all clients connected via wifi and lan


import telnetlib
import re

# Input data for your router
HOST = "192.168.0.1"
user = "#USER#"                                       # Please note that telnet is turned off by default 
password = "#your password#"                          # you need to make a new account to access telnet (readonly is acceptable)

tn = telnetlib.Telnet(HOST)                           # Connecting to host using standard Telnet port 23
tn.read_until(b"Login: ")                             # Awaiting for router to ask for login (Prints "login: ")
tn.write(user.encode('ascii') + b"\n")                # Writing your login
tn.read_until(b"Password: ")                          # Awaiting for router to ask for Password
tn.write(password.encode('ascii') + b"\n")            # Writing your password
tn.read_until(b"(config)> ")                          # Awaiting for router to write greetings and be ready
tn.write("show".encode('ascii') + b"\n")              # Sending command "show" to be able to input command
tn.read_until(b"(config)> ")                          # Awaiting for router to write greetings and be ready
tn.write("show associations".encode('ascii') + b"\n") # Sending command  show associations" to be able to input command
output= tn.read_until(b"(config)> ").decode('ascii')  # Awaiting for router to write wifi clients
# print (output)                                      # Print wifi clients
tn.close()                                            # Close telnet connection
# Getting list of Macs using regular expressions
found = re.findall(re.compile(r'(?:[0-9a-fA-F]:?){12}'), output)
for a in found:
    print (a)
