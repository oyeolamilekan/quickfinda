from django import forms
from django.contrib.auth.models import User
from .models import Profile

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
	password = forms.CharField(label='Password',widget=forms.PasswordInput)
	password2 = forms.CharField(label='Repeat password',widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ('username','first_name','email')

	def clean_password2(self):
		cd = self.cleaned_data
		if cd['password'] != cd['password2']:
			raise forms.ValidationError("Passwords don't match.")
		return cd['password2']

	# Validates the username for registration against the database
	def clean_username(self):
		username = self.cleaned_data.get('username')
		if User.objects.filter(username=username).exists():
			raise forms.ValidationError("This username is already taken")
		return username

	# Validates the email for registration against the database
	def clean_email(self):
		email = self.cleaned_data.get('email')
		if User.objects.filter(email=email).exists():
			raise forms.ValidationError("This email is already taken")
		return email

class UserEditForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name','last_name')

	# Validates the email against the database 
	def clean_email(self):
		email = self.cleaned_data.get('email')
		if email == '':
			raise forms.ValidationError("Email field can not be empty")	
		return email

class ProfileEditForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('date_of_birth','photo','snapchat_username','facebook_username','twitter_username','cover_photo','bio')
