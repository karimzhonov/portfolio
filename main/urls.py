from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('rest/contact/', ContactRestView.as_view()),
]

handler404 = hand404
