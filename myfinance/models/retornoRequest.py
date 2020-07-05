class RetornoRequest:
    def __init__(self, eherro, message):
        self.eherro = eherro
        self.message = message

    def as_json(self):
        return dict(
            eherro = self.eherro
            , message = self.message
        )        