from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.


class Subscription(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	verb = models.CharField(max_length=255)
	target_ct = models.ForeignKey(ContentType,blank=True,null=True,related_name='target_object')
	target_id = models.PositiveIntegerField(null=True,blank=True,db_index=True)
	target = GenericForeignKey('target_ct','target_id')
	created = models.DateTimeField(auto_now_add=True,db_index=True)

	class Meta:
		ordering = ['-created']

	def __str__(self):
		return self.user.username