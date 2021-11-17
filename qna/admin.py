from django.contrib import admin

from .models import Choice, Question, Subject, Score, Student





class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1



class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1



class ScoreInline(admin.TabularInline):
    model = Score
    extra = 1
    list_display = ('subject','score')
    readonly_fields = ('subject',)



class StudentAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Student',                {'fields': ['first_name','last_name','email','address']}),
    ]
    inlines = [ScoreInline]
    list_display = ('first_name','last_name','email','address')
    search_fields = ('first_name','last_name','email','address')



class SubjectAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Subject',                {'fields': ['subject_text']}),
    ]
    inlines = (QuestionInline,)
    search_fields = ('subject_text',)



class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Subject',                {'fields': ['subject']}),
        ('Question',               {'fields': ['question_text']}),
    ]
    readonly_fields = ['subject']
    inlines = [ChoiceInline]
    list_display = ('question_text','subject')
    search_fields = ('question_text',)



admin.site.register(Student, StudentAdmin)
admin.site.register(Subject,  SubjectAdmin)
admin.site.register(Question, QuestionAdmin)
