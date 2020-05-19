from django.urls import path

from geolocation.views import GeolocationView

urlpatterns = [
    path('', GeolocationView.as_view()),
    path('<int:number>', GeolocationView.as_view())
]
