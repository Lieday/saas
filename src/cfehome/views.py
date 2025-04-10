from django.shortcuts import render 
from django.http import HttpResponse 

from visits.models import PageVisit

import pathlib

this_dir = pathlib.Path(__file__).resolve().parent


def home_views(request,*args,**kwargs):
    return about_views(request,*args,**kwargs)



def about_views(request,*args,**kwargs):
    qs = PageVisit.objects.all()
    Page_qs = PageVisit.objects.filter(path = request.path)
    my_title = "Page One"
    html_templates ="home.html"
    try:
        persontage = (Page_qs.count() *100.0) /qs.count()
    except:
        persontage = 0
    my_context ={
        "page_title": my_title,
        "page_visit_count" : Page_qs.count,
        "percentage" : persontage,
        "totale_visit" : qs.count
    }
    path = request.path
    print(path)
    
    PageVisit.objects.create(path = request.path)
    #html_file_path = this_dir / "home.html"
    #html_ = html_file_path.read_text()
    return render(request,html_templates,my_context)