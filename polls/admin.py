from django.contrib import admin

# Register your models here.
from .models import Question, Choice

class ChoiceInline(admin.TabularInline) : 
    model = Choice
    extra = 3

#   admin panel for 
class QuestionAdmin(admin.ModelAdmin) : 
    list_display = ('id', 'question_text', 'pub_date', 'is_published')
    list_display_links = ('id', 'question_text')
    list_editable = ('is_published',)
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)


