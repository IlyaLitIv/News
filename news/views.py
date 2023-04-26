from django.shortcuts import render
from django.core.paginator import Paginator 

from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView 
from .models import News,Category
from .filters import NewsFilter
from .forms import NewsForm
from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

# Create your views here.


class NewsList(ListView):
    model = News
    template_name = 'news.html'
    context_object_name = 'news'
    queryset = News.objects.order_by('-id')
    paginate_by = 5
    form_class = NewsForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())
        context['categories'] = Category.objects.all()
        context['form'] = NewsForm()
        return context
    def post(self, request, *args, **kwargs):        
        form = self.form_class(request.POST)
 
        if form.is_valid():
            form.save()
        return super().get(request, *args, **kwargs)


class NewsDetail(DetailView):
    model = News
    template_name = 'new.html'
    context_object_name = 'new'


class NewsCreateView(CreateView):
    template_name = 'new_create.html'
    form_class = NewsForm


class NewsUpdateView(LoginRequiredMixin,UpdateView):
    template_name = 'new_create.html'
    form_class = NewsForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return News.objects.get(pk=id)


class NewsDeleteView(DeleteView):
    template_name = 'new_delete.html'
    queryset = News.objects.all()
    success_url = '/news/'
    context_object_name = 'new_d'


class NewsSearch(ListView):
    model = News
    template_name = 'search.html'
    context_object_name = 'news'
    queryset = News.objects.order_by('id')
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())
        return context
    