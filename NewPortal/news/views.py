from django.urls import reverse_lazy
from datetime import datetime
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .models import Post
from .filters import PostFilter, SearchFilter
from .forms import PostForm


class PostsList(ListView):
    model = Post
    ordering = 'choice'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = None
        context['filterset'] = self.filterset
        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'create.html'

    # def get_create_template_names(self):
    #     post = self.get_object()
    #     if post.POST_TYPES == post.POST_TYPES.news:
    #         self.template_name = 'news_edit.html'
    #     else:
    #         self.template_name = 'article_edit.html'
    #     return self.template_name

class PostUpdate(UpdateView, LoginRequiredMixin, TemplateView):
    form_class = PostForm
    model = Post
    template_name = 'create.html'

    # def get_update_template_names(self):
    #     post = self.get_object()
    #     if post.POST_TYPES == news:
    #         self.template_name = 'news_edit.html'
    #     else:
    #         self.template_name = 'article_edit.html'
    #     return self.template_name


class PostDelete(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('post_list')

    # def get_delete_template_name(self):
    #     post = self.get_object()
    #     if post.POST_TYPES == news:
    #         self.template_name = 'news_delete.html'
    #     else:
    #         self.template_name = 'article_delete.html'
    #     return self.template_name

class SearchList(ListView):
    model = Post
    ordering = 'choice'
    template_name = 'search.html'
    context_object_name = 'search'
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = SearchFilter(self.request.GET, queryset)
        return self.filterset.qs


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = None
        context['filterset'] = self.filterset
        return context


class IndexView(LoginRequiredMixin,TemplateView):
    template_name = 'create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_premium'] = not self.request.user.groups.filter(name = 'premium').exists()
        return context

@login_required
def upgrate_me(request):
    user = request.user
    premium_group = Group.objects.get(name = 'premium')
    if not request.user.groups.filter(name = 'premium').exists():
        premium_group.user_set.add(user)
    return redirect('/')