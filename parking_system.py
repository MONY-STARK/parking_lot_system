
from vehicle_data import VehicleData
from parking_ground import ParkingGround

class ParkingSystem:

    def __init__(self, compact_spots, regular_spots, oversized_spots):
        self.active_vehicles = VehicleData()
        self.parking_ground = ParkingGround(compact_spot=compact_spots,
                                            regular_spot= regular_spots, 
                                            oversized_spot= oversized_spots)
        
    
    def entry(self, vehicle_type):
        vehicle, ticket = self.parking_ground.entry(vehicle_type)
        self.active_vehicles.add(ticketId=ticket, data=vehicle)
        print(f"Your Ticket ID {ticket}")

    
    def exit(self, ticket_id):
        vehicle_data = self.active_vehicles.get_data(ticket_id)
        fee = self.parking_ground.exit(vehicle_data)
        print(f"Amount to Paid is {fee} rupees")