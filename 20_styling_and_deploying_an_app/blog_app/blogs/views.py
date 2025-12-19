from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import BlogPost
from .forms import BlogPostForm

# Create your views here.
def index(request):
    """The home page for blogs"""
    blogposts = BlogPost.objects.order_by('-date_added')
    context = {'blogposts': blogposts}
    return render(request, 'blogs/index.html', context)

@login_required
def new_blogpost(request):
    """Add a new blogpost."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = BlogPostForm()
    else:
        # POST data submitted; process data.
        form = BlogPostForm(request.POST)
        if form.is_valid():
            new_blogpost = form.save(commit=False)
            new_blogpost.owner = request.user
            new_blogpost.save()
            return HttpResponseRedirect(reverse('blogs:index'))
    
    context = {'form': form}
    return render(request, 'blogs/new_blogpost.html', context)

@login_required
def edit_blogpost(request, blogpost_id):
    """Edit an existing blogpost."""
    blogpost = BlogPost.objects.get(id=blogpost_id)
    if blogpost.owner != request.user:
        raise Http404

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
