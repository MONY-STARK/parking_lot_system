
from parking_system import ParkingSystem
import time


if __name__ == "__main__":

    mall_parking = ParkingSystem(2, 1, 2)
    mall_parking.entry("car")
    mall_parking.entry("motorbike")
    mall_parking.entry("truck")
    mall_parking.entry("motorbike")

    time.sleep(4 * 60)

    mall_parking.exit(102)


