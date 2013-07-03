from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
# Create your models here.

class Department(models.Model):
    name=models.CharField(max_length=50)
    parent_department=models.ForeignKey('self',null=True,blank=True)
    Department_owner=models.OneToOneField(User,null=True,blank=True)
    def __unicode__(self):
        return self.name
 
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    department=models.OneToOneField(Department,null=True,blank=True)
    
    
class Quiz(models.Model):
    quizId=models.CharField(max_length=10, primary_key=True)
    startDate=models.DateField()
    endDate=models.DateField()
    random=models.BooleanField()
    time=models.IntegerField(null=True)
    createdBy=models.ForeignKey(User)
    description=models.CharField(max_length=500,blank=True,null=True) 
    def __unicode__(self):
        return self.quizId
    
class Section(models.Model):
    quizId=models.ForeignKey(Quiz)
    name=models.CharField(max_length=20)
    sectionId=models.CharField(max_length=10,primary_key=True)
    
    

class QuizUser(models.Model):
    quiz=models.ForeignKey(Quiz)
    user=models.ForeignKey(User)
    marks=models.FloatField(null=True)


class Question(models.Model):
    question_id=models.CharField(max_length=10)
    section=models.ForeignKey(Section)
    question_text=models.CharField(max_length=500)
    marks=models.IntegerField(10)
    negative=models.IntegerField(10)
    starred=models.BooleanField()
    data_path=models.FilePathField(null=True,blank=True)
    def __unicode__(self):
        return self.question_text
  
      
class Option(models.Model):
    optionText=models.CharField(max_length=100)
    right=models.BooleanField()
    question=models.ForeignKey(Question)
    def __unicode__(self):
        return self.optionDescription
  


class Userquiz(models.Model):
    quiz=models.ForeignKey(Quiz)
    user=models.ForeignKey(User)
    question=models.ForeignKey(Question)
    answer=models.ForeignKey(Option)   



#Form Objects
 
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'labels'}),max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(render_value=False,attrs={'class':'labels'}),max_length=100)
    

class QuizForm(ModelForm):
    class Meta:
        model = Quiz
        exclude = ['createdBy','quizId']
       
    