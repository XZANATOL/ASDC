from django.urls import path
from . import views

urlpatterns = [
	path("upload/", views.upload, name="upload"),
	path("query/<int:key>", views.read, name="read"),
	path("update/<int:key>", views.update, name="update"),
	path("delete/<int:key>", views.delete, name="delete"),
]