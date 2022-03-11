from pyexpat import model
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import MusicAlbum, News, Tracks
from .models import Band
from django.shortcuts import HttpResponse 

# Create your views here.

class indexView(ListView):
    model = News
    template_name = 'dark/index.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(indexView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books  
        context['bands'] = Band.objects.all();
        context['title_page'] = 'Все новости'

        return context

class indexBandView(ListView):
    model = News
    template_name = 'dark/index.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(indexBandView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books

        band_slug = self.kwargs['slug']
        context['bands'] = Band.objects.all()  
      

        obj = get_object_or_404(Band, slug=band_slug)
        context['title_page'] = f'Новости по группе {band_slug}'
        if obj is None:
           context['news'] = [] 
        else:

           b = Band(obj)
           

           context['news'] = News.objects.filter(band=obj)
           context['title_page'] = f'Новости по группе {obj}' 

        return context


class BandsView(ListView):
    model = Band
    template_name = 'dark/Bands.html'
    context_object_name = 'bands'

    def get_context_data(self, **kwargs):
         context = super(BandsView, self).get_context_data(**kwargs)
         context['title_page'] = 'Список формаций'
         context['news'] = News.objects.all()
         return context

class NewsDetailView(DetailView):    
    model = News
    template_name = 'dark/news_detail.html'
    context_object_name = 'detail'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(NewsDetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['bands'] = Band.objects.all()
        
        return context

class BandDetailView(DetailView):    
    model = Band
    template_name = 'dark/band_detail.html'
    context_object_name = 'detail'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(BandDetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['bands'] = Band.objects.all()
        band_slug = self.kwargs['slug']
        obj = get_object_or_404(Band, slug=band_slug)
        context['albums'] = MusicAlbum.objects.filter(band=obj)
        context['tracks'] = Tracks.objects.filter(band=obj)
        context['news'] = News.objects.filter(band=obj)
        return context        
# def index(request):
  #  return render(request, 'dark/index.html')