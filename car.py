'''
from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self):
        pass
'''
from abc import ABC, abstractmethod
from serviceable import Serviceable

class Car(Serviceable, ABC):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery
        
    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()
