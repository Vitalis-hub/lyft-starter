from .carriganTire import CarriganTire
from .octoprimeTire import OctoprimeTire

class TireImplementationService(object):
    
    def __init__(self, tire_type, tire_status):
        self.tire_type = tire_type
        self.tire_status = tire_status
        if self.tire_type == "Carrigan":
            self.tire = CarriganTire(tire_status)
            
        if self.tire_type == "Octoprime":
            self.tire = OctoprimeTire(tire_status)
            
    def needs_service(self):
        return self.tire.needs_service()
            
    

    