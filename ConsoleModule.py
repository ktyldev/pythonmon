import configuration
import gui
from logger import Logger
import scenemodule


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
        scene_exists = scenemodule.SceneManager.check_if_scene_exists(scene_name)

        # load scene data if it exists, otherwise create a new one
        if scene_exists:
            scenemodule.SceneManager.load_scene(args[0])
        else:
            Logger.log('New scene: ' + scene_name)

        scenemodule.SceneManager.scene.start()
        Logger.log('Scene loaded: ' + scene_name)


        screen_size = configuration.editor_width, configuration.editor_height

        gui = gui.Gui(screen_size, configuration.layer_limit)
        gui.draw()