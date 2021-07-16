from django.urls import path

from blog.views import BlogTemplateView, BlogDetailView, CommentCreateView

app_name = 'blog'

urlpatterns = [
    path('<int:pk>/', BlogDetailView.as_view(), name='detail'),
    path('<int:pk>/comment/', CommentCreateView.as_view(), name='comment'),
    path('', BlogTemplateView.as_view(), name='list'),
]
