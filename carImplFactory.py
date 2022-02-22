from carFactory import CarFactory
from capuletEngine import CapuletEngine
from spindlerBattery import SpindlerBattery
from willoughbyEngine import WilloughbyEngine
from sternmanEngine import SternmanEngine
from nubbinBattery import NubbinBattery
from car import Car

class CarImplFactory(CarFactory):
    
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        super().create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
        capuletEngine = CapuletEngine(last_service_mileage, current_mileage)
        spindlerBattery = SpindlerBattery(last_service_date, current_date)
        calliope = Car(capuletEngine, spindlerBattery)
        return calliope
    
    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        super().create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
        willoughbyEngine =  WilloughbyEngine(last_service_mileage, current_mileage)
        spindlerBattery = SpindlerBattery(last_service_date, current_date)
        glissage = Car(willoughbyEngine, spindlerBattery)
        return glissage
    
    def create_palindrom(self, current_date, last_service_date, warning_light_on):
        super().create_palindrom(last_service_date, warning_light_on)
        sternmanEngine = SternmanEngine(warning_light_on)
        spindlerBattery = SpindlerBattery(last_service_date, current_date)
        palindrom = Car(sternmanEngine, spindlerBattery)
        return palindrom
    
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        super().create_rorschach(last_service_date, current_mileage, last_service_mileage)
        willoughbyEngine =  WilloughbyEngine(last_service_mileage, current_mileage)
        nubbinBattery = NubbinBattery(last_service_date, current_date)
        rorschach = Car(willoughbyEngine, nubbinBattery)
        return rorschach
        
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        super().create_thovex(last_service_date, current_mileage, last_service_mileage)
        capuletEngine = CapuletEngine(last_service_mileage, current_mileage)
        nubbinBattery = NubbinBattery(last_service_date, current_date)
        thovex = Car(capuletEngine, nubbinBattery)
        return thovex

    