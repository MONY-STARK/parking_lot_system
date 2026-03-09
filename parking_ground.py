
from vehicle.vehicle_factory import VehicleFactory
from vehicle.vehicle import Vehicle
from enums.parkinglot_enums import ParkingType
from enums.vehicle_enums import VehicleType
import time


class ParkingGround:

    def __init__(self, compact_spot, regular_spot, oversized_spot):
        self.compact_spot = compact_spot
        self.regular_spot = regular_spot
        self.oversized_spot = oversized_spot

        self.ticket_number = 100



    def entry(self, vehicle_type):
        vehicle = VehicleFactory.create_vehicle(vehicle_type=vehicle_type)
        if not self._check_available_spot(vehicle):
            raise ValueError("Parking full")
        self._assign_spot(vehicle)
        ticket = self._generate_ticket()
        return vehicle, ticket

    def exit(self, vehicle : Vehicle ):
        exit_time = self.calculate_exit_time()
        vehicle.exit_time = exit_time
        fee = self.calculate_fee(vehicle.entry_time, vehicle.exit_time)
        self.update_spot(vehicle)
        return fee

    def calculate_exit_time(self):
        return time.time()

    def calculate_fee(self, entry_time, exit_time):
        duration = (exit_time - entry_time) / 3600
        return 50 * duration
    
    def update_spot(self, vehicle : Vehicle):
        spot = vehicle.spot_assign

        if spot == ParkingType.COMPACT:
            self.compact_spot += 1
        elif spot == ParkingType.REGULAR:
            self.regular_spot += 1
        elif spot == ParkingType.OVERSIZED:
            self.oversized_spot += 1

    def _assign_spot(self, vehicle : Vehicle):

        if vehicle.VEHICLE_TYPE == VehicleType.CAR:
            vehicle.spot_assign = ParkingType.REGULAR
            self.regular_spot -= 1
        elif vehicle.VEHICLE_TYPE == VehicleType.MOTORBIKE:
            vehicle.spot_assign = ParkingType.COMPACT
            self.compact_spot -= 1
        elif vehicle.VEHICLE_TYPE == VehicleType.TRUCK:
            vehicle.spot_assign = ParkingType.OVERSIZED
            self.oversized_spot -= 1

        
        
    def _check_available_spot(self, vehicle: Vehicle):

        if vehicle.VEHICLE_TYPE == VehicleType.CAR:
            return self.regular_spot > 0

        elif vehicle.VEHICLE_TYPE == VehicleType.MOTORBIKE:
            return self.compact_spot > 0

        elif vehicle.VEHICLE_TYPE == VehicleType.TRUCK:
            return self.oversized_spot > 0

        return False


    def _generate_ticket(self):        
        self.ticket_number += 1
        return self.ticket_number