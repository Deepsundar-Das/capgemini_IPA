from signals.base_signal import Traffic_signal
from app_logger import logger
from config import(
    HIGHWAY_HIGH_GREEN_TIME,
    HIGHWAY_LOW_GREEN_TIME,
    HIGHWAY_SIGNAL_TRAFFIC_LIMIT
)

class HighwaySignal(Traffic_signal):
    def green_time(self):
        logger.info(f"calculating green time for highway signal...")
        if self._vehicle_count < HIGHWAY_SIGNAL_TRAFFIC_LIMIT:
            return HIGHWAY_LOW_GREEN_TIME
        return HIGHWAY_HIGH_GREEN_TIME

    def signal_type(self):
        return "Highway Signal"