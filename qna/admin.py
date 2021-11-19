from django.contrib import admin

from .models import Choice, Question, Subject, Score



class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1



class ScoreInline(admin.TabularInline):
    model = Score
    extra = 1
    list_display = ('subject','score','items')
    readonly_fields = ('subject',)



class SubjectAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Subject',                {'fields': ['subject_text']}),
    ]
    search_fields = ('subject_text',)



class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Subject',                {'fields': ['subject']}),
        ('Question',               {'fields': ['question_text']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text','subject')
    search_fields = ('question_text',)



class ChoiceAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question',                {'fields': ['question']}),
        ('Choice',                  {'fields': ['choice_text']}),
        ('Is Correct Answer',       {'fields': ['is_correct_answer']}),
    ]
    list_display = ('question','choice_text','is_correct_answer')
    search_fields = ('question_text',)



class ScoreAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Score',                  {'fields': ['user','subject','score','items','pub_date']}),
    ]
    list_display = ('user','subject','score','items','pub_date')
    search_fields = ('user','subject','pub_date')



admin.site.register(Subject,  SubjectAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice,   ChoiceAdmin)
admin.site.register(Score,    ScoreAdmin)

