
class CarriganTire(object):
    def __init__(self, tire_status):
        self.tire_status = tire_status
        
    def needs_service(self):
        for i in range(len(self.tire_status)):
            if self.tire_status[i] > 0.9:
                return True
        return False