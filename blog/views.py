from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from blog.models import PostModel


class BlogTemplateView(ListView):
    template_name = 'blog.html'
    queryset = PostModel.objects.order_by('-pk')


class BlogDetailView(DetailView):
    template_name = 'blog-detail.html'
    model = PostModel
