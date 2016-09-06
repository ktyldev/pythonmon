"""
COMPONENT USAGE

This is where all game logic is defined. Components should only update themselves and the entity they are attached
to. On rare occasions it may be necessary to access other components from inside a component's update method. This
should be achieved via ```self.scene.find_entity(%entity_name%).get_component(%component_name%)```.

Components have parameter-less constructors, two override-able parameter-less methods and one override-able
method with a single parameter.

Component()

Every component should have a parameter-less constructor defined.

component.update()

This method will be called once per tick. It is used to update the state of the Component and the entity to which
the component is attached.

component.start()

This method is called once at the start of the scene. It is used to prepare the state of the component using data
that is only available at runtime.

component.load_data(data)

This method is called before the start of the scene. It is used to load data from the scene JSON file. The data is
an array which can be used with index arguments to assign data to class members.
"""


class Component:
    """
    generic base class for defining entity behaviour
    """
    List = []

    @staticmethod
    def find(tag):
        for component in Component.List:
            if component.tag == tag:
                return component
        return None

    def __init__(self):
        self.scene = None
        self.enabled = True
        self.tag = ''
        self.entity = None
        self.started = False
        Component.List.append(self)

    def start(self):
        """
        called at the start of the scene
        :return:
        """
        self.started = True
        return

    def update(self):
        """
        called once per tick
        :return:
        """
        return

    def load_data(self, data_array):
        """
        assign data to a class instance before starting scene
        :param data_array: an array of data to initialise the component with
        :return:
        """
        return
