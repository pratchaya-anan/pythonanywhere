from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(req):
	return HttpResponse('ยินดีต้อนรับ' + req.method)
	#return render(req, 'myweb/index.html')

def sketchy(req):
	return render(req, 'myweb/sketchy.html')

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)