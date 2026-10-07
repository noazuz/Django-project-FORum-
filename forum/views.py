from django.shortcuts import render
from .models import Category, Post
from django.db.models import F
from .forms import PostAddForm


def Index(request):
    # MAIN PAGE
    posts = Post.objects.all()
    categories = Category.objects.all()
    context = {
        'title': 'Forum',
        'posts': posts,
        'categories': categories,
    }
    return render(request, 'forum/index.html', context)


def category_list(request, pk):
    # REACTION ON PRESSED BUTTON OF CATEGORY
    posts = Post.objects.filter(category_id=pk)
    categories = Category.objects.all()
    context = {
        'title': posts[0].category,
        'posts': posts,
        'categories': categories,
    }
    return render(request, 'forum/index.html', context)


def post_detail(request, pk):
    # PAGE OF ARTICLE
    article = Post.objects.get(pk=pk)
    Post.objects.filter(pk=pk).update(watched=F('watched') + 1)
    ext_post = Post.objects.all().order_by('-watched')[:5]
    context = {
        'title': article.title,
        'post': article,
        'ext_posts': ext_post,
    }
    return render(request, 'forum/article_detail.html', context)


def add_post(request):
    # Add a article by user, without admin
    if request.method == 'POST':
        pass
    else:
        form = PostAddForm()

    context = {
        'form': form,
        'title': "Add a article",
    }
    return render(request, 'forum/article_add_form.html', context)