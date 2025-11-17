from django.shortcuts import render, get_object_or_404, redirect
from .models import Blogger

def blogger_list(request):
    bloggers = Blogger.published.all()
    return render(request, 'bloggers/blogger/list.html', {'bloggers': bloggers})


def blogger_detail(request, id):
    blogger = get_object_or_404(Blogger, id=id, status=Blogger.Status.PUBLISHED)
    return render(request, 'bloggers/blogger/detail.html', {'blogger': blogger})
def home(request):
    latest_bloggers = Blogger.published.all()[:5]
    return render(request, 'bloggers/home.html', {'recent_bloggers': latest_bloggers})
def news(request):
    return redirect('bloggers:home')