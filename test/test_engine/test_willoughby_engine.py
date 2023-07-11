import unittest

from engine.willoughby_engine import WilloughbyEngine


class TestWilloughbyEngine(unittest.TestCase):
    def test_needs_service_true(self):
        last_service_mileage = 100000
        current_mileage = 160001
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertTrue(engine.needs_service())
    
    def test_needs_service_false(self):
        last_service_mileage = 100000
        current_mileage = 160000
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertFalse(engine.needs_service())
