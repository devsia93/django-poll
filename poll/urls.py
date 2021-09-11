from rest_framework.routers import DefaultRouter

from poll.views import PollViewSet, QuestionViewSet

router = DefaultRouter()

router.register(r'polls', PollViewSet)
router.register(r'questions', QuestionViewSet)

urlpatterns = [
    *router.urls,
]
