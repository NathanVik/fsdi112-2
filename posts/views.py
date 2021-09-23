from django.views.generic import ListView, DetailView
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = "post_list.html"
    context_object_name = "post_list"

class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
