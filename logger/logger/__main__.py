import logging
from colorama import Fore, Style, init

# Create a custom formatter with colors
class CustomFormatter(logging.Formatter):
    # Define color codes for different log levels
    FORMAT = {
        logging.DEBUG: Fore.BLUE
        + "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        + Style.RESET_ALL,
        logging.INFO: Fore.GREEN
        + "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        + Style.RESET_ALL,
        logging.WARNING: Fore.YELLOW
        + "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        + Style.RESET_ALL,
        logging.ERROR: Fore.RED
        + "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        + Style.RESET_ALL,
        logging.CRITICAL: Fore.RED
        + Style.BRIGHT
        + "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        + Style.RESET_ALL,
    }

    def format(self, record):
        log_fmt = self.FORMAT.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


if __name__ == "__main__":
    #############################################################
    # Logging code
    #############################################################
    # Initialize colorama
    init()

    # Step 2: Create a logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Step 3: Create a handler that outputs to stdout
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)

    # Step 4. Apply the custom formatter to the handler
    handler.setFormatter(CustomFormatter())

    # Step 5: Add the handler to the logger
    logger.addHandler(handler)
    #############################################################
    
    logger.info(f"Hello from {__file__}")