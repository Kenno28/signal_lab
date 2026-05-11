import logging

class AppLogger:
    """
    Simple wrapper around Python's logging module.

    Creates a logger with console output and optional file output.
    """

    def __init__(self,name: str, level: int = logging.DEBUG) -> None:
        """
        Initialize the logger.

        Args:
            name (str): Name of the logger.
            level (int, optional): Logging level. Defaults to logging.INFO.
        """
    

        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self.logger.propagate = False

        # Prevent duplicate handlers if the logger is created multiple times
        if not self.logger.handlers:
            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )

            console_handler = logging.StreamHandler()
            console_handler.setLevel(level)
            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)

    def debug(self, message: str) -> None:
        self.logger.debug(f"{message}")

    def info(self, message: str) -> None:
        self.logger.info(f"{message}")

    def warning(self, message: str) -> None:
        self.logger.warning(f"{message}")

    def error(self, message: str) -> None:
        self.logger.error(f"{message}")

    def critical(self, message: str) -> None:
        self.logger.critical(f"{message}")