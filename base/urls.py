from django.urls import path
from . import views
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
#from .views import EventsListView


urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('events/', views.getEvents, name='events'),
    #path('events/', EventsListView.as_view(), name='events-list'),
    # path('products/', views.getProdcuts, name='products'),
    # path('magasin/', views.getMagasin, name='magasin'),
    # path('articlePost/', views.registerArticle, name='article_post'),
    # path('articleAll/', views.getAllArticle, name='article_all'),
    # path('api_schema', get_schema_view(title='Pastebin API', description='HandSwap'), name="api_shema"),
    
]