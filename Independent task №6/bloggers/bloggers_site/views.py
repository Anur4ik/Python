from django.shortcuts import render, get_object_or_404, redirect
from .models import Blogger, News


def blogger_list(request):
    bloggers = Blogger.published.all()
    return render(request, 'bloggers/blogger/list.html', {'bloggers': bloggers})


def blogger_detail(request, id):
    blogger = get_object_or_404(Blogger, id=id, status=Blogger.Status.PUBLISHED)
    content_pieces = blogger.content_pieces.all()
    return render(request, 'bloggers/blogger/detail.html', {'blogger': blogger,
        'content_pieces': content_pieces})
def home(request):
    latest_news = News.published.all()[:5]
    return render(request, 'bloggers/home.html', {'latest_news': latest_news})
def blogger_news(request):
    all_news = News.published.all()
    return render(request, 'bloggers/news.html', {'all_news': all_news})
