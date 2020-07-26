from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("new", views.new, name="new"),
    path("images/<int:img_id>/", views.img_view, name="img_view"),
]
