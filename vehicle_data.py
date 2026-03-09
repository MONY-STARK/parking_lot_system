
from vehicle.vehicle import Vehicle

class VehicleData:

    def __init__(self):
        self.data = {}

    def add(self, ticketId, data:Vehicle):
        self.data[ticketId] = data

    def get_data(self, ticketId):
        return self.data[ticketId]