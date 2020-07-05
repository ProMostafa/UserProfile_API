
from django.urls import path ,include
from .views import HellowApiView ,HellowApiViewSets ,ProfileApiViewSets ,UserLoginApiView ,UserProfileFeedViewSet
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('hellow',HellowApiViewSets,basename="hellow")
router.register('profile',ProfileApiViewSets)
router.register('feed',UserProfileFeedViewSet)

urlpatterns = [
     path('hellow_view',HellowApiView.as_view(),name="apibase"),
     path('login/',UserLoginApiView.as_view()),
      path('',include(router.urls)),
]
