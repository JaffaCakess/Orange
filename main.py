
import paramiko
import sys
import cisco_parser
import ciscoconfparse as c
import shutil

# Empty list to store config output
storage = []
# Read IP addresses
address = open("ipaddresses")
print("="*40)
# Iterate through each ip address
for x in address:
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	# Establish SSHv2 connection to host
	try:
		client.connect(x, port=22, username="ben", password="cisco")
		print("Connected to {}".format(x.strip()))
	except paramiko.ssh_exception.NoValidConnectionsError:
		print("Connection to {} failed.".format(x.strip()))
		continue

	#print("="*40)
	# execute show command on device
	cmd = "show conf\n"
	stdin, stdout, stderr = client.exec_command(cmd)
	
	# Retrieving hostname for filename
	output = [line.strip("\r\n") for line in stdout]
	parser = c.CiscoConfParse(output)
	hostname = parser.find_lines("hostname")
	ext = ".cfg"
	for txt in hostname:
		name = txt.strip("hostname \n")
	filename = name + ext
	
	# print config to file
	orig_stdout = sys.stdout
	sys.stdout = open(filename, "w")
	for line in output:
		config = "".join(line)
		print(config)
	sys.stdout = orig_stdout
	
	# Send a copy of the config to a TFTP directory
        # Using Linux to Solarwinds free TFTP server on Windows
	shutil.copy2(filename, "/mnt/hgfs/TFTP-Root/")

	storage.append(filename)
	client.close()
print("="*40)
# Iterate through each .cfg file for errors
for x in storage:
	output = []
	with open(x) as f:
		parser = c.CiscoConfParse(x)
		errors = {}
                # Call the ios_config module to parse for errors
		cisco_parser.security(parser, errors)
		cisco_parser.router(parser, errors)
		for e in errors.keys():
			if not errors[e]:
				continue
			else:
				for error in errors[e]:
					output.append("{}".format(error))
		output.append("\nThe above config can be viewed in {}".format(x))
		output.append("="*40)
	for line in output:
		print(line)
