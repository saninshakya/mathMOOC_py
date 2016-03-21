from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Username or Email'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class SignupForm(forms.Form):
	p_first_name =  forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Parent First Name'}), label ='')
	p_last_name =  forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Parent Last Name'}), label ='')
	p_username = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Parent Username'}), label ='')
	p_email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder':'Email'}), label ='')
	
	first_name =  forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Student First Name'}), label ='')
	last_name =  forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Student Last Name'}), label ='')
	username = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Student Username'}), label ='')
	
	# password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), label ='')
	# confirm = forms.CharField(required=True,  widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}), label ='')
    
	def clean_confirm(self):
		password = self.cleaned_data.get('password')
		confirm = self.cleaned_data.get('confirm')
		if password !=  confirm:
		    raise forms.ValidationError("Confirm Password didnot matched.")
		return confirm

	def clean_username(self):
	    username = self.cleaned_data['username']
	    if User.objects.filter(username=username).exists():
	        raise forms.ValidationError('Username already exists.')
	    return username

	