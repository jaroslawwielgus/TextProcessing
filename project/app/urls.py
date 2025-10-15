from django.urls import path
from . import views

urlpatterns = [
    path("", views.form, name="form"),
    path("wynik/", views.score, name="score")
]