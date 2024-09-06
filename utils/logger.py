import logging

def setup_logger(log_file="app.log"):
    """Sets up the logging configuration."""
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    logging.info("Logger initialized")

def log_event(event_message):
    """Logs a specific event with an informational message."""
    logging.info(event_message)

def log_error(error_message):
    """Logs an error message."""
    logging.error(error_message)
