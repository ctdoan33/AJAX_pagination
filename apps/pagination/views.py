# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from models import *

def index(request):
    leads = Lead.objects.all()
    context = {
        "users" : leads[:10],
        "page_range" : range(2, (leads.count()-1)/10+2)
    }
    return render(request, "pagination/index.html", context)
def page(request, id):
    leads = Lead.objects.filter(first_name__contains=request.POST["name"])|Lead.objects.filter(last_name__contains=request.POST["name"])
    if request.POST["from_date"] != "":
        leads = leads.filter(registered__gte=request.POST["from_date"])
    if request.POST["to_date"] != "":
        leads = leads.filter(registered__lte=request.POST["to_date"])
    context = {
        "users" : leads[(int(id)-1)*10:int(id)*10]
    }
    return render(request, "pagination/page.html", context)
def search(request):
    leads = Lead.objects.filter(first_name__contains=request.POST["name"])|Lead.objects.filter(last_name__contains=request.POST["name"])
    if request.POST["from_date"] != "":
        leads = leads.filter(registered__gte=request.POST["from_date"])
    if request.POST["to_date"] != "":
        leads = leads.filter(registered__lte=request.POST["to_date"])
    context = {
        "users" : leads[:10],
        "page_range" : range(2, (leads.count()-1)/10+2)
    }
    return render(request, "pagination/result.html", context)
