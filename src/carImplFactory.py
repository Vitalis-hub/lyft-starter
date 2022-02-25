from .carFactory import CarFactory
from .capuletEngine import CapuletEngine
from .spindlerBattery import SpindlerBattery
from .willoughbyEngine import WilloughbyEngine
from .sternmanEngine import SternmanEngine
from .nubbinBattery import NubbinBattery
from .car import Car
from .tireImplementationService import TireImplementationService

class CarImplFactory(CarFactory):
    
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_type, tire_status):
        super().create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire_type, tire_status)
        capuletEngine = CapuletEngine(last_service_mileage, current_mileage)
        spindlerBattery = SpindlerBattery(last_service_date, current_date)
        tire = TireImplementationService(tire_type, tire_status)
        calliope = Car(capuletEngine, spindlerBattery, tire)
        return calliope
    
    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_type, tire_status):
        super().create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire_type, tire_status)
        willoughbyEngine =  WilloughbyEngine(last_service_mileage, current_mileage)
        spindlerBattery = SpindlerBattery(last_service_date, current_date)
        tire = TireImplementationService(tire_type, tire_status)
        glissage = Car(willoughbyEngine, spindlerBattery, tire)
        return glissage
    
    def create_palindrome(self, current_date, last_service_date, warning_light_on, tire_type, tire_status):
        super().create_palindrome(last_service_date, warning_light_on, tire_type, tire_status)
        sternmanEngine = SternmanEngine(warning_light_on)
        spindlerBattery = SpindlerBattery(last_service_date, current_date)
        tire = TireImplementationService(tire_type, tire_status)
        palindrom = Car(sternmanEngine, spindlerBattery, tire)
        return palindrom
    
    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_type, tire_status) -> Car:
        super().create_rorschach(last_service_date, current_mileage, last_service_mileage, tire_type, tire_status)
        willoughbyEngine =  WilloughbyEngine(last_service_mileage, current_mileage)
        nubbinBattery = NubbinBattery(last_service_date, current_date)
        tire = TireImplementationService(tire_type, tire_status)
        rorschach = Car(willoughbyEngine, nubbinBattery, tire)
        return rorschach
        
    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_type, tire_status):
        super().create_thovex(last_service_date, current_mileage, last_service_mileage, tire_type, tire_status)
        capuletEngine = CapuletEngine(last_service_mileage, current_mileage)
        nubbinBattery = NubbinBattery(last_service_date, current_date)
        tire = TireImplementationService(tire_type, tire_status)
        thovex = Car(capuletEngine, nubbinBattery, tire)
        return thovex

    