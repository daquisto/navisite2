# serial/urls.py
from django.urls import path
from .views import GuitarAdd, GuitarDelete, GuitarDetail, GuitarUpdate, HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("guitar/<int:pk>", GuitarDetail.as_view(), name="guitar_detail"),
    path("guitar/add", GuitarAdd.as_view(), name="guitar_add"),
    path("guitar/update/<int:pk>", GuitarUpdate.as_view(), name="guitar_update"),
    path("guitar/delete/<int:pk>", GuitarDelete.as_view(), name="guitar_delete"),
]
