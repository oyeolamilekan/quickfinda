from .models import *
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
import re
from django.contrib.contenttypes.models import ContentType

def subscribe(userd,new_form,verb=None):
	target_ct = ContentType.objects.get_for_model(new_form)
	similar = Subscription_list.objects.filter(user=userd,target_ct=target_ct,target_id=new_form.id)
	if similar.exists():
		similar.delete()
	else:
		sub = Subscription_list(user=userd,target=new_form,verb=verb)
		sub.save()