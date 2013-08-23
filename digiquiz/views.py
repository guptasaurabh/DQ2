# Create your views here.
from datetime import datetime
from django.http import HttpResponse,Http404
from django.shortcuts import render, render_to_response
from django.contrib import auth
from django.core.context_processors import csrf, request
from django.http.response import HttpResponseRedirect
from digiquiz.models import LoginForm,Department,QuizForm,Section,Quiz,Question,QuestionForm
from django.forms.models import modelformset_factory
from digiquiz.services import generateQuizId,generateSectionId,generateQuestionId

def testModule(request):
    return HttpResponse(generateQuizId())

def quiz(request,ids):
    print ids
    quiz=Quiz.objects.get(quizId=ids)
    sections=Section.objects.filter(quizId=quiz)
#    quesNo={}
    for section in sections:
        section.noOfQues=Question.objects.filter(section=section).count()
#         quesNo[section.sectionId]=Question.objects.filter(section=section).count()
    return render(request, 'quiz.html', {'user':request.user,'quiz':quiz,'sections':sections,})

    
def createQuiz(request):
    if request.method=='POST':
        form=QuizForm(request.POST,request.FILES)
        if form.is_valid():
            quizs=form.save(commit=False)
            quizs.createdBy=request.user
            quizs.quizId=generateQuizId()
            quizs.save()
            return quiz(request,quizs.quizId)
            
        else:
            print "Its error"
            
    else:
        form=QuizForm()
        
#     dept=Department.objects.filter(parent_department=None)
#     
    return render(request, 'createQuiz.html', {'user':request.user,'form':form,})

def addsection(request,quizid):
    quiz=Quiz.objects.get(quizId=quizid)
    sectionFormSet=modelformset_factory(Section,exclude=['quizId','sectionId'])
    if request.method=='POST':
        formset = sectionFormSet(request.POST)
        if formset.is_valid():
#             data = formset.cleaned_data
            for form in formset.forms:
                section = form.save(commit=False)
                section.quizId =quiz
                if section.sectionId == '':
                    section.sectionId=generateSectionId()
                section.save()
            return render(request, 'addsection.html', {'formset':formset,'quizid':quizid,})
        else:
            return render(request, 'addsection.html', {'formset':formset,'quizid':quizid,})
    else:
        formset=sectionFormSet(queryset=Section.objects.filter(quizId=quiz))
        return render(request, 'addsection.html', {'formset':formset,'quizid':quizid,})

       
def addsec(request):
    sections=Section.objects.all().delete();
    print sections
    print "hello"
    print request.POST
    return render(request, 'addsec.html')#, {'total':request.POST['total'],})

def login(request):
    if request.method == 'POST': # If the form has been submitted...
        form = LoginForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request, user)
                return HttpResponseRedirect('createquiz')
            else:
                return render(request, 'login.html', {'form': form,})
    else:
        form = LoginForm() # An unbound form

    return render(request, 'login.html', {'form': form,})

def logout(request):
    auth.logout(request)
    print "wassup miyam"
    return HttpResponseRedirect('login')
    
def getsubdept(request):
#     subdepts={}
#     for i in request.POST.getlist('id[]'):
#         deptid=i;
#         parentdept=Department.objects.get(id=deptid)
#         subdept=Department.objects.filter(parent_department=parentdept)
#         subdepts[parentdept]=subdept
#     print subdepts
    return HttpResponseRedirect('login')
    #return render(request, 'deptselector.html', {'subdepts': subdepts,'n':int(request.POST["n"]),'next':int(request.POST["n"])+1,'i':1})
#     
#     
def testajax(request):
#     print request.GET
#     deptid=request.GET["id[]"]
#     parentdept=Department.objects.get(id=deptid)
#     subdepts=Department.objects.filter(parent_department=parentdept)
#     print subdepts
#    return render(request, 'deptselector.html', {'subdepts': subdepts,'n':int(request.GET["n"]),'next':(int(request.GET["n"]+1))})
    
    return HttpResponseRedirect('login')
        
      
      
def addquestions(request,sectionid):
    section=Section.objects.get(sectionId=sectionid)
    quiz=section.quizId
    if request.method=='POST':
        form=QuestionForm(request.POST)
        if form.is_valid():
            question=form.save(commit=False)
            question.createdBy=request.user
            question.quizId=generateQuestionId()
            question.save()
        else:
            print "Its error"
    else:
        form=QuestionForm()
        
#     dept=Department.objects.filter(parent_department=None)
#     
    return render(request, 'addQuestion.html', {'quiz':quiz,'section':section,'user':request.user,'form':form,})


#def fileupload(request):
    