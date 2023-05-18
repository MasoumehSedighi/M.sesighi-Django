from django.urls import path
from . import views
from django.views.generic import TemplateView, RedirectView

app_name = "blog"

urlpatterns = [
    # function base views
    # path('fbv_index', views.indexView, name='fbv_index'),
    # path('cbv_index', TemplateView.as_view(template_name="index.html", extra_context={'name':'ali'}))
    # path('fbv_redirect_django', views.redirectToDjango, name = "fbv_redirect_django"),
    
    # class base views
    path('cbv_index', views.IndexView.as_view(), name ="cbv_index"),
    path("go-to-cbv_index/", RedirectView.as_view(pattern_name="blog:cbv_index"),name="go-to_cbv_index"),
    path("cbv_redirect_django/<int:pk>/", views.RedirectToDjango.as_view(), name = "cbv_redirect_django")

]
