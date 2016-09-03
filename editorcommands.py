import sys
import game_loop
import jsonmanager
import logger

from consolemodule import Console


class ConsoleMenu:

    MENU_DATA_FILE_PATH = '_Resources/Data/MenuData/'

    class ConsoleMenuItem:
        def __init__(self, text, action):
            self.text = text
            self.action = action

        def invoke(self):
            try:
                getattr(sys.modules[__name__], self.action)()
            except AttributeError:
                logger.log(self.action + ' is not recognised.')

    @staticmethod
    def from_data(name):
        path = ConsoleMenu.MENU_DATA_FILE_PATH + name + '.json'
        data = jsonmanager.get_data(path)

        title = data['Title']
        item_data = data['Items']
        args = []
        for item_datum in item_data:
            args.append((item_datum['Text'], item_datum['Action']))

        return ConsoleMenu(title, args)

    def __init__(self, title, args):
        self.title = title
        self.menu_items = []

        for argument in args:
            self.add_menu_item(argument[0], argument[1])

    def add_menu_item(self, text, action):
        self.menu_items.append(ConsoleMenu.ConsoleMenuItem(text, action))

    def get_menu_item(self, index):
        return self.menu_items[index]

    def display_menu_item(self, index):
        menu_item = self.get_menu_item(index)
        print('[' + str(index) + '] - ' + menu_item.text)

    def run(self):
        for index in range(0, len(self.menu_items)):
            self.display_menu_item(index)

        result = input('Choose an option: ')

        self.get_menu_item(int(result)).invoke()


def print_help():
    print('help')


def run_editor():
    loop = game_loop.TestLoop()
    loop.set_scene('pallet-town')
    loop.run()


def run_game():
    loop = game_loop.DefaultGameLoop()
    loop.set_scene('pallet-town')
    loop.run()


def start_console():
    console = Console()
    console.run()
