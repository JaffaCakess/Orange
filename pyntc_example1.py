
import json
from pyntc import ntc_device as NTC
iosvl2 = NTC(
        host="192.168.122.82",
        username="ben",
        password="cisco",
        device_type="cisco_ios_ssh")
iosvl2.open()
ios_run = iosvl2.backup_running_config("iosvl2-1.cfg")
