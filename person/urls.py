from django.urls import path

from person.views import PersonView, PersonCreateView

urlpatterns = [
    path('', PersonView.as_view()),
    path('<int:number>', PersonCreateView.as_view()),
]