"""Defines URL patterns for blogs."""

from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    # Home page
    path("", views.index, name='index'),

    # Page for adding new blogposts
    path("new_blogpost/", views.new_blogpost, name='new_blogpost'),

    # Page for editing a blogpost
    path("edit_blogpost/<int:blogpost_id>/", views.edit_blogpost, name='edit_blogpost')
]
