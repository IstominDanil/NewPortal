from django.urls import path
from .views import PostsList, PostDetail, PostCreate, PostUpdate, PostDelete, SearchList, upgrate_me, IndexView

urlpatterns = [
    path('', PostsList.as_view(), name='post_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    # path('create/', PostCreate.as_view(), name='post_create'),
    # path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
    # path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('search/', SearchList.as_view(), name='search'),
    path('create/', PostCreate.as_view(), name='create'),
    path('<int:pk>/update/', PostUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', PostDelete.as_view(),name='delete'),
    path('upgrate/', upgrate_me, name='upgrate'),
    path('', IndexView.as_view()),

]