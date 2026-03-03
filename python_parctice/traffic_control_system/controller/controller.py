from app_logger import logger

class signalController:
    def operate(self, signal):
        logger.info(f"signal controller stated for {signal.signal_type()}")
        time = signal.green_time()
        logger.info(f"{signal.signal_type()} --> greeen for {time} seconds...")
        logger.info(f"signal controller operation completed")
