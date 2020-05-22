from django.urls import path

from generator.views import GeneratorView

urlpatterns = [
    path('', GeneratorView.as_view()),
]