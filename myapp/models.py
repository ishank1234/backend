from django.db import models

# Create your models here.

class CryptoCoin(models.Model):
    name=models.CharField(max_length=50, null=True)
    price=models.CharField(max_length=50, null=True)
    onehour = models.CharField(max_length=50, null=True)
    oneday = models.CharField(max_length=50, null=True)
    sevenday =models.CharField(max_length=50, null=True)
    marketcap = models.CharField(max_length=50, null=True)
    volume = models.CharField(max_length=50, null=True)
    supply =models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name
