
def security(parser, errors):
	errors["security"] = []
	if parser.find_objects(r"no\saaa\snew-model"):
		errors["security"].append("No AAA configured.")	
	if " transport input telnet ssh" in parser.find_all_children(r"line vty") or " transport input telnet" in parser.find_all_children(r"line vty"):
		errors["security"].append("Telnet is configured (insecure)")	
	if not parser.find_objects(r"service\spassword-encryption"):
		errors["security"].append("No service password-encryption")
	for obj in parser.find_objects_w_child(r"line", r"privilege level 15"):
		errors["security"].append(obj.text.strip("\n") + " has privilege level 15")
	for obj in parser.find_lines(r"privilege 15"):
		errors["security"].append(obj.strip("\n"))
	#if parser.find_objects(r"no\sip\shttp\sserver"):
		

def router(parser, errors):
	errors["router"] = []
	for obj in parser.find_objects_w_child("interface", "duplex half"):
		errors["router"].append(obj.text.strip("\n") + " has half duplex")
