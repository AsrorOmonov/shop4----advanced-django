from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from blog.forms import CommentModelForm
from blog.models import PostModel


class BlogListView(ListView):
    template_name = 'blog.html'
    paginate_by = 2

    def get_queryset(self):
        qs = PostModel.objects.order_by('-pk')
        tag = self.request.GET.get('tag')

        if tag:
            qs = qs.filter(tags__title=tag)
        return qs


class BlogDetailView(DetailView):
    template_name = 'blog-detail.html'
    model = PostModel


class CommentCreateView(CreateView):
    form_class = CommentModelForm

    def form_valid(self, form):
        form.instance.post = get_object_or_404(PostModel, pk=self.kwargs.get('pk'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:detail', kwargs={'pk': self.kwargs.get('pk')})





