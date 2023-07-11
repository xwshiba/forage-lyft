import unittest

from engine.capulet_engine import CapuletEngine


class TestCapuletEngine(unittest.TestCase):
    def test_needs_service_true(self):
        last_service_mileage = 100000
        current_mileage = 160001
        engine = CapuletEngine(last_service_mileage, current_mileage)
        self.assertTrue(engine.needs_service())
    
    def test_needs_service_false(self):
        last_service_mileage = 100000
        current_mileage = 130000
        engine = CapuletEngine(last_service_mileage, current_mileage)
        self.assertFalse(engine.needs_service())
