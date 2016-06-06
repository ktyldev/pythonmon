import pygame
import sys

class InputData:
	def __init__(self, movement_key, action_key):
		self.movement_key = movement_key
		self.action_key = action_key

class EventData:
	def __init__(self, key, state):
		self.key = key
		self.state = state

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

	@staticmethod
	def get_event_data():
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			state = InputHandler.get_input_state(event.type)

			if state == 'none':
				break

			key = InputHandler.get_input_type(event.key)

			if key == InputType.NONE:
				break

			return EventData(key, state)

	@staticmethod
	def get_continuous_data():

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		keys = pygame.key.get_pressed()

		movement_key = InputType.NONE
		action_key = InputType.NONE
		
		if keys[pygame.K_UP]:
			movement_key = InputType.UP
		elif keys[pygame.K_RIGHT]:
			movement_key = InputType.RIGHT
		elif keys[pygame.K_DOWN]:
			movement_key = InputType.DOWN
		elif keys[pygame.K_LEFT]:
			movement_key = InputType.LEFT

		if keys[pygame.K_z]:
			action_key = InputType.A
		elif keys[pygame.K_x]:
			action_key = InputType.B
		elif keys[pygame.K_c]:
			action_key = InputType.START
		elif keys[pygame.K_v]:	
			action_key = InputType.SELECT

		if action_key == InputType.NONE and movement_key == InputType.NONE:
			return

		return InputData(movement_key, action_key)