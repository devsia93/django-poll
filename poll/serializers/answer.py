from rest_framework import serializers

from poll.models import AnswerModel


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerModel
        fields = ('id', 'title', 'question',)
