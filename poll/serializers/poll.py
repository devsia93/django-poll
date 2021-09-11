from rest_framework import serializers

from poll.models import PollModel


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollModel
        fields = ('id', 'title', 'about', 'start_date', 'end_date',)
