from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('posts/', include('news.urls')),
    path('news/', include('news.urls')),
    path('sign/', include(('sign.urls', 'sign'), namespace='sign')),
    path('accounts/', include('allauth.urls')),

]
