from vehicle.vehicle import Car, MotorBike, Truck

class VehicleFactory:

    VEHICLE_MAP = {
        "car": Car,
        "motorbike": MotorBike,
        "truck": Truck
    }

    @classmethod
    def create_vehicle(cls, vehicle_type: str):
        vehicle_type = vehicle_type.lower()
        if vehicle_type not in cls.VEHICLE_MAP:
            raise ValueError("Invalid vehicle type")
        return cls.VEHICLE_MAP[vehicle_type]()