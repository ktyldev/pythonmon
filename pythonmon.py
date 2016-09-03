import argparse

from menu import *


parser = argparse.ArgumentParser(description='Pythonmon game engine')
parser.add_argument('-l', action='store_true', help='enable logging')
args = parser.parse_args()

# set logging state
logger.enabled = args.l

logger.log('Program started')

start_menu = ConsoleMenu.from_data('start-menu')

start_menu.run()


