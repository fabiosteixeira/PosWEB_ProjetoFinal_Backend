from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=300)
    password = models.CharField(max_length=300)

    def as_json(self):
        return dict(
            id = self.id
            , nome = self.nome
            , email = self.email
        )

    def match_password(self, password):
        if password != self.password:
            raise User.PasswordDoesNotMatch
    
    class PasswordDoesNotMatch(BaseException):
        pass

    class DoesNotExist(BaseException):
        pass