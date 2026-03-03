from signals.base_signal import Traffic_signal
from app_logger import logger
from config import(
    CITY_HIGH_GREEN_TIME,
    CITY_LOW_GREEN_TIME,
    CITY_SIGNAL_TRAFFIC_LIMIT
)

class CitySignal(Traffic_signal):
    def green_time(self):
        logger.info(f"calculating green time for highway signal...")
        if self._vehicle_count < CITY_SIGNAL_TRAFFIC_LIMIT:
            return CITY_LOW_GREEN_TIME
        return CITY_HIGH_GREEN_TIME

    def signal_type(self):
        return "Highway Signal"