from django import forms
from .models import Feedback

class feedBackForm(forms.ModelForm):
	class Meta:
		model = Feedback
		fields = ('feelings','url_locator','content')
		labels = {'content':'body','feelings':'How was the services','url_locator':'Current location'}
		widgets = {'content':forms.Textarea(attrs={'cols':10,'rows':3})}