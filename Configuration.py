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
	draw_tiles = int(config.get('Display', 'draw_tiles')) == 1

	# ENGINE
	event_loop_multiplier = int(config.get('Engine', 'event_loop_multiplier'))
	tile_size = int(config.get('Engine', 'tile_size'))

	#LOGGING
	log_all = int(config.get('Logging', 'all')) == 1
	log_gui = int(config.get('Logging', 'gui')) == 1
