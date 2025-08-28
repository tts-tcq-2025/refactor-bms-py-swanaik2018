# monitor.py

from vitals import check_vitals
from alerts import alert_if_not_ok

def vitals_ok(temperature, pulse_rate, spo2):
    vital_values = {
        "temperature": temperature,
        "pulse": pulse_rate,
        "spo2": spo2
    }

    results = check_vitals(vital_values)

    all_ok = True
    for vital, is_ok in results.items():
        label = vital.replace("_", " ").capitalize()
        all_ok = alert_if_not_ok(label, is_ok) and all_ok

    return all_ok
