from django.shortcuts import render
from django.http import FileResponse, Http404
from dotenv import load_dotenv

from pathlib import Path
import os

# Create your views here.
def resume_view(request,*args, **kwargs):
    load_dotenv()
    context = {
        'ADOBE_API_KEY' : os.getenv('ADOBE_API_KEY')
    }
    return render(request,'resume.html',context)

def home_view(request,*args, **kwargs):
    """
    page view to display the author of the model
    """
    context = {
        'author1':'Henri Vandersleyen',
        'github1':'https://github.com/Vanderscycle',
    }
    return render(request,'home.html',context)

