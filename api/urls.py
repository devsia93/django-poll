from django.conf import settings
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication

urlpatterns = []

if settings.DEBUG:
    schema_view = get_schema_view(openapi.Info(title="Polls",
                                               default_version='v1',
                                               description="API Documentation",
                                               contact=openapi.Contact(email="ivan.serov37@gmail.com"),
                                               ),
                                  public=False,
                                  permission_classes=(permissions.IsAuthenticated,),
                                  authentication_classes=(SessionAuthentication,))

    urlpatterns += [
        re_path(r'^doc(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
        re_path(r'^doc/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]

urlpatterns += [
    path('polls/', include('poll.urls')),
]