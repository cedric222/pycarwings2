#!/usr/bin/python

import pycarwings2
import time
from ConfigParser import SafeConfigParser
import logging
import sys
import pprint

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

parser = SafeConfigParser()
candidates = [ 'config.ini', 'my_config.ini' ]
found = parser.read(candidates)

username = parser.get('get-leaf-info', 'username')
password = parser.get('get-leaf-info', 'password')

logging.debug("login = %s , password = %s" % ( username , password)  )

print "Prepare Session"
s = pycarwings2.Session(username, password , "NE")
print "Login..."
l = s.get_leaf()

climate = l.get_latest_hvac_status()
pprint.pprint(climate.answer)
result_key = l.request_update()
time.sleep(30) # sleep 30 seconds to give request time to process
battery_status = l.get_status_from_update(result_key)
while battery_status is None:
	print "not update"
        time.sleep(10)
	battery_status = l.get_status_from_update(result_key)

pprint.pprint(battery_status.answer)
leaf_info = l.get_latest_battery_status()

#result_key = l.start_climate_control()
#time.sleep(60)
#start_cc_result = l.get_start_climate_control_result(result_key)

#result_key = l.stop_climate_control()
#time.sleep(60)
#stop_cc_result = l.get_stop_climate_control_result(result_key)
