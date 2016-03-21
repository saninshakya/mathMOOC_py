from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.contrib import messages
import sys
# from django.contrib.sessions.models import Session
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.contrib.auth.models import User
import datetime
from django.shortcuts import redirect
from user.forms import LoginForm, SignupForm

def signup(request):
	try:
		args={}
		form = SignupForm()
		if request.method == 'POST':
			form = SignupForm(request.POST)

			if form.is_valid():
				cd = form.cleaned_data
				s_first_name = cd['first_name']
				s_last_name = cd['last_name']
				s_username = cd['username']
				s_password = 'pass'

				p_first_name = cd['p_first_name']
				p_last_name = cd['p_last_name']
				p_username = cd['p_username']
				p_email = cd['p_email']
				p_password = 'pass'

				result = User.objects.create_user(password=s_password, username=s_username, first_name=s_first_name, last_name=s_last_name, email = 'testuser@gmail.com')
				rslt = User.objects.create_user(password=p_password, username=p_username, first_name=p_first_name, last_name=p_last_name, email =p_email)

				if rslt:
					messages.add_message(request, messages.INFO, "Welcome, You are Registered Successfully.")
					return HttpResponseRedirect('/test/')	
				else:
					messages.add_message(request, messages.ERROR, "Error occured during registration. Please Try Again.")
					return render(request, 'user/signup.html')
			else:
				args['form'] = form	
				return render(request, 'user/signup.html', args)
		else:
			return render(request, 'user/signup.html', {'form':form})
	except:
		messages.add_message(request, messages.ERROR, sys.exc_info()[1])
	return render(request, 'user/signup.html', {'form':form})			
				

def login_account(request):
	try:
		args={}
		form = LoginForm()
		if request.method == 'POST':
			form = LoginForm(request.POST)
			if form.is_valid():
				cd = form.cleaned_data
				username = cd['username']
				password = cd['password']
				user = authenticate(username=username, password=password)
				if user is not None:
					if user.is_active:	
						# update last login in database
						result = User.objects.filter(username=username).update(last_login=datetime.datetime.now())
						login(request, user) #Django buildin login method
						# request.session['bookserviceUser'] = username
						# response = HttpResponse()
						# response.set_cookie('bookserviceLogin', 'True')
						return HttpResponseRedirect('/test/')
					else:
						messages.add_message(request, messages.INFO, 'This account has been disabled.')
				else:
					messages.add_message(request, messages.INFO, 'Invalid Username and Password')
			else:
				args['form'] = form	
				return render(request, 'user/login.html', args)
		else:
			return render(request, 'user/login.html', {'form':form})
	except:
		messages.add_message(request, messages.ERROR, sys.exc_info()[1])
	return render(request, 'user/login.html', {'form':form})

def logout_account(request):
	try:
		# del request.session['bookserviceUser']
		# response = HttpResponse()
		# response.delete_cookie('bookserviceLogin')
		auth.logout(request)
		return HttpResponseRedirect("/test/")
	except KeyError:
		pass
	return HttpResponseRedirect("/test/")

