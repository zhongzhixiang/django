from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
import random
# Create your views here.
def index(request):
    return HttpResponse("hello world")

def add_data(request):
    int_num = random.randrange(10)
    title = "post" + str(int_num)
    body = "body of post" + str(int_num)
    Post.objects.create(title=title, body=body)


def article(request):
    post_list = Post.objects.all()
    context = {"post_list": post_list}
    return render(request, 'blog/article.html', context=context)

def detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'blog/detail.html', context={"post": post})

def update_post(request):
    post_id = request.POST.get("post_id")
    post = Post.objects.get(id=post_id)
    post.body="diwupianwenzhang"
    post.save()
    return HttpResponse("update success")