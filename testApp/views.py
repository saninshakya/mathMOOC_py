from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from testApp.forms import testAppForm

def index(request):
	form = testAppForm()
	return render(request,'testApp/index.html', {'form':form})
