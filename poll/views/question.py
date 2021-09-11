from django_filters import rest_framework
from rest_framework.viewsets import ReadOnlyModelViewSet

from api.filter import NumberInFilter
from poll.models import QuestionModel
from poll.serializers import QuestionSerializer


class QuestionFilter(rest_framework.FilterSet):
    poll = NumberInFilter(field_name='poll', lookup_expr='in')


class QuestionViewSet(ReadOnlyModelViewSet):
    queryset = QuestionModel.objects.all()
    serializer_class = QuestionSerializer
    filter_class = QuestionFilter
