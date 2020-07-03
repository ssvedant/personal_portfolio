
from django.urls import path
from . import views  # dot since we are inside the blog directory itself
app_name = 'blog'
urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail'),

]
