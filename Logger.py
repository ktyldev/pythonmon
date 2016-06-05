

class Logger:
	_state = False
	
	@staticmethod
	def log(text):
		if Logger._state:
			print text
		


