from django.db import models

# Create your models here.

class Kontak(models.Model):
	nama = models.CharField(max_length=50, blank=True)
	no_telp = models.CharField(max_length=13, blank=True)

def __str__(self):
	return "{}". format(self.id)

