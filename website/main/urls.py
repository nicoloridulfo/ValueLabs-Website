from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("blog", views.blog, name="blog"),
    path("code", views.code, name="code"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
]