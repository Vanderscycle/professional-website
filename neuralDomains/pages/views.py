from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request,*args, **kwargs):
    """
    Home page view (not sure what to display yet)
    """
    return render(request,'home.html',{})


def about_view(request,*args, **kwargs):
    """
    page view to display the author of the model
    """
    context = {
        'author1':'Henri Vandersleyen',
        'github1':'https://github.com/Vanderscycle',
    }
    return render(request,'about.html',context)

