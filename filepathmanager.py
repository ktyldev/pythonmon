import os

resources = '_Resources'
data = 'Data'
images = 'Images'
sprites = 'sprites'

_data_path = os.path.join(resources, data)
_images_path = os.path.join(resources, images)
_sprites_path = os.path.join(_images_path, sprites)

def get_data_path(data_folder):
    return os.path.join(_data_path, data_folder)

def get_sprite(sprite_name):
    return os.path.join(_sprites_path, sprite_name)