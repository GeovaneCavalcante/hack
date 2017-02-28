from django.db import models

class Dados(models.Model):
    email = models.EmailField()
    senha = models.CharField(max_length=20)
    quantidade = models.IntegerField()

    def __str__(self):
        return self.email