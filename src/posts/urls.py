from django.contrib.auth.decorators import login_required
from django.urls import path

#from blog.urls import urlpatterns
from posts.views import BlogHome, BlogPostCreate, BlogPostUpdate, BlogPostDetail, BlogPostDelete

app_name ="posts"

urlpatterns = [
    path('', BlogHome.as_view(),name = 'home'),
    path('create', BlogPostCreate.as_view(),name = 'create'), # Etre connecter avant d'utiliser
    path('<str:slug>/', BlogPostDetail.as_view(),name = 'post'),
    path('edit/<str:slug>/', BlogPostUpdate.as_view(),name = 'edit'),
    path('delete/<str:slug>/', BlogPostDelete.as_view(),name = 'delete'),
]