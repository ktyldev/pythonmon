import sys

class ConsoleMenu:
    class ConsoleMenuItem:
        def __init__(self, text, action):
            self.text = text
            self.action = action

        def invoke(self):
            try:
                getattr(sys.modules[__name__], self.action)()
            except AttributeError:
                print(self.action + ' is not recognised.')

    def __init__(self, title):
        self.title = title
        self.menu_items = []

    def add_menu_item(self, menu_item):
        self.menu_items.append(menu_item)

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

def help():
    print('help')