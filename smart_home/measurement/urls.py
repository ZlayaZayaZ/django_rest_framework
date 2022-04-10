from django.urls import path
from .views import SensorView, SensorIdView, MeasurementsView

urlpatterns = [
    path('sensors/', SensorView.as_view()),
    path('sensors/<pk>/', SensorIdView.as_view()),
    path('measurements/', MeasurementsView.as_view()),
]
