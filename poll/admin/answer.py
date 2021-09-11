from django.contrib import admin

from poll.models import AnswerModel


@admin.register(AnswerModel)
class AnswerModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'question',)
    search_fields = ('title', 'question__title',)
