from django.db import models

class Customer(models.Model):
	first_name = models.CharField(max_length=30, null=True)
	last_name = models.CharField(max_length=30, null=True)
	email = models.EmailField(null=True)
	# vendors = models.ManyToManyField(Vendor)
	Account_token = models.CharField(max_length=50, null=True, blank=True)

	def __str__(self):
		return self.first_name + ' ' + self.last_name

class Vendor(models.Model):
	first_name = models.CharField(max_length=30, null=True)
	last_name = models.CharField(max_length=30, null=True)
	company_name = models.CharField(max_length=256, null=True, blank=True)
	email = models.EmailField(null=True)
	clients = models.ManyToManyField(Customer, blank=True)
	Account_token = models.CharField(max_length=50, null=True, blank=True)

	def __str__(self):
		return self.first_name + ' ' + self.last_name