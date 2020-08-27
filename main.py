from system_devices import *

checker = system_devices(config="config.json")
xbee = checker.device('xbee')
gps = checker.device('gps')
pwm = checker.pwm(wait_seconds=5)
