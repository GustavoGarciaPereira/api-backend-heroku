from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


class Music(models.Model):

    class Meta:

        db_table = 'music'

    title = models.CharField(max_length=200)
    seconds = models.IntegerField()

    def __str__(self):
        return self.title

class Programador(models.Model):

    class Meta:

        db_table = 'programador'

    nome = models.CharField(max_length=200)
    data_nascimento = models.DateField(blank=True, null=True)
    liguagem_atualmente = models.CharField(max_length=200)

    def __str__(self):
        return self.nome