from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('fbv_index', views.indexView, name='fbv_index'),
    path('cbv_index', TemplateView.as_view(template_name="index.html", extra_context={'name':'ali'}))

]
