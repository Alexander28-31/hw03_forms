from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PostForm
from .models import Group, Post, User
from .utils import get_page_pages


def index(request):
    """Выводит шаблоны главной страницы."""
    context = get_page_pages(
        Post.objects.select_related('author', 'group'), request)
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    """Выводит шаблон с группами постов."""
    group = get_object_or_404(Group, slug=slug)
    context = {
        'group': group,
    }
    context.update(get_page_pages(group.posts.all(), request))
    return render(request, 'posts/group_list.html', context)


def profile(request, username):
    """Выводит шаблон профайла пользователя."""
    author = get_object_or_404(User, username=username)
    posts = Post.objects.select_related('author')
    context = {
        'author': author,
        'posts': posts,
    }
    context.update(get_page_pages(
        Post.objects.filter(author=author), request))
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post = Post.objects.select_related('author', 'group').get(id=post_id)
    context = {
        'post': post,
    }
    context.update(get_page_pages(
        Post.objects.filter(author=post.author), request))
    return render(request, 'posts/post_detail.html', context)


@login_required
def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        form.save()
        return redirect('posts:profile', request.user)
    return render(request, 'posts/post_create.html', {'form': form})


@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    is_edit = True
    if post.author != request.user:
        return redirect('posts:post_detail', post.pk)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        post = form.save(commit=False)
        form.save()
        return redirect('posts:post_detail', post_id=post_id)
    return render(request, 'posts/post_create.html', {'form': form,
                                                      'is_edit': is_edit})
