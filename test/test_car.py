import unittest
from datetime import datetime
import imp
import sys

#import sys
#sys.path.append('C:/Users/Michealvitalis/Documents/temp1/forage_lyft_starter/src/carImplFactory.py')
#import carImplFactory
class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        current_mileage = 0
        last_service_mileage = 0
        tire_type = "Carrigan"
        tire_status = [0, 0.3, 0.9, 0.9]
        carFactory = carImplFactory.CarImplFactory();
        calliope = carFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage, tire_type, tire_status)
        self.assertTrue(calliope.needs_service())
        
    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        tire_type = "Octoprime"
        tire_status = [0.5, 0.5, 0.5, 0.5]
        carFactory = carImplFactory.CarImplFactory();
        calliope = carFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage, tire_type, tire_status)
        self.assertFalse(calliope.needs_service())
        
    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        tire_type = "Octoprime"
        tire_status = [0.9, 0.5, 0.5, 0.5]
        carFactory = carImplFactory.CarImplFactory();
        calliope = carFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage, tire_type, tire_status)
        self.assertTrue(calliope.needs_service())
        
    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 30000
        last_service_mileage = 0
        tire_type = "Carrigan"
        tire_status = [0.5, 0.5, 0.5, 0.5]
        carFactory = carImplFactory.CarImplFactory();
        calliope = carFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage, tire_type, tire_status)
        self.assertFalse(calliope.needs_service())

        
class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        current_mileage = 0
        last_service_mileage = 0
        tire_type = "Carrigan"
        tire_status = [0.5, 0.5, 0.5, 0.5]
        carFactory = carImplFactory.CarImplFactory();
        car = carFactory.create_glissade(today, last_service_date, current_mileage, last_service_mileage, tire_type, tire_status)
        self.assertTrue(car.needs_service())
        
    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        tire_type = "Octoprime"
        tire_status = [0.4, 0.5, 0.1, 0.5]
        carFactory = carImplFactory.CarImplFactory();
        car = carFactory.create_glissade(today, last_service_date, current_mileage, last_service_mileage, tire_type, tire_status)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year-1)
        current_mileage = 60001
        last_service_mileage = 0
        tire_type = "Octoprime"
        tire_status = [0.4, 0.5, 0.1, 0.5]
        carFactory = carImplFactory.CarImplFactory();
        car = carFactory.create_glissade(today, last_service_date, current_mileage, last_service_mileage, tire_type, tire_status)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        tire_type = "Octoprime"
        tire_status = [0.4, 0.5, 0.1, 0.5]
        carFactory = carImplFactory.CarImplFactory();
        car = carFactory.create_glissade(today, last_service_date, current_mileage, last_service_mileage, tire_type, tire_status)
        self.assertFalse(car.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        warning_light_is_on = False
        tire_type = "Carrigan"
        tire_status = [0.9, 0.5, 0.1, 0.5]
        carFactory = carImplFactory.CarImplFactory();
        car = carFactory.create_palindrome(today, last_service_date, warning_light_is_on, tire_type, tire_status)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        warning_light_is_on = False
        tire_type = "Carrigan"
        tire_status = [0.1, 0.5, 0.1, 0.5]
        carFactory = carImplFactory.CarImplFactory();
        car = carFactory.create_palindrome(today, last_service_date, warning_light_is_on, tire_type, tire_status)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        warning_light_is_on = True
        tire_type = "Octoprime"
        tire_status = [0.9, 0.5, 0.1, 0.5]
        carFactory = carImplFactory.CarImplFactory();
        car = carFactory.create_palindrome(today, last_service_date, warning_light_is_on, tire_type, tire_status)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        warning_light_is_on = False
        tire_type = "Octoprime"
        tire_status = [0.4, 0.5, 0.1, 0.5]
        carFactory = carImplFactory.CarImplFactory();
        car = carFactory.create_palindrome(today, last_service_date, warning_light_is_on, tire_type, tire_status)
        self.assertFalse(car.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        tire_type = "Octoprime"
        tire_status = [0.9, 0.5, 0.1, 0.5]
        carFactory = carImplFactory.CarImplFactory();
        car = carFactory.create_thovex(today, last_service_date, current_mileage, last_service_mileage, tire_type, tire_status)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        tire_type = "Octoprime"
        tire_status = [0.3, 0.5, 0.1, 0.5]
        carFactory = carImplFactory.CarImplFactory();
        car = carFactory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage, tire_type, tire_status)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        tire_type = "Carrigan"
        tire_status = [0.9, 0.5, 0.1, 0.5]
        carFactory = carImplFactory.CarImplFactory();
        car = carFactory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage, tire_type, tire_status)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        tire_type = "Carrigan"
        tire_status = [0.3, 0.5, 0.1, 0.5]
        carFactory = carImplFactory.CarImplFactory();
        car = carFactory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage, tire_type, tire_status)
        self.assertFalse(car.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        tire_type = "Octoprime"
        tire_status = [0.5, 0.5, 0.1, 0.5]
        carFactory = carImplFactory.CarImplFactory();
        car = carFactory.create_thovex(today, last_service_date, current_mileage, last_service_mileage, tire_type, tire_status)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        tire_type = "Octoprime"
        tire_status = [0.5, 0.5, 0.1, 0.5]
        carFactory = carImplFactory.CarImplFactory();
        car = carFactory.create_thovex(today, last_service_date, current_mileage, last_service_mileage, tire_type,tire_status)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        tire_type = "Octoprime"
        tire_status = [0.5, 0.5, 0.1, 0.5]
        carFactory = carImplFactory.CarImplFactory();
        car = carFactory.create_thovex(today, last_service_date, current_mileage, last_service_mileage, tire_type, tire_status)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        tire_type = "Octoprime"
        tire_status = [0.5, 0.5, 0.1, 0.5]
        carFactory = carImplFactory.CarImplFactory();
        car = carFactory.create_thovex(today, last_service_date, current_mileage, last_service_mileage, tire_type, tire_status)
        self.assertFalse(car.needs_service())


class CarriganTest(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        warning_light_is_on = False
        tire_type = "Carrigan"
        tire_status = [0.9, 0.5, 0.1, 0.5]
        carFactory = carImplFactory.CarImplFactory();
        car = carFactory.create_palindrome(today, last_service_date, warning_light_is_on, tire_type, tire_status)
        self.assertTrue(car.needs_service())
        
    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        warning_light_is_on = False
        tire_type = "Carrigan"
        tire_status = [0.1, 0.8, 0.1, 0.5]
        carFactory = carImplFactory.CarImplFactory();
        car = carFactory.create_palindrome(today, last_service_date, warning_light_is_on, tire_type, tire_status)
        self.assertTrue(car.needs_service())
    
class OctoprimeTest(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        tire_type = "Octoprime"
        tire_status = [0.9, 0.9, 0.8, 0.5]
        carFactory = carImplFactory.CarImplFactory();
        car = carFactory.create_thovex(today, last_service_date, current_mileage, last_service_mileage, tire_type, tire_status)
        self.assertTrue(car.needs_service())
        
    def test_tire_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        tire_type = "Octoprime"
        tire_status = [0.5, 0.5, 0.1, 0.5]
        carFactory = carImplFactory.CarImplFactory();
        car = carFactory.create_thovex(today, last_service_date, current_mileage, last_service_mileage, tire_type, tire_status)
        self.assertFalse(car.needs_service())

if __name__ == '__main__':
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
    from src import carImplFactory
    unittest.main()
