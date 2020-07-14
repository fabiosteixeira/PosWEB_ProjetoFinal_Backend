import datetime

JWT_SECRET = 'd41d8cd98f00b204e9800998ecf8427e'
JWT_ALGORITHM = 'HS256'
JWT_EXP_DELTA_SECONDS = 2000

class Utils:
    def converter(o):
        if isinstance(o, datetime.date):
            return o.__str__()

    def converterParaListagem(o):
        if isinstance(o, datetime.date):
            return o.strftime('%d/%m/%Y')