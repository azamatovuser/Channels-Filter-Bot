from django.urls import path
from .views import GroupAPIView, PersonCreateAPIView, GroupFilterAPIView


urlpatterns = [
    path('person/create/', PersonCreateAPIView.as_view()),
    path('list/groups/', GroupAPIView.as_view()),
    path('list/groups/filter/', GroupFilterAPIView.as_view()),
]