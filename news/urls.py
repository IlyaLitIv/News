from django.urls import path
from .views import NewsList, NewsDetail, NewsSearch, NewsCreateView, NewsUpdateView, NewsDeleteView

 
urlpatterns = [
    path('', NewsList.as_view()),
    path('<int:pk>', NewsDetail.as_view(), name='new'),
    path('search', NewsSearch.as_view()),
    path('new_create/<int:pk>/', NewsCreateView.as_view(), name='new_create'),
    path('new_delete/<int:pk>/', NewsDeleteView.as_view(), name='new_delete'),
    path('new_update/<int:pk>/', NewsUpdateView.as_view(), name='new_update'),
]