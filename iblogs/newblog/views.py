

from django.shortcuts import render, HttpResponse
from newblog.models import Post, Category
# Create your views here.
def home(request):
    post=Post.objects.all()[:11]
    # print(post)
    cats= Category.objects.all()
    data={
        'post':post,
        'cats': cats
    }
    return render(request, 'home.html', data)

def posts(request, url):
    post=Post.objects.get(url=url)
    cats= Category.objects.all()
    return render(request, "posts.html", {'post':post, 'cats':cats})

def category(request, url):

    category= Category.objects.get(url= url)
    posts= Post.objects.filter(cat= category)
    return render(request, "category.html", {'category':category, 'posts':posts})