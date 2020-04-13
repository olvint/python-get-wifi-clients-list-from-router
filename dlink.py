# Code for getting list of wifi clients (mac addresses) from your router
# This code is made and tested fot Dlink DIR-825ACG1 revision G1A 
# Router firmware 2019.04.17-12.40_DIR_825AC_G1A_UFANET_1.0.5_release)

import telnetlib
import time

# Input data for your router
HOST = "192.168.0.1"
user = "admin"
password = "$your password$"


tn = telnetlib.Telnet(HOST)                           # Connecting to host using standard Telnet port 23
tn.read_until(b"login: ")                             # Awaiting for router to ask for login (Prints "login: ")
tn.write(user.encode('ascii') + b"\n")                # Writing your login
tn.read_until(b"Password: ")                          # Awaiting for router to ask for Password
tn.write(password.encode('ascii') + b"\n")            # Writing your password
tn.read_until(b"$")                                   # Awaiting for router to write greetings and be ready
tn.write("resident_cli".encode('ascii') + b"\n")      # Sending command "resident_cli" to be able to input command
time.sleep(1)                                         # Awaiting for one second to press "enter" another time
tn.write(b"\n")                                       # Sending Enter
tn.read_until(b"Login: ")                             # Awaiting for router to ask for login (Note capital "L")
tn.write(user.encode('ascii') + b"\n")                # Writing your login
tn.read_until(b"Password: ")                          # Awaiting for router to ask for Password
tn.write(password.encode('ascii') + b"\n")            # Writing your password
tn.read_until(b"#")                                   # Awaiting for router to write greetings and be ready
tn.write("show wifi clients".encode('ascii') + b"\n") # Sending command "show wifi clients" to be able to input command
output=tn.read_until(b"OK <20>").decode('ascii')      # Awaiting for router to write wifi clients
print (output)                                        # Print wifi clients
tn.close()                                            # Close telnet connection
