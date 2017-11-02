from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.contrib.auth.models import User,models

# Create your models here.

class Profile(models.Model):
	GENDER = (
		('Male','Male'),
		('female','female')
	)
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	date_of_birth = models.DateField(blank=True,null=True)
	photo = models.ImageField(upload_to="users/%Y/%m/%d",blank=True,null=True)
	gender = models.CharField(max_length=200,choices=GENDER,default='None')
	cover_photo = models.ImageField(upload_to="users/%Y/%m/%d",blank=True,null=True)
	phone_number = models.CharField(max_length=20,blank=True,null=True,default="")
	twitter_username = models.CharField(max_length=20,blank=True,null=True,default="")
	facebook_username = models.CharField(max_length=20,blank=True,null=True,default="")
	snapchat_username = models.CharField(max_length=20,blank=True,null=True,default="")
	bio = models.TextField(default="",blank=True,null=True)
	page_views = models.IntegerField(default=0)
	counter = models.IntegerField(default=0)
	subscription = models.TextField()
	name = models.CharField(max_length=800)
	message_counter = models.IntegerField(default=0)
	agree_to_terms = models.BooleanField(default=True)

	def __str__(self):
		return 'Profile for user {}'.format(self.user.username)

	def get_screen_name(self):
		try:
			if self.user.get_full_name():
				return self.user.get_full_name()
			else:
				return self.user.username
		except:
			return self.user.username

class Sub(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	lisert = models.CharField(max_length=600)

	def __str__(self):
		return self.lisert


def create_profile(sender,**kwargs):
	if kwargs['created']:
		user_profile = Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)