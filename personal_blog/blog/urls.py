from django.urls import path
from . import views


urlpatterns=[
    path('profile', views.profile, name='profile'),
    path('search/', views.search, name='search'),
    path('blogs/',views.add_blogs, name='blogs'),
    path('update-blog/<int:id>/', views.update_blog, name='update_blog'),
    path('delete-blog/<int:id>/', views.delete_blog, name='delete_blog'),
    path('comment/', views.post_comment, name='post_comment'),
    # path('category/eduction/', views.eduction, name='eduction'),
    # path('category/entertainment/', views.entertainment, name='entertainment'),
    # path('category/politics/', views.politics, name='politics'),
    # path('category/sports/', views.sports, name='sports'),
    # path('category/business/', views.business, name='business'),
    # path('categores', views.categores, name='categores'),
    path('categories/<str:category_name>/', views.categories, name='categories'),

    
]