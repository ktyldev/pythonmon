from Configuration import Configuration

class Logger:
	enabled = Configuration.log_all
	
	@staticmethod
	def log(text):
		if Logger.enabled:
			print text