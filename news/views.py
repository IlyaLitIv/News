from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.core.paginator import Paginator 
from django.urls import resolve
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView 
from .models import News,Category
from .filters import NewsFilter
from .forms import NewsForm
from datetime import datetime
# from django.template.loader import render_to_string

from django.core.mail import EmailMultiAlternatives

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.core.mail import send_mail

from django.conf import settings
DEFAULT_FROM_EMAIL = settings.DEFAULT_FROM_EMAIL

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
        
        # send_mail(
        #     subject=form.name,
        #     message=form.description,
        #     from_email='me@litvinko.ru',
        #     recipient_list=['ilya.litvinko@gmail.com',],
        # )
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
    
class NewCategoryView(ListView):
    model = News
    template_name = 'category.html'
    context_object_name = 'news'
    ordering = ['-created_at']
    paginate_by = 10

    def get_queryset(self):
        self.id = resolve(self.request.path_info).kwargs['pk']
        c = Category.objects.get(id=self.id)
        queryset = News.objects.filter(Category=c)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        category = Category.objects.get(id=self.id)
        subscribed = category.subscribers.filter(email=user.email)
        if not subscribed:
            context['category'] = category
        
        return context

@login_required
def subscribe_to_category(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)

    if not category.subscribe.filter(id=user.id).exists():
        category.subscribe.add(user)
        email = user.email,
        html = render_to_string(
            'mail/subscribed.html',
            {
                'category': category,
                'user':user,
            },            
        )

        msg = EmailMultiAlternatives(
            subject=f'{category} subscription',
            body='',
            from_email=DEFAULT_FROM_EMAIL,
            to=[email,],
        )

        msg.attach_alternative(html, 'text/html')

        try:
            msg.send()
        except Exception as e:
            print(e)
        return redirect('news:index')
    return redirect(request.MERA.get('HTTP_REFERER'))

@login_required
def unsubscribe_from_category(request, pk):
    user = request.user
    c = Category.objects.get(id=pk)
    if c.subscribers.filter(id=user.id).exists():
        c.subscribers.remove(user)
    return redirect('users:index')
