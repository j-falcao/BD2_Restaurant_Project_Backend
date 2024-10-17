from django.db import models

class Garcom(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=20)

    class Meta:
        db_table = 'garcom'

    def __str__(self):
        return self.nome

class Idioma(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        db_table = 'idioma'

    def __str__(self):
        return self.nome

class GarcomIdioma(models.Model):
    garcom = models.ForeignKey(Garcom, on_delete=models.CASCADE, related_name='idiomas')
    idioma = models.ForeignKey(Idioma, on_delete=models.CASCADE, related_name='garcons')

    class Meta:
        db_table = 'garcom_idioma'

    def __str__(self):
        return f"{self.garcom.nome} - {self.idioma.nome}"
