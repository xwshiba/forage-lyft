import unittest

from tires.carrigan_tires import CarriganTires


class TestCarriganTires(unittest.TestCase):
    def test_needs_service_true(self):
        tires_wear_array = [0,0,0,0.9]
        tires = CarriganTires(tires_wear_array)
        self.assertTrue(tires.needs_service())
    
    def test_needs_service_false(self):
        tires_wear_array = [0,0,0,0.8]
        tires = CarriganTires(tires_wear_array)
        self.assertFalse(tires.needs_service())
