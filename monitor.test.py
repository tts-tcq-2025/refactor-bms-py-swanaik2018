# monitor_test.py

import unittest
from vitals import check_vitals, is_vital_ok

class TestVitals(unittest.TestCase):
    # Temperature tests
    def test_temperature_below_range(self):
        self.assertFalse(is_vital_ok("temperature", 94.9))

    def test_temperature_at_lower_bound(self):
        self.assertTrue(is_vital_ok("temperature", 95))

    def test_temperature_above_range(self):
        self.assertFalse(is_vital_ok("temperature", 102.1))

    # Pulse tests
    def test_pulse_below_range(self):
        self.assertFalse(is_vital_ok("pulse", 59))

    def test_pulse_at_upper_bound(self):
        self.assertTrue(is_vital_ok("pulse", 100))

    def test_pulse_above_range(self):
        self.assertFalse(is_vital_ok("pulse", 101))

    # SpO2 tests
    def test_spo2_below_threshold(self):
        self.assertFalse(is_vital_ok("spo2", 89.9))

    def test_spo2_exact_threshold(self):
        self.assertTrue(is_vital_ok("spo2", 90))

    def test_spo2_above_threshold(self):
        self.assertTrue(is_vital_ok("spo2", 98))

    # Combined checks
    def test_all_vitals_ok(self):
        values = {"temperature": 98.6, "pulse": 75, "spo2": 96}
        result = check_vitals(values)
        self.assertTrue(all(result.values()))

    def test_multiple_vitals_not_ok(self):
        values = {"temperature": 104, "pulse": 40, "spo2": 80}
        result = check_vitals(values)
        self.assertFalse(result["temperature"])
        self.assertFalse(result["pulse"])
        self.assertFalse(result["spo2"])

    def test_invalid_vital_name_raises_exception(self):
        with self.assertRaises(ValueError):
            is_vital_ok("blood_pressure", 120)

if __name__ == "__main__":
    unittest.main()
