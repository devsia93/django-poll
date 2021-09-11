from django_filters import rest_framework


class CharInFilter(rest_framework.BaseInFilter, rest_framework.CharFilter):
    pass


class NumberInFilter(rest_framework.BaseInFilter, rest_framework.NumberFilter):
    pass
