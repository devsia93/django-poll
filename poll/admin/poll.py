from django.contrib import admin

from poll.models import PollModel, QuestionModel


class QuestionItemInline(admin.TabularInline):
    model = QuestionModel
    fields = ('title', 'type',)
    extra = 1


@admin.register(PollModel)
class PollModelAdmin(admin.ModelAdmin):
    inlines = (QuestionItemInline,)
    list_display = ('title', 'about', 'start_date', 'end_date',)
    search_fields = ('title', 'about', 'start_date', 'end_date',)

    def get_readonly_fields(self, request, obj=None):
        defaults = super().get_readonly_fields(request, obj=obj)
        if obj:
            defaults = tuple(defaults) + ('start_date',)
        return defaults
