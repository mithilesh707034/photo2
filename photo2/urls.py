from django.contrib import admin
from django.urls import path
from mainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_page),
    path('about/',views.about_page),
    path('contact/',views.contact_page),
    path('gallery/',views.gallery_page),
    path('pricing/',views.pricing_page),
    path('single/',views.single_page),

]
