from django.shortcuts import render
from .models import *
def home_page(Request):
    return render(Request,'index.html')

def about_page(Request):
    return render(Request,'about.html')

def contact_page(Request):
    return render(Request,'contact.html')

def gallery_page(Request):
    return render(Request,'gallery.html')

def pricing_page(Request):
    return render(Request,'pricing.html')

def single_page(Request):
    return render(Request,'single.html')


def portfolio_page(Request):
    portfolio=Portfolio.objects.all()
    return render(Request,'portfolio.html',{'portfolio':portfolio})


def portfolio_details(Request,name,id):
    data=Portfolio.objects.get(id=id)
    data2=PortfolioImage.objects.filter(portfolio=data)

    return render(Request,'portfolio-details.html',{'data':data,'data2':data2})

