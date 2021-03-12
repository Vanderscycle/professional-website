from django.shortcuts import render
from django.http import FileResponse, Http404

def pdf_view(request):
    BASE_DIR = Path(__file__).resolve().parent.parent
    coverLetterFilePath = os.path.join(BASE_DIR,'media/')
    try:
        return FileResponse(open(coverLetterFilePath + 'HenriVandersleyenCV.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

from pathlib import Path
import os

# Create your views here.
def resume_view(request,*args, **kwargs):

    context = {

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

