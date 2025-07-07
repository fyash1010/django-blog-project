from django.shortcuts import render
from .models import BlogPost, Category
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404
from .forms import CustomUserCreationForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .forms import BlogPostForm

# Blog views for the blog application
def home(request):
    query = request.GET.get('q', '')
    category_filter = request.GET.get('category', '')

    posts = BlogPost.objects.all().order_by('-created_at')

    if query:
        posts = posts.filter(Q(title__icontains=query) | Q(content__icontains=query))

    if category_filter:
        posts = posts.filter(categories__id=category_filter)

    paginator = Paginator(posts, 5)  # 5 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categories = Category.objects.all()

    return render(request, 'blog/home.html', {
        'page_obj': page_obj,
        'categories': categories,
        'query': query,
        'selected_category': category_filter,
    })

# Detail view for a single blog post
def post_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

# User registration and authentication views
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

# Login required views for creating, editing, and deleting posts
@login_required
def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Assign current user as author
            post.save()
            form.save_m2m()  # Save many-to-many field (categories)
            return redirect('post_detail', pk=post.pk)
    else:
        form = BlogPostForm()
    return render(request, 'blog/post_form.html', {'form': form, 'title': 'Create Post'})

@login_required
def edit_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)

    if post.author != request.user:
        raise PermissionDenied()

    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form, 'title': 'Edit Post'})

@login_required
def delete_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)

    if post.author != request.user:
        raise PermissionDenied()

    if request.method == 'POST':
        post.delete()
        return redirect('home')

    return render(request, 'blog/post_confirm_delete.html', {'post': post})
