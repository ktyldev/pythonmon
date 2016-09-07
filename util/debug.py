import datetime

enabled = False
record_time = False


def log(text):
    if enabled:
        if record_time:
            __write(__date_format(text))
        else:
            __write(text)


def log_error(error_text):
    text = __date_format(error_text)
    __write(text)


# Private methods
def __write(text):
    print(text)


def __date_format(text):
    date_string = '{%H:%M:%S}'.format(datetime.datetime.now())
    log_string = '[{0}]: {1}'.format(date_string, text)
    return log_string
