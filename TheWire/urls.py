from django.urls import path
from . import views

urlpatterns = [
    path('the-wire', views.the_wire_view, name='the-wire'),
    path('submit-news', views.submit_news, name='submit-news'),
    path('news/<str:pk>/', views.view_news, name="view-selected-news"),
    path('browse-news', views.all_news, name='browse-news'),
    path('deleted-news/<str:pk>/', views.news_delete, name='delete-news'),
    path('api/news/', views.TheWireNewsListView.as_view(), name='news-api'),
]

