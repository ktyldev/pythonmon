from Logger import Logger
from EditorCommands import *

Logger.log('Program started')

def run_editor():
    start_menu = ConsoleMenu.from_data('start-menu')
    while True:
        start_menu.run()

run_editor()
