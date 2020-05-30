# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from student import views

urlpatterns = [
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.
    re_path(r'^.*\.html', views.pages, name='pages'),

    # The home page
    path('student/', views.index, name='home'),
    path('studentprofile/', views.profile, name='studentprofile'),
    path('studentprofile/', views.upload_pic, name=''),
]
