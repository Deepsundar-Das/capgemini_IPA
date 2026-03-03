from abc import ABC,abstractmethod
from app_logger import logger

class Traffic_signal(ABC):

    def __init__(self, vehicle_count):
        self._vehicle_count = vehicle_count
        logger.info(f"Traffic signal created with vehicle count = {vehicle_count}")

    @abstractmethod
    def green_time(self):
        pass

    @abstractmethod
    def signal_type(self):
        pass