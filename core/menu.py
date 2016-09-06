import sys

from core import loop
from util import jsonmanager, logger


def make_console_menu(name):
    menu_data_file_path = '_Resources/Data/MenuData/'

    path = menu_data_file_path + name + '.json'
    data = jsonmanager.get_data(path)

    title = data['Title']
    item_data = data['Items']
    args = []
    for item_datum in item_data:
        args.append((item_datum['Text'], item_datum['Action']))

    return ConsoleMenu(title, args)


class ConsoleMenuItem:
    def __init__(self, text, action):
        self.text = text
        self.action = action

    def invoke(self):
        try:
            getattr(sys.modules[__name__], self.action)()
        except AttributeError:
            logger.log(self.action + ' is not recognised.')


class ConsoleMenu:
    def __init__(self, title, args):
        self.title = title
        self.menu_items = []

        for argument in args:
            self.add_menu_item(argument[0], argument[1])

    def add_menu_item(self, text, action):
        self.menu_items.append(ConsoleMenuItem(text, action))

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


def run_loop(game_loop):
    game_loop.set_scene('pallet-town')
    game_loop.run()


def run_editor():
    run_loop(loop.TestLoop())


def run_game():
    run_loop(loop.DefaultGameLoop())
