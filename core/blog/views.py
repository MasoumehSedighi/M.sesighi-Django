from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .forms import PostForm
from .models import Post

# Create your views here.

def indexView(request):
    """
    a function bases view to show index page
    """
    context = {"name":"Mary"}
    return render(request,"index.html", context)


class IndexView(TemplateView):
    """
    a class view to show index page
    """
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "ali"
        context["posts"] = Post.objects.all()
        return context


def redirectToDjango(request):
    """
    a function bases view to redirect Django site
    """

    return redirect("https://www.djangoproject.com/")


class RedirectToDjango(RedirectView):
    url = "https://www.djangoproject.com/"

    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs["pk"])
        print(post)
        return super().get_redirect_url(*args, **kwargs)

class PostListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = "blog.view_post"
    # model = Post
    # queryset = Post.objects.all()
    queryset = Post.objects.filter(status=True)
    context_object_name = 'posts'
    paginate_by = 2
    ordering = 'id'


    # def get_queryset(self) -> QuerySet[Any]:
    #     posts =  Post.objects.filter(status=False)
    #     return posts

class PostDetailView(LoginRequiredMixin, DetailView):
    # permission_required = "blog.view_post"
    model = Post


'''
class PostCreateView(FormView):
    """
    create a post 
    """
    template_name = "blog/post_create.html"
    form_class = PostForm
    success_url = "/blog/post/"

    def form_valid(self, form: Any) -> HttpResponse:
        form.save()
        return super().form_valid(form)
'''

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    # fields = ['author', 'title', 'content', 'status', 'category', 'published_date']
    form_class = PostForm
    success_url = "/blog/post/"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostEditView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    success_url = '/blog/post/'

class PostDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    permission_required = "blog.delete_post"
    model = Post
    success_url = "/blog/post/"