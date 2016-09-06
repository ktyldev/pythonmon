import argparse

from core import menu
from util import logger

parser = argparse.ArgumentParser(description='Pythonmon game engine')
parser.add_argument('-l', action='store_true', help='enable logging')
args = parser.parse_args()

# set logging state
logger.enabled = args.l

logger.log('Program started')

start_menu = menu.make_console_menu('start-menu')

start_menu.run()


