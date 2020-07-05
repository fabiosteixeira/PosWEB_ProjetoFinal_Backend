import datetime

class Utils:
    def converter(o):
        if isinstance(o, datetime.date):
            return o.__str__()