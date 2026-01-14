from django.contrib import admin
from django.urls import path
from apps.scraper import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('scrape/', views.scrape, name='scrape'),
    path('clear/', views.clear_links, name='clear'),
    path('download/', views.download_links, name='download'),
]
