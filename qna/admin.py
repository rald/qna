from django.contrib import admin

from .models import Choice, Question, Subject, Score



class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1



class ScoreInline(admin.TabularInline):
    model = Score
    extra = 1
    list_display = ('subject','score')
    readonly_fields = ('subject',)



class SubjectAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Subject',                {'fields': ['subject_text']}),
    ]
    search_fields = ('subject_text',)



class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question',               {'fields': ['question_text']}),
        ('Subject',                {'fields': ['subject']}),
    ]
    readonly_fields = ['subject']
    inlines = [ChoiceInline]
    list_display = ('question_text','subject')
    search_fields = ('question_text',)



admin.site.register(Subject,  SubjectAdmin)
admin.site.register(Question, QuestionAdmin)
