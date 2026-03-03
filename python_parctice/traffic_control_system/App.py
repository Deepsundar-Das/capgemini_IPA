from signals.city_signal import CitySignal
from signals.highway_signal import HighwaySignal
from controller.controller import signalController
from app_logger import logger

logger.info(f"Traffic simulation started...")
controller = signalController()
no_vehicle = int(input("enter number of vehicles: "))
city_signal = CitySignal(no_vehicle)
highway_signal = HighwaySignal(HighwaySignal)

controller.operate(city_signal)
controller.operate(highway_signal)
logger.info("simulation completed")
