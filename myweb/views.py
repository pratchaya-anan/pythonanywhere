
from .form import addComment
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_user, logout as logout_user
from .models import *
from django.contrib.auth.forms import UserCreationForm

from .models import Comment
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
				req.session.set_expiry(300)
				login_user(req, user)
				return redirect("/")
		else:
			return render(req,r"Login.html")

def logout_active(req):
	logout_user(req)
	return redirect("/")

def signup(req):
	if req.method == "POST":
    		return render(req, r'login')
	return render(req,r"Signup.html")

def signup_active(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login_user(request, user)
			return redirect('/')
	else:
		form = UserCreationForm()
	return render(request, r'Signup.html', {'form': form})


def landscape(req):
    return render(req,r"Landscape.html")

def portrait(req):
    return render(req,r"Portrait.html")

def food(req):
    return render(req,"Food.html")

def comment(req):
	getcomment = Comment.objects.all()
	for i in getcomment:
		print(i)
	return render(req,"comment.html",{"comment":getcomment})

def writer(req):
	if req.method == "POST":
		headtext = req.POST.get("headtext")
		commenttext = req.POST.get("commenttext")
		if (headtext == None)  or (commenttext == None):
    			return redirect('writer')
		elif (headtext != None)  and (commenttext != None):
			add = Comment(CommentName=headtext, Comment=commenttext)
			add.save()
			return redirect('writer')
		#Comment.objects.insert(CommentName=headtext,Comment = commenttext)

		#print(headtext)

	return render(req,"writer.html")

