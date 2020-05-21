from django.urls import path

from attributes.views import AttributesView

urlpatterns = [
    path('', AttributesView.as_view()),
]
