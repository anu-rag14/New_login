from __future__ import unicode_literals

from django.db import models

# Create your models here.
class login_data(models.Model):
	name=models.CharField(max_length=120)
	number=models.IntegerField(null=True)
	otp=models.IntegerField(null=True)
	email=models.EmailField(null=True)

