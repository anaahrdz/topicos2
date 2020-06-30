from django.db import models

class User(models.Model):
	#Modelo de tabla usuaruios#
	#email,password nombre,ap_pat bio, fecha de nacimiento#

	email =models.EmailField(unique=True)
	password = models.CharField(max_length =100)

	first_name=models.CharField(max_length =100)
	last_name = models.CharField(max_length =100)

	bio = models.TextField(blank=True)

	birthdate = models.TextField(blank=True, null=True)
	created =models.DateTimeField(auto_now_add=True)
	modified =models.DateField(auto_now=True)

