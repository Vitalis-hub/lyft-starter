from abc import ABC, abstractmethod

from car import Car

class CarFactory(ABC):
        
    @abstractmethod
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        pass
    
    @abstractmethod
    def create_glissade(self,current_date, last_service_sate, current_mileage, last_service_mileage) -> Car:
        pass
    
    @abstractmethod
    def create_palindrom(current_date, last_service_date, warning_light_on)-> Car:
        pass
    
    @abstractmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        pass
    
    @abstractmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        pass