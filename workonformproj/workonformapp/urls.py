from django.urls import path, include
from . import views

urlpatterns = [
    #path("", views.home_view, name="index"),
    path("", views.list_view, name="student_change_list"),
    path("add/", views.create_view, name="student_add"),
    path("add/", views.load_cities, name="load_cities"),
    path("<int:pk>/", views.update_view, name="student_change"),


]
