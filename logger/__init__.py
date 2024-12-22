import logging
from datetime import datetime
import os


class CustomLogger:
    """Custom logger class to handle logging with a timestamped log file."""

    def __init__(self):
        self.log_dir = 'logs'

        os.makedirs(self.log_dir, exist_ok=True)

        current_time_stamp = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"

        self.log_file_name = f"log_{current_time_stamp}.log"

        self.log_file_path = os.path.join(self.log_dir, self.log_file_name)

        logging.basicConfig(
            filename=self.log_file_path,
            filemode="w",
            format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
            level=logging.INFO
        )

        self.logger = logging.getLogger(__name__)

    def get_logger(self):
        """Returns the logger instance"""
        return self.logger