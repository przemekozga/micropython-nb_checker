from system_devices import *

checker = system_devices(config="config.json")
xbee = checker.device('xbee')
gps = checker.device('gps')
mpu = checker.device('mpu')
pwm = checker.pwm(wait_seconds=5)
