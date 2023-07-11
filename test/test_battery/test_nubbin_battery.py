import unittest
from datetime import date

from battery.nubbin_battery import NubbinBattery


class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat('2020-01-02')
        last_service_date = date.fromisoformat('2016-01-01')
        battery = NubbinBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())
    
    def test_needs_service_false(self):
        current_date = date.fromisoformat('2020-01-01')
        last_service_date = date.fromisoformat('2018-01-01')
        battery = NubbinBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())
