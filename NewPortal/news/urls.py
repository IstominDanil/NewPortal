from django.urls import path
from .views import PostsList, PostDetail, PostCreate, PostUpdate, PostDelete, SearchList

urlpatterns = [
    path('', PostsList.as_view(), name='post_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('search/', SearchList.as_view(), name='search'),
    path('news/create/', PostCreate.as_view(), name='news_create'),
    path('article/create/', PostCreate.as_view(), name='article_create'),
    path('news/update/', PostUpdate.as_view(), name='news_update'),
    path('article/update/', PostUpdate.as_view(), name='article_update'),
    path('news/delete/', PostDelete.as_view(),name='news_delete'),
    path('article/delete/', PostDelete.as_view(), name='article_delete'),

]