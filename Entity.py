import pygame

from Logger import Logger
from Constants import Constants

class Entity:

	List = []

	@staticmethod
	def find(name):
		for entity in Entity.List:
			if entity.name == name:
				return entity
		return None

	def __init__(self, name, x = 0, y = 0):
		self.name = name
		self.x = x
		self.y = y
		self.child_entities = []
		self.components = []

		Entity.List.append(self)

		Logger.log(self.name + ' initialised at ' + str(self.x) + ", " + str(self.y))

	def get_component(self, component_tag):
		for component in self.components:
			if component.tag == component_tag:
				return component

	def update(self):
		for component in self.components:
			if component.enabled:
				component.update()