from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

def articles_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/articles_list.html', { 'articles': articles })

def article_detail(request, slug):
    return HttpResponse(slug)