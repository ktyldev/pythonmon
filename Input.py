import pygame
import sys

class InputData:
	def __init__(self, action, pressed):
		self.action = action
		self.pressed = pressed

class InputType:
	A = 0
	B = 1
	START = 2
	SELECT = 3
	LEFT = 4
	UP = 5
	RIGHT = 6
	DOWN = 7
	NONE = 8

class InputHandler:
	@staticmethod
	def get_input_state(event_type):
		if event_type == pygame.KEYDOWN:
			return 'down'
		elif event_type == pygame.KEYUP:
			return 'up'
		else:
			return 'none'
		
	@staticmethod
	def get_input_type(event_key):
		result = InputType.NONE

		if event_key == pygame.K_z:
			result = InputType.A
		elif event_key == pygame.K_x:
		    result = InputType.B
		elif event_key == pygame.K_c:
		    result = InputType.START
		elif event_key == pygame.K_v:
		    result = InputType.SELECT
		elif event_key == pygame.K_LEFT:
		    result = InputType.LEFT
		elif event_key == pygame.K_UP:
		    result = InputType.UP
		elif event_key == pygame.K_RIGHT:
		    result = InputType.RIGHT
		elif event_key == pygame.K_DOWN:
		    result = InputType.DOWN
		
		return result

    # TODO: add system to intelligently provide input data when needed
	@staticmethod
	def get_event_data():
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			pressed = InputHandler.get_input_state(event.type)

			if pressed == 'none':
				break

			action = InputHandler.get_input_type(event.key)

			if action == InputType.NONE:
				break

			return InputData(action, pressed)
