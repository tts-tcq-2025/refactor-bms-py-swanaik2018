# alerts.py

import sys
from time import sleep

def blink_alert(times=6):
    for _ in range(times):
        print('\r* ', end='')
        sys.stdout.flush()
        sleep(1)
        print('\r *', end='')
        sys.stdout.flush()
        sleep(1)

def alert_if_not_ok(vital_name, is_ok):
    if not is_ok:
        print(f"{vital_name} is out of range!")
        blink_alert()
        return False
    return True
