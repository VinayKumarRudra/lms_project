# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from authentication.models import Profile
from authentication.models import User_Category

@login_required(login_url="/login/")
def index(request):
    return render(request, "pindex.html")

def profile(request):
    base_template_name=None
    username = None
    choices=None
    if request.user.is_authenticated:
        username = request.user.username
        data=Profile.objects.filter(username=username).values()
        user_category_values = User_Category.objects.get(username = username)
        choices=user_category_values.get_user_category_display()
        if user_category_values.user_category == 'P':
            base_template_name='layouts/pbase.html'
    return render(request,'profile.html',{'username':data,'choices':choices,'base_template_name':base_template_name})

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template = request.path.split('/')[-1]
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'error-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'error-500.html' )
        return HttpResponse(html_template.render(context, request))
