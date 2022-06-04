from distutils.command.upload import upload
from django.db import models

# Create your models here.

class KahveModel(models.Model):
    ad = models.CharField(max_length=50, verbose_name="Kahve")
    aciklama = models.TextField(max_length=500, verbose_name="Açıklama")
    fotograf = models.ImageField(upload_to="kahveler")

    def __str__(self):
        return self.ad

    class Meta:
        verbose_name = "Kahve"
        verbose_name_plural = "Kahveler"