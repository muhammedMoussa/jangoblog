from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from . import views
from articles import views as article_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles', include('articles.urls')),
    path('accounts', include('accounts.urls')),
    path('about/', views.about, name='about'),
    path('', article_views.articles_list, name='home'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)