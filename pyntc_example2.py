
import json
from pyntc import ntc_device as NTC
iosvl2 = NTC(
        host="192.168.122.82",
        username="ben",
        password="cisco",
        device_type="cisco_ios_ssh")
iosvl2.open()

ios_output = iosvl2.facts
print(json.dumps(ios_output, indent=4))

iosvl2.config_list([
    "hostname s1",
    "router ospf 1",
    "no network 0.0.0.0 255.255.255.255 area 0",
    "network 10.1.1.0 0.0.0.255 area 0",
    "network 10.1.2.0 0.0.0.255 area 1"])
