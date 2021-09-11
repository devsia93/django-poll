from django_filters import rest_framework
from rest_framework.viewsets import ReadOnlyModelViewSet

from poll.models import PollModel
from poll.serializers import PollSerializer


class PollFilter(rest_framework.FilterSet):
    start_date = rest_framework.Filter(field_name='start_date', lookup_expr='exact')
    start_date__gte = rest_framework.Filter(field_name='start_date', lookup_expr='gte')
    end_date__lt = rest_framework.Filter(field_name='end_date', lookup_expr='lt')


class PollViewSet(ReadOnlyModelViewSet):
    # filter(Q(start_date__gte=datetime.now()) & Q(end_date__lt=datetime.now()))
    queryset = PollModel.objects.all()
    serializer_class = PollSerializer
    filter_class = PollFilter
