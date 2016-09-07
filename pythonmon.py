import argparse

from core import menu
from util import debug

parser = argparse.ArgumentParser(description='Pythonmon game engine')
parser.add_argument('-l', action='store_true', help='enable logging')
args = parser.parse_args()

# set logging state
debug.enabled = args.l

debug.log('Program started')

start_menu = menu.make_console_menu('start-menu')

start_menu.run()


