from django.shortcuts import render

# Create your views here.
# Create your views here.
def project_view(request,*args, **kwargs):
    """
    Home page view (not sure what to display yet)
    """
    context = {
        'author1':'Henri Vandersleyen',
        'github1':'https://github.com/Vanderscycle',
    }
    return render(request,'project.html',context)

