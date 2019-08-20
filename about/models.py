from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Orang(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	nis = models.CharField(max_length=6, null=False, blank=False, primary_key=True)
	nama = models.CharField(max_length=30, blank=True, null=True)
	umur = models.IntegerField(blank=False, null=False)

	def __str__(self):
		return "{}".format(self.nama)

class Nilai(models.Model):
	user = models.ForeignKey(User, blank=False)
	bulan = models.CharField(max_length=10, blank=True, null=True)
	nilai = models.IntegerField(blank=True, null=True)

	def __str__(self):
		return "{}".format(self.user)

class SPP(models.Model):
	user = models.ForeignKey(User, blank=False)
	bulan = models.CharField(max_length=10, blank=True, null=True)
	status = models.CharField(max_length=15, blank=True, null=True)

	def __str__(self):
		return "{}".format(self.user)

