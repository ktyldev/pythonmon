import logger


class Console:
    def __init__(self):
        self.running = True

    def run(self):
        while self.running:
            command = input('> ')
            self.interpret_command(command)

    def interpret_command(self, command):
        split_command = str(command).split()
        verb = split_command[0]
        args = []
        for item in split_command:
            if not item == verb:
                args.append(item)

        try:
            command_to_run = getattr(self, verb)
            command_to_run(args)
        except AttributeError:
            logger.log(verb + ' not recognised or arguments invalid.')

    def exit(self):
        self.running = False
