from django.shortcuts import render, get_object_or_404

from .models import Blogpost

# Create your views here. https://docs.djangoproject.com/en/2.2/topics/http/views/
def bloghome(request):
    blogposts = Blogpost.objects.all()
    # We used bloghome/bloghome.html instead of just home.html since we created a bloghome sub-template folder
    return render(request, 'bloghome/home.html', {'blogposts':blogposts})

# From DB Get a Blogpost model with primary key = blogpost_id
def blogpostdetails(request, blogpost_id):
    postdetails = get_object_or_404(Blogpost, pk=blogpost_id) #Gets the object from DB
    return render(request, 'bloghome/postdetail.html', {'postdetails':postdetails})
