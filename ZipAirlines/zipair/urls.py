from django.urls import path

from . import views


urlpatterns = [
    path('assess', views.Assess_Planes.as_view(), name='assess_plane')
]
