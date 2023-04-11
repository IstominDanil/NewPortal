from django.urls import path
from .views import PostsList, CategoryListView, PostCreate, PostUpdate, \
    PostDelete, SearchList, IndexView, AppointmentView, IndexViews

urlpatterns = [
    path('', PostsList.as_view(), name='post_list'),
    path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
    # path('create/', PostCreate.as_view(), name='post_create'),
    # path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
    # path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('search/', SearchList.as_view(), name='search'),
    path('create/', PostCreate.as_view(), name='create'),
    path('<int:pk>/update/', PostUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', PostDelete.as_view(),name='delete'),
    path('index/', IndexView.as_view()),
    path('appointments/', AppointmentView.as_view(), name='appointments'),
    path('celery/', IndexViews.as_view(), name='celery'),

]