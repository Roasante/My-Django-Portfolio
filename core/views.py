from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')

def projects(request):
    return render(request, 'core/projects.html')

def Experience(request):
    return render(request, 'core/experience.html')

def gridco_gallery(request):
    return render(request,'core/gridco_gallery.html')

def dzill_gallery(request):
    return render(request,'core/dzill_gallery.html')

def media_gallery(request):
    return render(request,'core/media_gallery.html')

def internship_gallery(request):
    return render(request,'core/internship_gallery.html')