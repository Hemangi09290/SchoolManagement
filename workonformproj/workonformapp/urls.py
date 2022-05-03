from django.urls import path, include
from . import views

urlpatterns = [
    #path("", views.index, name="index"),
    path("", views.StudenListView.as_view(), name="student_change_list"),
    path("add/", views.StudenCreateView.as_view(), name="student_add"),
    path("<int:pk>/", views.StudenUpdateView.as_view(), name="student_change"),


]
