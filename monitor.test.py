# monitor.test.py
import unittest
from monitor import check_vitals


class MonitorTest(unittest.TestCase):
    def test_temperature_out_of_range(self):
        result = check_vitals(94.9, 70, 98)
        self.assertFalse(result["temperature"])

    def test_temperature_edge_values(self):
        self.assertTrue(check_vitals(95, 70, 98)["temperature"])
        self.assertTrue(check_vitals(102, 70, 98)["temperature"])
        self.assertFalse(check_vitals(102.1, 70, 98)["temperature"])

    def test_pulse_out_of_range(self):
        result = check_vitals(98.6, 59, 98)
        self.assertFalse(result["pulse"])

    def test_pulse_edge_values(self):
        self.assertTrue(check_vitals(98.6, 60, 98)["pulse"])
        self.assertTrue(check_vitals(98.6, 100, 98)["pulse"])
        self.assertFalse(check_vitals(98.6, 101, 98)["pulse"])

    def test_spo2_out_of_range(self):
        result = check_vitals(98.6, 70, 89)
        self.assertFalse(result["spo2"])

    def test_spo2_edge_values(self):
        self.assertTrue(check_vitals(98.6, 70, 90)["spo2"])
        self.assertFalse(check_vitals(98.6, 70, 89.9)["spo2"])

    def test_all_vitals_ok(self):
        result = check_vitals(98.6, 70, 95)
        self.assertTrue(all(result.values()))

    def test_multiple_vitals_not_ok(self):
        result = check_vitals(103, 50, 85)
        self.assertFalse(result["temperature"])
        self.assertFalse(result["pulse"])
        self.assertFalse(result["spo2"])


if __name__ == '__main__':
    unittest.main()
