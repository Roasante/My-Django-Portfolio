from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('projects/', views.projects, name='projects'),
    path('experience/', views.Experience, name='experience'),
    path('work-highlights/gridco/',views.gridco_gallery,name='gridco_gallery'),
    path('work-highlights/dzill/', views.dzill_gallery, name='dzill_gallery'),
    path('work-highlights/media/',views.media_gallery,name='media_gallery'),
    path('work-highlights/internship/',views.internship_gallery,name='internship_gallery')
]