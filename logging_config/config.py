import logging.config


config_dict = {
    'formatters': {
        'my_formatter': {
            'format': '%(funcName)-20s %(levelname)-15s %(name)-18s %(message)s',
            'datefmt': None,
            'validate': True
        }
    },
    'filters': {},
    'handlers': {
        'stream_handler': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'my_formatter',
            'filters': []
        },
    },
    'loggers': {
        'my_logger': {
            'level': 'DEBUG',
            'filters': [],
            'handlers': ['stream_handler'],
        },
        'info_logger': {
            'level': 'INFO',
            'filters': [],
            'handlers': ['stream_handler']
        }
    },
    'root': {},
    'disable_existing_loggers': True,
    'version': 1,
}

logging.config.dictConfig(config_dict)


# Example for capturing stack traces in logs while exception handling:
#
# try:
#   c = a / b
# except Exception as e:
#   logging.error("Exception occurred", exc_info=True)
