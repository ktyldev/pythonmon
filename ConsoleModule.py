from Logger import Logger
import SceneModule


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
            Logger.log(verb + ' not recognised or arguments invalid.')

    def exit(self, args):
        self.running = False

    def scene(self, args):
        scene_name = args[0]
        scene_exists = SceneModule.SceneManager.check_if_scene_exists(scene_name)

        if scene_exists:
            SceneModule.SceneManager.load_scene(args[0])
        else:
            Logger.log('New scene: ' + scene_name)
        Logger.log('Scene loaded: ' + scene_name)