from django.urls import path

from . import views

urlpatterns = [
    # ex: /
    path('', views.index_view, name='index'),
    path('arithmetic', views.arithmetic_view, name='arithmetic'),
]
