from django.urls import path

from person.views import PersonView

urlpatterns = [
    path('', PersonView.as_view()),
]