from Logger import Logger
from EditorCommands import *

Logger.log('Program started')

def run_editor():
    menu = ConsoleMenu('main menu')
    help_menu_item = ConsoleMenu.ConsoleMenuItem('show help', 'help')
    run_game_menu_item = ConsoleMenu.ConsoleMenuItem('run game', 'run_game')
    menu.add_menu_item(help_menu_item)
    menu.add_menu_item(run_game_menu_item)
    menu.run()

run_editor()
