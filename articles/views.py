from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from .models import Article

def articles_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/articles_list.html', { 'articles': articles })

def article_detail(request, slug):
    # return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_details.html', { 'article': article })

@login_required(login_url='/accounts/login')
def article_create(request):
    return render(request, 'articles/article_create.html')
