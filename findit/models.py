from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
# Create your models here.
CONDITIONS = (

	(100, 'Extremely satisfied'),
	(70, 'Moderately satisfied'),
	(40, 'Slightly satisfied'),
	(10, 'Neutral'),
	(5, 'Slightly dissatisfied'),
	(2, 'Moderately dissatisfied'),
	(1, 'Exteremely dissatisfied'),
)

class Products(models.Model):
	name = models.CharField(max_length=300)
	price = models.CharField(max_length=300)
	real_price = models.IntegerField(default=0)
	image = models.ImageField(blank=True,null=True)
	source_url = models.CharField(max_length=300)
	shop = models.CharField(max_length=300)
	createdate = models.DateTimeField(auto_now_add=True)
	old_price = models.CharField(max_length=200,default='')
	old_price_digit = models.IntegerField(default=0)
	sub_genre = models.CharField(max_length=200,blank=True,null=True,default='')
	genre = models.CharField(max_length=200,blank=True,null=True,default='')
	subcriptions = models.ManyToManyField(settings.AUTH_USER_MODEL)

	def __str__(self):
		return self.name

class Analytics(models.Model):
	product = models.OneToOneField(Products) 
	number_of_clicks = models.IntegerField(default=0)
	createdate = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.number_of_clicks

class Feedback(models.Model):
	feelings = models.IntegerField(choices=CONDITIONS,blank=True,null=True)
	url_locator = models.CharField(blank=True,null=True,max_length=200)
	content = models.TextField(blank=True,null=True)
	createdate = models.DateTimeField(auto_now_add=True,blank=True,null=True)

	def __str__(self):
		return self.content


def create_products(sender,**kwargs):
	if kwargs['created']:
		products = Analytics.objects.create(product=kwargs['instance'])

post_save.connect(create_products, sender=Products)
