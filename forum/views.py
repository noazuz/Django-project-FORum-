from django.shortcuts import render, redirect
from .models import Category, Post
from django.db.models import F
from .forms import PostAddForm, LoginForm, RegistrationForm
from django.contrib.auth import login, logout
from django.contrib import messages

def Index(request):
    # Main page
    posts = Post.objects.all()
    categories = Category.objects.all()
    context = {
        'title': 'Forum',
        'posts': posts,
        'categories': categories,
    }
    return render(request, 'forum/index.html', context)


def category_list(request, pk):
    # Reaction on pressed button of category
    posts = Post.objects.filter(category_id=pk)
    categories = Category.objects.all()
    context = {
        'title': posts[0].category,
        'posts': posts,
        'categories': categories,
    }
    return render(request, 'forum/index.html', context)


def post_detail(request, pk):
    # Page of article
    article = Post.objects.get(pk=pk)
    Post.objects.filter(pk=pk).update(watched=F('watched') + 1)
    ext_post = Post.objects.all().exclude(pk=pk).order_by('-watched')
    context = {
        'title': article.title,
        'post': article,
        'ext_posts': ext_post,
    }
    return render(request, 'forum/article_detail.html', context)


def add_post(request):
    # Add a article by user, without admin
    if request.method == 'POST':
        form = PostAddForm(request.POST, request.FILES)
        if form.is_valid():
            post = Post.objects.create(**form.cleaned_data)
            post.save()
            return redirect('post_detail', post.pk)
    else:
        form = PostAddForm()

    context = {
        'form': form,
        'title': "Add a article",
    }
    return render(request, 'forum/article_add_form.html', context)


def user_login(request):
    # Auth user
    if request.method =='POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Success authorization')
            return redirect('Index')
    else:
        form = LoginForm()

    context = {
        'title': 'Auth user',
        'form': form,
    }
    return render(request, 'forum/login_form.html', context)

def user_logout(request):
    # Logout user
    logout(request)
    messages.error(request, 'Success logout')
    return redirect('Index')


def user_register(request):
    # Register user
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Success registration. Please login')
            return redirect('login')
    else:
        form = RegistrationForm()
    context = {
        'title': 'Registration user',
        'form': form,
    }
    return render(request, 'forum/registration_form.html', context)