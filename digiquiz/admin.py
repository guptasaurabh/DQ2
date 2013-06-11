from django.contrib import admin
from digiquiz.models import Quiz,UserProfile,Department,QuizUser,Question,Options

#admin.site.register(Quiz)
admin.site.register(UserProfile)
admin.site.register(Department)
admin.site.register(QuizUser)
#admin.site.register(Options)


class QuestionInline(admin.StackedInline):
    model = Question


class OptionsInline(admin.StackedInline):
    model = Options
    

class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    
class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionsInline]

admin.site.register(Quiz,QuizAdmin)

admin.site.register(Question,QuestionAdmin)
