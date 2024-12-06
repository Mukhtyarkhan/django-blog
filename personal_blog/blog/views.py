from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm
import json
from django.http import JsonResponse
from django.utils.timezone import now

def profile(request):
    blog = Post.objects.filter(author=request.user)  
    return render(request, 'profile.html', {'blogs': blog})

def add_blogs(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)  
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  
            post.save()
            return redirect('profile')
    else:
        form = PostForm()
    return render(request, "add_blogs.html", {'form': form})



def update_blog(request,id):
    blog=Post.objects.get(id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = PostForm(instance=blog)
    return render(request, 'update.html', {'form': form}) 


def delete_blog(request, id):
    blog=Post.objects.get(id=id)
    if request.method=='POST':
        blog.delete()
        return redirect('profile')
    return render(request, 'profile.html', {'blog':blog})



def search(request):
    blogs = []
    if request.method == 'GET':
        search_term = request.GET.get('q')  
        if search_term:
            blogs = Post.objects.filter(title__icontains=search_term)

    return render(request, 'index.html', {'blogs': blogs})




def post_comment(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        post_id = data.get('post_id')
        content = data.get('content')
        
        comment = Comment.objects.create(
            post_id=post_id,
            content=content,
            author=request.user,
            date_posted=now(),
        )
        
        
        if 'comment_count' in request.session:
            request.session['comment_count'] += 1
        else:
            request.session['comment_count'] = 1

        comment_count=request.session.get('comment_count', 0) 
        
        
        return JsonResponse({
            'comment': comment.content,
            'author': comment.author.username,
            'created_on': comment.date_posted.strftime('%B %d, %Y, %I:%M %p'),
            'total_comments': comment_count,  
        })        
        
        

def categories(request, category_name):
    blogs = Post.objects.filter(category=category_name)
    return render(request, 'index.html', {'blogs': blogs})


# def eduction(request):
#     blogs = Post.objects.filter(category='eduction')
#     return render(request, 'index.html', {'blogs': blogs})


# def entertainment(request):
#     blogs = Post.objects.filter(category='entertainment')
#     return render(request, 'index.html', {'blogs': blogs})


# def politics(request):
#     blogs = Post.objects.filter(category='politics')
#     return render(request, 'index.html', {'blogs': blogs})


# def sports(request):
#     blogs = Post.objects.filter(category='sports')
#     return render(request, 'index.html', {'blogs': blogs})


# def business(request):
#     blogs = Post.objects.filter(category='business')
#     return render(request, 'index.html', {'blogs': blogs})


