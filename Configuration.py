import configparser
import Constants

config = configparser.RawConfigParser()
config.read(Constants.CONFIG_PATH)

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

# LOGGING
log_all = int(config.get('Logging', 'all')) == 1

# FILE PATHS
scene_data_folder_path = config.get('File Paths', 'scene_data_folder_path')
