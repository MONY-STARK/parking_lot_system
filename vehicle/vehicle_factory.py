from vehicle.vehicle import Car, MotorBike, Truck

class VehicleFactory:

    VEHICLE_MAP = {
        "car": Car,
        "motorbike": MotorBike,
        "truck": Truck
    }

    @staticmethod
    def create_vehicle(vehicle_type: str):

        vehicle_type = vehicle_type.lower()

        if vehicle_type not in VehicleFactory.VEHICLE_MAP:
            raise ValueError("Invalid vehicle type")

        return VehicleFactory.VEHICLE_MAP[vehicle_type]()