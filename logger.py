import configuration


class Logger:
    enabled = configuration.log_all
    
    @staticmethod
    def log(text):
        if Logger.enabled:
            print(text)
