from django.contrib import admin
from django.urls import path
from mainApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_page),
    path('about/',views.about_page),
    path('contact/',views.contact_page),
    path('gallery/',views.gallery_page),
    path('pricing/',views.pricing_page),
    path('single/',views.single_page),
    path('portfolio/',views.portfolio_page),
    path('portfolio-details/<str:name>-<int:id>/',views.portfolio_details),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
