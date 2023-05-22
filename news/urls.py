from django.urls import path
from .views import NewsList, NewsDetail, NewsSearch, NewsCreateView, NewsUpdateView, NewsDeleteView, NewCategoryView, subscribe_to_category, unsubscribe_from_category


app_name = 'news'
urlpatterns = [
    path('', NewsList.as_view()),
    path('<int:pk>', NewsDetail.as_view(), name='new'),
    path('search', NewsSearch.as_view()),
    path('news/int:pk', NewsDetail.as_view(), name='details'),
    path('new_create/<int:pk>/', NewsCreateView.as_view(), name='new_create'),
    path('new_delete/<int:pk>/', NewsDeleteView.as_view(), name='new_delete'),
    path('new_update/<int:pk>/', NewsUpdateView.as_view(), name='new_update'),
    path('category/<int:pk>/', NewCategoryView.as_view(), name='category'),
    path('subscribe/<int:pk>', subscribe_to_category, name='subscribe'),
    path('unsubscribe/<int:pk>', unsubscribe_from_category, name='unsubscribe'),
]