import os
import logging

class Logger:

    @staticmethod
    def log_init():
        # Get the directory of the current file
        current_file_directory = os.path.dirname(__file__)
        # Get the parent directory of the current file's directory
        parent_directory = os.path.dirname(current_file_directory)
        # Create the log folder in the parent directory
        log_folder = os.path.join(parent_directory, 'Logger')
        os.makedirs(log_folder, exist_ok=True)
        # Define the log file path in the new log folder
        log_file = os.path.join(log_folder, 'logger.log')

        # Configure logging
        logging.basicConfig(
            filename=log_file,
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s'
        )

        # Adding the logger separator
