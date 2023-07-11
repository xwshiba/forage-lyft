from car import Car

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires


class CarFactory(Car):
    """
    A factory class for creating different types of cars.

    This factory class provides static methods to create instances of various car models
    with different engine and battery combinations. Each method takes specific parameters
    to configure the car based on the desired model and its current status.

    Note: The class assumes that the imported modules (car, engine, battery) exist in the project.
    """
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tires_wear_array):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = CarriganTires(tires_wear_array)
        calliope = Car(battery, engine, tires)
        
        return calliope
    
    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tires_wear_array):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = OctoprimeTires(tires_wear_array)
        glissade = Car(battery, engine, tires)
        
        return glissade

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_is_on, tires_wear_array):
        engine = SternmanEngine(last_service_date, warning_light_is_on)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = OctoprimeTires(tires_wear_array)
        palindrome = Car(battery, engine, tires)
        
        return palindrome

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tires_wear_array):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tires = CarriganTires(tires_wear_array)
        rorschach = Car(battery, engine, tires)
        
        return rorschach

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tires_wear_array):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tires = OctoprimeTires(tires_wear_array)
        thovex = Car(battery, engine, tires)
        
        return thovex
