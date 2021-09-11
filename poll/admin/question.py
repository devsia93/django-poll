from django.contrib import admin

from poll.models import QuestionModel, AnswerModel


class AnswerItemInline(admin.TabularInline):
    model = AnswerModel
    fields = ('title',)
    extra = 1


@admin.register(QuestionModel)
class QuestionModelAdmin(admin.ModelAdmin):
    inlines = (AnswerItemInline,)
    list_display = ('title', 'type', 'poll',)
    list_filter = ('type',)
    search_fields = ('title', 'poll__title', 'poll_about',)
