import controller.component
from util import jsonmanager, debug, configuration
from view.entity import Entity


class Scene:
    def __init__(self, name, entities_data):
        self.name = name
        self.entities = []
        self.started_entities = []
        self.event_input = None
        self.cont_input = None

        for entity_data in entities_data:
            position = (entity_data["X"], entity_data["Y"])

            entity = Entity(entity_data["Name"], position)
            for component_data in entity_data["Components"]:
                try:
                    component_constructor = getattr(controller.component, component_data["Type"])
                    component = component_constructor()
                    component.scene = self

                    data = component_data["ComponentData"]
                    if not len(data) == 0:
                        component.load_data(data)

                    entity.add_component(component)
                except AttributeError:
                    debug.log(component_data["Type"] + " not recognised :/")

            self.entities.append(entity)

    def start(self):
        self.event_input = 'none'
        self.cont_input = 'none'

        while not self.ready_to_start():
            debug.log('preparing to start entities...')
            entities_to_start = []
            for ent in self.entities:
                if not ent.is_started():
                    entities_to_start.append(ent)
            debug.log(str(len(entities_to_start)) + ' entities ready to start.')

            debug.log('starting...')
            for entity in entities_to_start:
                try:
                    entity.start()
                except Exception as e:
                    debug.log('could not start entity. Logging error:')
                    debug.log(e)

        log_string = str.format('started {0} entities :)', len(self.entities))
        debug.log(log_string)

    def update(self, event_input, cont_input):
        self.event_input = event_input
        self.cont_input = cont_input
        for entity in self.entities:
            entity.update()

    def find_entity(self, entity_name):
        for entity in self.entities:
            if entity.name == entity_name:
                return entity
        return None

    def add_entity(self, entity):
        self.entities.append(entity)

    def ready_to_start(self):
        for entity in self.entities:
            if not entity.is_started():
                return False
        return True


class SceneManager:
    @staticmethod
    def get_path(scene_name):
        return configuration.scene_data_folder_path + scene_name + '.json'

    @staticmethod
    def load_scene(scene_name):
        path = SceneManager.get_path(scene_name)
        scene_data = jsonmanager.get_data(path)

        return Scene(scene_name, scene_data['Entities'])

    @staticmethod
    def check_if_scene_exists(scene_name):
        path = SceneManager.get_path(scene_name)

        return jsonmanager.check_for_file(path)
