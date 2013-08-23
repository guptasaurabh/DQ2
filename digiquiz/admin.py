from django.contrib import admin
from digiquiz.models import Quiz,UserProfile,Department,QuizUser,Question,Option,Section

#admin.site.register(Quiz)
admin.site.register(UserProfile)
admin.site.register(Department)
admin.site.register(QuizUser)
#admin.site.register(Section)


class QuestionInline(admin.StackedInline):
    model = Question


class OptionsInline(admin.StackedInline):
    model = Option

class SectionAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    
class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionsInline]

class SectionsInLine(admin.StackedInline):
    model=Section
    
class QuizAdmin(admin.ModelAdmin):
    inlines=[SectionsInLine]

# admin.site.register(Quiz,QuizAdmin)

admin.site.register(Question,QuestionAdmin)

admin.site.register(Quiz,QuizAdmin)

admin.site.register(Section, SectionAdmin)