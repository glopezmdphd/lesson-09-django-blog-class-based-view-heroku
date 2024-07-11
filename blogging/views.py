from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from blogging.forms import PostForm
from blogging.models import Post
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import UserCreationForm

class BlogListView(ListView):
    model = Post
    template_name = 'blogging/list.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blogging/detail.html'

@login_required
def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect("blog_index")
    else:
        form = PostForm()
    return render(request, "blogging/add.html", {"form": form})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "blogging/register.html", {"form": form})


class BlogListView(ListView):
    template_name = "blogging/list.html"
    queryset = Post.objects.exclude(published_date__exact=None).order_by(
        "-published_date"
    )


class BlogDetailView(DetailView):
    model = Post
    template_name = "blogging/detail.html"
