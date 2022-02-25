class OctoprimeTire(object):
    def __init__(self, tire_status):
        self.tire_status = tire_status
        
    def needs_service(self):
        sumValue = 0
        for i in range(len(self.tire_status)):
           sumValue += self.tire_status[i]
        return sumValue >= 3