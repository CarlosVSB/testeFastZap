from uuid import uuid4

from django.db import models

# Create your models here.


class Produto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(verbose_name='Nome Produto',max_length=255, default='')
    description = models.CharField(max_length=255, default='')
    price = models.FloatField(default=0.0)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.nome