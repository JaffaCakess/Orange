#!/usr/bin/env python

import getpass
import telnetlib

# Prompt for username and password
user = raw_input("Enter your telnet username: ")
password = getpass.getpass()

# Open the host file
f = open("myswitches")

# Loop through each IP in "myswitches" file
for line in f:
    print "Getting running config from Switch " + line
    HOST = line.strip()
    tn = telnetlib.Telnet(HOST)
    
    # Username and password you entered earlier
    tn.read_until("Username: ")
    tn.write(user + "\n")
    if password:
        tn.read_until("Password: ")
        tn.write(password + "\n")

    # Run specific commands
    tn.write("terminal length 0\n")
    tn.write("show run\n")
    tn.write("exit\n")

    # Read the running-config then store in a file
    output = tn.read_all()
    with open("switch" + HOST, "w") as saveoutput:
        saveoutput.write(output)
