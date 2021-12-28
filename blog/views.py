from django.db.models.base import Model

from django.shortcuts import render, get_object_or_404
from .models import Post


def get_date(all_posts):
    return all_posts['date']


def starting_page(request):
    slice_posts = Post.objects.all().order_by("-post_date")[:3]
    return render(request, "blog/index.html", {
        "posts": slice_posts
    })


def posts(request):
    all_posts = Post.objects.all().order_by("-post_date")
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })


def post_detail(request, slug):
    identified_post = get_object_or_404(Post, post_slug=slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post,
        "tags": identified_post.post_tag.all()
    })
