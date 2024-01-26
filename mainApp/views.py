from django.shortcuts import render

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

