
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_user, logout as logout_user
from .models import *

# Create your views here.
def index(req):
	if req.user.is_authenticated:
		return render(req, 'index_on_login.html')
	else:
		return render(req, r'index.html')


def login(req):
	return render(req, r'Login.html')

def login_active(req):
	if req.method == 'POST':
		Username = req.POST.get("Username")
		Password = req.POST.get("Password")
		user = authenticate(username=Username, password=Password)
		if user is not None:
			if user.is_active:
				req.session.set_expiry(3600)
				login_user(req, user)
				return redirect("/")
		else:
			return render(req,r"Login.html")

def logout_active(req):
	logout_user(req)
	return redirect("/")

def signup(req):
	return render(req,r"Signup.html")

def signup_active(req):
	if req.method =="POST":
		try:
			user = User.objects.create_user(username = req.POST.get('Username'),
											password = req.POST.get('Password'),
											email = req.POST.get('Email'),
											first_name = req.POST.get('Name'))
			user.save()
			return redirect('/')
		except:
			return render(req ,r'Signup.html')

def landscape(req):
    return render(req,r"Landscape.html")

def portrait(req):
    return render(req,r"Portrait.html")

def food(req):
    return render(req,"Food.html")

def comment(req):
    return render(req,"comment.html")

def writer(req):
    return render(req,"writer.html")

