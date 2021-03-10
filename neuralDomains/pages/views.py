from django.shortcuts import render
from django.http import HttpResponse,FileResponse
from django.core.files.storage import FileSystemStorage

# Create your views here.
def about_view(request,*args, **kwargs):
    """
    Home page view (not sure what to display yet)
    """
    return render(request,'about.html',{})


def home_view(request,*args, **kwargs):
    """
    page view to display the author of the model
    """
    context = {
        'author1':'Henri Vandersleyen',
        'github1':'https://github.com/Vanderscycle',
    }
    return render(request,'home.html',context)

