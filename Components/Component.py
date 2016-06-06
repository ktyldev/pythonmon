class Component:
	def __init__(self, entity, tag):
		self.entity = entity
		self.enabled = True
		self.tag = tag

	def update(self):
		return