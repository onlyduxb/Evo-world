"""Set up logger."""

import logging.config

def setup_logger(file_name: str = "debugger") -> None:
    """setup_logger sets up logger.

    Parameters
    ----------
    file_name : str, optional
        File name to save to, file extension (log) already included, by default "debugger".

    """
    logging.config.dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "standard": {
                    "format": "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
                }
            },
            "handlers": {
                "file": {
                    "class": "logging.FileHandler",
                    "filename": file_name + ".log",
                    "mode": "w",  # use 'a' to append
                    "formatter": "standard",
                    "level": "INFO",
                }
            },
            "root": {
                "handlers": ["file"],
                "level": "INFO",
            },
        }
    )