from django.urls import path
from . import views

appName = 'djangoapp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
