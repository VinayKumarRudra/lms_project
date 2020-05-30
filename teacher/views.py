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
from authentication.models import User_Category,Teacher_Class,Student
from authentication.forms import ClassSection

@login_required(login_url="/login/")
def index(request):
    return render(request, "tindex.html")


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

@login_required(login_url="/login/")
def profile(request):
    base_template_name=None
    username = None
    choices=None
    if request.user.is_authenticated:
        username = request.user.username
        data=Profile.objects.filter(username=username).values()
        user_category_values = User_Category.objects.get(username = username)
        choices=user_category_values.get_user_category_display()
        if user_category_values.user_category == 'T':
            base_template_name='layouts/tbase.html'
    return render(request,'profile.html',{'username':data,'choices':choices,'base_template_name':base_template_name}) 


def std_section(request):
    username = None
    classname=None
    standard=None
    section=None
    student_class_section=None
    if request.user.is_authenticated:
        username = request.user.username
        teacher_class_section=Teacher_Class.objects.filter(staffid=username).values()
        if request.method == 'POST':
            form = ClassSection(request.POST)
            if form.is_valid():
                standard = form.cleaned_data['value']
                section =  form.cleaned_data['result']
                student_class_section=Student.objects.filter(std=standard,section=section)

    return render(request,'studententry.html',{'std':teacher_class_section,'section':teacher_class_section,'subcode':teacher_class_section,'studname':student_class_section})
