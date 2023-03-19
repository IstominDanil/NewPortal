from django import forms
from django.core.exceptions import ValidationError
from django_filters import DateFilter
from .models import Post

class PostForm(forms.ModelForm):
    header = forms.CharField(min_length=3)
    time_post = DateFilter(field_name='time_in', widget=forms.DateInput(attrs={'type': 'date'}), label='Поиск по дате',
                      lookup_expr='date__gte')
    class Meta:
        model = Post
        fields = [
            'author',
            'choice',
            'category',
            'header',
            'text',
        ]

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get('text')
        header = cleaned_data.get('header')

        if text == header:
            raise ValidationError(
                'Статья не должна быть идентична описанию.'
            )

        return cleaned_data
