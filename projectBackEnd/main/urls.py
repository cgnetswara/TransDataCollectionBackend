from django.urls import path, include
from . import views

urlpatterns = [
    path('getTen/<IMEI>', views.getTen),
    path('submitAnswer/<IMEI>/<int:qId>/<answerGiven>', views.submitAnswer)
]