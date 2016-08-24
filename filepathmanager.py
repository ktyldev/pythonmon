import os

resources = '_Resources'
data = 'Data'
images = 'Images'

_data_path = os.path.join(resources, data)
_images_path = os.path.join(resources, images)


def get_data_path(data_folder):
    return os.path.join(_data_path, data_folder)
