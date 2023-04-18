from django.urls import path

from measurement.views import SensorsListCreateView, SensorView, MeasurementCreateView, SensorChangeView

urlpatterns = [
    path('sensors/', SensorsListCreateView.as_view()),
    path('measurements/', MeasurementCreateView.as_view()),
    path('sensors/<pk>/', SensorChangeView.as_view()),
    path('sensorspk/<pk>/', SensorView.as_view())
]




