from django.urls import path

from metrics.views import MetricsView

urlpatterns = [
    path('', MetricsView.as_view()),
]