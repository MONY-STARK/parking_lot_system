
from vehicle_data import VehicleData
from parking_ground import ParkingGround

class ParkingSystem:

    def __init__(self, compact_spots, regular_spots, oversized_spots):
        self.active_vehicles = VehicleData()
        self.parking_ground = ParkingGround(compact_spot=compact_spots,
                                            regular_spot= regular_spots, 
                                            oversized_spot= oversized_spots)
        
    
    def entry(self):
        self.parking_ground.entry()