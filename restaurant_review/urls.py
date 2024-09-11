from django.urls import path

from . import views

app_name = 'restaurant_review'

urlpatterns = [
    path('', views.index, name='index'),
    # other URL patterns...
]
