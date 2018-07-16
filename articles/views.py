from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Article
from . import forms

def articles_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/articles_list.html', { 'articles': articles })

def article_detail(request, slug):
    # return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_details.html', { 'article': article })

@login_required(login_url='/accounts/login')
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            editable_form = form.save(commit=False)
            editable_form.author = request.user
            editable_form.save()
            return redirect('list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', { 'form': form })
