from django_filters import FilterSet, ModelChoiceFilter
from .models import Post
from .forms import *


class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            'header': ['icontains'],
            'author': ['gt'],
        }

class SearchFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            'header': ['icontains'],
            'author': ['gt'],
        }