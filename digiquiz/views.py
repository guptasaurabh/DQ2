# Create your views here.
from django.http import HttpResponse,Http404
from django.shortcuts import render

def createQuiz(request):
    return render(request, 'createQuiz.html', {'user':request.user})

def login(request):
     username=request.POST['username']
     password=request.POST['password']
    