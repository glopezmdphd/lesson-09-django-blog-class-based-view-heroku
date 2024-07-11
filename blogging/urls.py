from django.urls import path
from django.contrib.auth import views as auth_views
from blogging.views import BlogListView, BlogDetailView, register, add_post

urlpatterns = [
    path("", BlogListView.as_view(), name="blog_index"),
    path("posts/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
    path("add/", add_post, name="add_post"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("register/", register, name="register"),
]
