from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import BlogPost
from .forms import BlogPostForm

# Create your views here.
def index(request):
    """The home page for blogs"""
    blogposts = BlogPost.objects.order_by('date_added')
    context = {'blogposts': blogposts}
    return render(request, 'blogs/index.html', context)

def new_blogpost(request):
    """Add a new blogpost."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = BlogPostForm()
    else:
        # POST data submitted; process data.
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:index'))
    
    context = {'form': form}
    return render(request, 'blogs/new_blogpost.html', context)

def edit_blogpost(request, blogpost_id):
    """Edit an existing blogpost."""
    blogpost = BlogPost.objects.get(id=blogpost_id)

    if request.method != 'POST':
        # Initial request; pre-fill form with the current blogpost.
        form = BlogPostForm(instance=blogpost)
    else:
        # POST data submitted; process data.
        form = BlogPostForm(instance=blogpost, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:index'))
        
    context = {'blogpost': blogpost, 'form': form}
    return render(request, 'blogs/edit_blogpost.html', context)
