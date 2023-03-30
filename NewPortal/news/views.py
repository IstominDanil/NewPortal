from django.template.loader import render_to_string
from django.urls import reverse_lazy
from datetime import datetime
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect, render, reverse
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.mail import send_mail, EmailMultiAlternatives, mail_admins
from .models import Post, Appointment, Category
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


class CategoryDetail(LoginRequiredMixin, DetailView):
    model = Category
    template_name = 'post.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_sub'] = not (self.request.user.username in Category.objects.all().values('subscribers'))
        category = Category.objects.get(pk=self.kwargs['pk'])
        context['subscribers'] = category.subscribers.all()
        return context


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

class PostUpdate(LoginRequiredMixin, UpdateView):
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


class ProtectedView(LoginRequiredMixin, TemplateView):
    template_name = 'protected_page.html'


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_authors'] = not self.request.user.groups.filter(name = 'authors').exists()
        return context


class MyView(PermissionRequiredMixin, View):
    permission_required = ('<app>.<action>_<model>',
                           '<app>.<action>_<model>')


class AddProduct(PermissionRequiredMixin,CreateView):
    permission_required = ('news.add_post', )
    "//customize form view"


class AppointmentView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'make_appointment.html', {})

    def post(self, request, *args, **kwargs):
        appointment = Appointment(
            date=datetime.strptime(request.POST['date'], '%Y-%m-%d'),
            client_name=request.POST['client_name'],
            message=request.POST['message'],
        )
        appointment.save()

        # html_content = render_to_string(
        #     'appointment_created.html',
        #     {
        #         'appointment': appointment,
        #     }
        # )

        send_mail(
           subject= appointment.client_name,
           message = appointment.message,
           from_email='istomin.danil@mail.ru',
           recipient_list=[''],
        )



# @login_required
# def subscribe(request, pk):
#     user = request.user
#     subs = Category.objects.get('subscribers')
#
#     if user not in subs:
#         Category.subscribers.add(user)
#     return redirect('/')

        return redirect('appointments')