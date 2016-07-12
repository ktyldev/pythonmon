from Logger import Logger
from EditorCommands import *

Logger.log('Program started')

def run_editor():
    ConsoleMenu.from_data('start-menu').run()

run_editor()
