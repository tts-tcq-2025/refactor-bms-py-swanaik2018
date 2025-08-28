# vitals.py

VITAL_RANGES = {
    "temperature": (95, 102),
    "pulse": (60, 100),
    "spo2": (90, float('inf'))
}

def is_vital_ok(vital_name, value):
    if vital_name not in VITAL_RANGES:
        raise ValueError(f"Unknown vital: {vital_name}")
    min_val, max_val = VITAL_RANGES[vital_name]
    return min_val <= value <= max_val

def check_vitals(vital_values: dict):
    return {
        vital: is_vital_ok(vital, value)
        for vital, value in vital_values.items()
    }
