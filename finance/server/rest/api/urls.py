from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:tipo_conta_id>/details', views.detail, name='details')
]
