import unittest

from tires.octoprime_tires import OctoprimeTires


class TestOctoprimeTires(unittest.TestCase):
    def test_needs_service_true(self):
        tires_wear_array = [1,1,1,0]
        tires = OctoprimeTires(tires_wear_array)
        self.assertTrue(tires.needs_service())
    
    def test_needs_service_false(self):
        tires_wear_array = [0.1,1,1,0.8]
        tires = OctoprimeTires(tires_wear_array)
        self.assertFalse(tires.needs_service())
