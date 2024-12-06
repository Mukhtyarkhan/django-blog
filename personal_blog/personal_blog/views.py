from django.shortcuts import render
from blog.models import Post, Comment

def home(request):
    blogs=Post.objects.all().order_by('-created_at')
    # comments=Comment.objects.filter()
    # for blog in blogs:
    #   print(blog.id)
    return render(request,'index.html',{'blogs':blogs})


    