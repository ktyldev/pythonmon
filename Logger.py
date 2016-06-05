from Configuration import Configuration

class Logger:
	_state = Configuration.log_all
	
	@staticmethod
	def log(text):
		if Logger._state:
			print text
		


