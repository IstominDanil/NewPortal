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
    time_post = DateFilter(field_name='time_post',
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Поиск по дате',
        lookup_expr='date__gte')
    class Meta:
        model = Post
        fields = {
            'header': ['icontains'],
            'author': ['gt'],
        }