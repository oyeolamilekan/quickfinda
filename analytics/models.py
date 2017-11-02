from django.db import models

# Create your models here.

class QueryList(models.Model):
	title = models.CharField(max_length=200)
	res_list = models.TextField(blank=True,null=True)
	section = models.CharField(max_length=200)
	qury_bool = models.BooleanField(default=True)
	date_added = models.DateTimeField(auto_now_add=True,blank=True,null=True)

	def __str__(self):
		return self.title