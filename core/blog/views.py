from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import TemplateView, RedirectView
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
