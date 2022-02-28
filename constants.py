"""Maintaining Test Scripts related constants"""

import configparser
import os

import pytest_orion.constant as constants

BASE_DIR_PATH = os.path.abspath(os.path.dirname(__file__))
constants.SCREENSHOT_BASE_DIR = BASE_DIR_PATH

config = configparser.ConfigParser()
ini_file = os.path.join(BASE_DIR_PATH, 'config.ini')
config.read(ini_file)


URL = config.get('WEB', 'url')
BROWSER = config.get('WEB', 'browser')
