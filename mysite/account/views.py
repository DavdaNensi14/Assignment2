from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

# Create your views here.
print "*********View***********"
def account_registration_page(request):
	if request.method == "POST":
		print request.POST

		return HttpResponseRedirect('/account/login/')
	else:	
		return render(request,'account_registration_page.html', {})

def account_login_page(request):
	return render(request,'account_login_page.html')


def account_logout_page(request):
	# if request.method == "POST"
		return HttpResponseRedirect('/account/login/')


	