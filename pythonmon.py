from editorcommands import *
import argparse

Logger.log('Program started')

parser = argparse.ArgumentParser(description='Pythonmon game engine')
parser.add_argument('--foo', help='foo help')
args = parser.parse_args()

start_menu = ConsoleMenu.from_data('start-menu')

start_menu.run()


