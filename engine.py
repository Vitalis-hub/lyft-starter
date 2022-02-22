from abc import ABC, abstractmethod
from car import Car
class Engine(ABC):
    
    @abstractmethod
    def needs_service():
        pass