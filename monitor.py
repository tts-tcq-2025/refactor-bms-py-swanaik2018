# monitor.py
import sys
from time import sleep

# --- Pure logic (functional style) ---
def is_temperature_ok(temp):
    return 95 <= temp <= 102

def is_pulse_rate_ok(pulse):
    return 60 <= pulse <= 100

def is_spo2_ok(spo2):
    return spo2 >= 90

def check_vitals(temperature, pulseRate, spo2):
    return {
        "temperature": is_temperature_ok(temperature),
        "pulse": is_pulse_rate_ok(pulseRate),
        "spo2": is_spo2_ok(spo2)
    }

# --- I/O and actions (procedural + aspect-oriented style) ---
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

def vitals_ok(temperature, pulseRate, spo2):
    results = check_vitals(temperature, pulseRate, spo2)
    return (
        alert_if_not_ok("Temperature", results["temperature"]) and
        alert_if_not_ok("Pulse Rate", results["pulse"]) and
        alert_if_not_ok("Oxygen Saturation", results["spo2"])
    )
