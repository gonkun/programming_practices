#!/usr/bin/env python3

import logging
import os
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {
        'BASE_FORMAT': {
            'format': '[%(name)s][%(levelname)-6s] %(message)s'
        },
        'FILE_FORMAT': {
            'format': '[%(asctime)s [%(name)s][%(levelname)-6s] %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'BASE_FORMAT'
        },
        'file': {
            'class': 'logging.FileHandler',
            'level': 'DEBUG',
            'formatter': 'FILE_FORMAT'
        }
    },
    'root': {
        'level': 'INFO',
        'handlers': ['console', 'file']
    }
})

# BASE_FORMAT = "[%(name)s][%(levelname)-6s] %(message)s"
# FILE_FORMAT = "[%(asctime)s]" + BASE_FORMAT

# root_logger = logging.getLogger()
# root_logger.setLevel(logging.DEBUG)

# try:
#     file_logger = logging.FileHandler('application.log')
# except (OSError, IOError):
#     file_logger = logging.FileHandler('/tmp/application.log')

# file_logger.setLevel(logging.INFO)
# file_logger.setFormatter(logging.Formatter(BASE_FORMAT))
# root_logger.addHandler(file_logger)

# console_logger = logging.StreamHandler()
# console_logger.setFormatter(BASE_FORMAT)
# console_logger.setLevel(logging.WARNING)
# root_logger.addHandler(console_logger)

# logger = logging.getLogger()
# logger.warning('this is an info message from the root logger')

# app_logger = logging.getLogger('my-app')
# app_logger.warning('an info message from my-app')
