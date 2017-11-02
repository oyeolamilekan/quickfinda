from django import template
from ..forms import feedBackForm

register = template.Library()

@register.inclusion_tag('_form.html')
def report_form(url):
	form = feedBackForm()
	return {'form':form,'url':url}