from django.urls import path
from . import views



urlpatterns = [
    path('', views.indexView.as_view(), name='news'),
    path('news/<slug:slug>', views.NewsDetailView.as_view(), name='news_detail'),
    path('list/', views.BandsView.as_view(), name='list'),
    path('bands/<slug:slug>', views.indexBandView.as_view(), name='bands'),
    path('info/<slug:slug>', views.BandDetailView.as_view(), name='info')


]