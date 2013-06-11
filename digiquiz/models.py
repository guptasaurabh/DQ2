from django.db import models
from django.contrib.auth.models import User

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
    time=models.TimeField(null=True)
    createdBy=models.ForeignKey(User)
    description=models.CharField(max_length=500,blank=True,null=True) 
    def __unicode__(self):
        return self.quizId

class QuizUser(models.Model):
    quiz=models.ForeignKey(Quiz)
    user=models.ForeignKey(User)
    marks=models.FloatField(null=True)


class Question(models.Model):
    question_id=models.CharField(max_length=10)
    quiz=models.ForeignKey(Quiz)
    question_text=models.CharField(max_length=500)
    marks=models.IntegerField(10)
    negative=models.IntegerField(10)
    starred=models.BooleanField()
    data_path=models.FilePathField(null=True,blank=True)
    def __unicode__(self):
        return self.question_text
  
      
class Options(models.Model):
    optionDescription=models.CharField(max_length=100)
    right=models.BooleanField()
    question=models.ForeignKey(Question)
    def __unicode__(self):
        return self.optionDescription
  


# #class userquizquestion(models.Model):
#     #quiz
#     #user
#     #question
#     #answer    

