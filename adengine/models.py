from django.db import models
from django.conf import settings 
# Create your models here.
timers = (('True','True'),('False','False'))
ad_tpye = (('Banner','Banner'),('Products','Products'))

class AdsBuy(models.Model):
	ad_owner = models.ForeignKey(settings.AUTH_USER_MODEL,blank=True,null=True)
	ad_type = models.CharField(max_length=200,choices=ad_tpye,default='Banner')
	as_ad_credit = models.BooleanField(default=False)

	def __str__(self):
		return str(self.as_ad_credit)

class Ads(models.Model):
	ad_owner = models.ForeignKey(settings.AUTH_USER_MODEL,blank=True,null=True)
	title = models.CharField(max_length=200,blank=True,null=True)
	price = models.CharField(max_length=200,blank=True,null=True)
	banner = models.ImageField(upload_to="ad_cutomers",blank=True,null=True)
	website = models.CharField(max_length=200,blank=True,null=True)
	date_adder = models.DateField(auto_now_add=True)
	date_added = models.DateTimeField(auto_now_add=True)
	expired = models.CharField(max_length=40,choices=timers,default='False')
	time_wait = models.CharField(max_length=200,blank=True,null=True)
	ad_type = models.CharField(max_length=200,choices=ad_tpye,default='Banner')
	views = models.IntegerField(default=0)
	clicks = models.IntegerField(default=0)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Ads'

class Click(models.Model):
	ads = models.ForeignKey(Ads)
	click_cal = models.CharField(max_length=20,blank=True,null=True)
	date_added = models.DateTimeField(auto_now_add=True,null=True)

	def __str__(self):
		return self.click_cal

	class Meta:
		verbose_name = 'Clicks'

class View(models.Model):
	ads = models.ForeignKey(Ads)
	views_cal = models.CharField(max_length=20,blank=True,null=True)
	date_added = models.DateTimeField(auto_now_add=True,null=True)

	def __str__(self):
		return self.views_cal

	class Meta:
		verbose_name = 'Views'