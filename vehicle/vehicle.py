import time
from enums.vehicle_enums import VehicleType

class Vehicle:

    VEHICLE_ID = 0
    VEHICLE_TYPE = None

    def __init__(self):
        Vehicle.VEHICLE_ID += 1
        self.vehicle_id = Vehicle.VEHICLE_ID
        self.entry_time = time.time()
        self.exit_time = None
        self.spot_assign = None
    
    @property
    def vechile_id(self):
        return self.vechile_id
    
    @property
    def exit_time(self):
        return self.exit_time
    
    @exit_time.setter
    def exit_time(self, value):
        if value is not None and value < self.entry_time:
            raise ValueError("exit time cannot be earlier than entry time")
        self.exit_time = value


class Car(Vehicle):
    VEHICLE_TYPE = VehicleType.CAR


class MotorBike(Vehicle):
    VEHICLE_TYPE = VehicleType.MOTORBIKE


class Truck(Vehicle):
    VEHICLE_TYPE = VehicleType.t