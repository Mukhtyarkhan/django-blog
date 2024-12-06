from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    
    categories=[
        ('eduction', 'eduction'),
        ('entertainment', 'entertainment'),
        ('politics', 'politics'),
        ('sports', 'sports'),
        ('business', 'business')
    ]
    
    title = models.CharField(max_length=255)
    content = models.TextField()
    content_img=models.ImageField(upload_to='images', null=True,blank=True, default=None)
    category=models.CharField(max_length=50,choices=categories)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments" )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

