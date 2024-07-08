from django.views.generic import ListView, DetailView
from blogging.models import Post

class BlogListView(ListView):
    template_name = 'blogging/list.html'
    queryset = Post.objects.exclude(published_date__exact=None).order_by('-published_date')

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blogging/detail.html'

