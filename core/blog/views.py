from django.shortcuts import render
from django.views.generic.base import TemplateView
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

