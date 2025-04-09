from django.shortcuts import render 
from django.http import HttpResponse 

from visits.models import PageVisit

import pathlib

this_dir = pathlib.Path(__file__).resolve().parent


def home_page_views(request,*args,**kwargs):
    qs = PageVisit.objects.all()
    Page_qs = PageVisit.objects.filter(path = request.path)
    my_title = "Page One"
    my_context ={
        "page_title": my_title,
        "page_visit_count" : Page_qs.count,
        "totale_visit" : qs.count
    }
    path = request.path
    print(path)
    html_templates ="home.html"
    PageVisit.objects.create(path = request.path)
    #html_file_path = this_dir / "home.html"
    #html_ = html_file_path.read_text()
    return render(request,html_templates,my_context)



def page_views(request,*args,**kwargs):
    print(this_dir)
    page_title = "Page Two"
    context={
        "tilte":page_title,
    }
    html_ =""
    html_file_path = this_dir / "home.html"
    html_ = html_file_path.read_text()
    return HttpResponse(html_)