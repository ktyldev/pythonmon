import ConfigParser

from Constants import Constants

class Configuration:
	config = ConfigParser.RawConfigParser()
	config.read(Constants.CONFIG_PATH)

	# DISPLAY
	screen_width = int(config.get('Display', 'width'))
	screen_height = int(config.get('Display', 'height'))
	layer_limit = int(config.get('Display', 'layerlimit'))
	fps = int(config.get('Display', 'fps'))

	# ENGINE
	event_loop_multiplier = int(config.get('Engine', 'event_loop_multiplier'))
	tile_size = int(config.get('Engine', 'tile_size'))
