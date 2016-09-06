import configparser

config = configparser.RawConfigParser()
config.read('_config.cfg')

# EDITOR
editor_width = int(config.get('Editor', 'width'))
editor_height = int(config.get('Editor', 'height'))

# DISPLAY
screen_width = int(config.get('Display', 'width'))
screen_height = int(config.get('Display', 'height'))
layer_limit = int(config.get('Display', 'layer_limit'))
fps = int(config.get('Display', 'fps'))

# ENGINE
event_loop_multiplier = int(config.get('Engine', 'event_loop_multiplier'))
tile_size = int(config.get('Engine', 'tile_size'))
clock_tick = event_loop_multiplier * fps

# FILE PATHS
scene_data_folder_path = config.get('File Paths', 'scene_data_folder_path')
input_config_path = config.get('File Paths', 'input_config_path')
