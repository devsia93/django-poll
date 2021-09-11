from rest_framework import serializers

from poll.models import QuestionModel
from poll.serializers import AnswerSerializer


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)
    type = serializers.CharField(source='get_type_display')

    class Meta:
        model = QuestionModel
        fields = ('id', 'title', 'type', 'poll', 'answers',)
