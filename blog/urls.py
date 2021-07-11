from django.urls import path

from blog.views import BlogTemplateView, BlogDetailView
from pages.views import ContactTemplateView, IndexTemplateView

app_name = 'blog'

urlpatterns = [
    path('<int:pk>/', BlogDetailView.as_view(), name='detail'),
    path('', BlogTemplateView.as_view(), name='list'),
]
