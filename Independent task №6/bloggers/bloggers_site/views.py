from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Blogger, News


def blogger_list(request):
    bloggers = Blogger.published.all()
    return render(request, 'bloggers/blogger/list.html', {'bloggers': bloggers})


def blogger_detail(request, slug):
    blogger = get_object_or_404(Blogger, slug=slug, status=Blogger.Status.PUBLISHED)
    content_pieces = blogger.content_pieces.all()
    return render(request, 'bloggers/blogger/detail.html', {'blogger': blogger,
        'content_pieces': content_pieces})
def home(request):
    all_news = News.published.all()
    return render(request, 'bloggers/home.html', {'all_news': all_news})
def blogger_news(request):
    return redirect('bloggers:home')
def i_am(request):
    return HttpResponse("<h1>Сторінка зі мною</h1><p>Цей маршрут спрацював, тому що він перший в урл але інформації про мене немає.</p>")