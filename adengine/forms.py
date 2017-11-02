from .models import Ads
from django import forms

class AdsForm(forms.ModelForm):
	class Meta:
		model = Ads
		fields = ['title','website','banner']
		labels = {'title':'Title'}

class ProdAdsForm(forms.ModelForm):
	class Meta:
		model = Ads
		fields = ['title','website','price','banner']
		labels = {'title':'Title'}