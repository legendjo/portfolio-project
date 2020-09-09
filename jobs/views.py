from django.shortcuts import render

from .models import Job

# Create your views here. https://docs.djangoproject.com/en/2.2/topics/http/views/
def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})  # jobs/home.html since home.html is in /jobs subfolder in templates
