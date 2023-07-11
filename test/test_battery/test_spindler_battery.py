import unittest
from datetime import date

from battery.spindler_battery import SpindlerBattery


class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat('2020-01-01')
        last_service_date = date.fromisoformat('2017-01-01')
        battery = SpindlerBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())
    
    def test_needs_service_false(self):
        current_date = date.fromisoformat('2020-01-01')
        last_service_date = date.fromisoformat('2018-01-17')
        battery = SpindlerBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())
