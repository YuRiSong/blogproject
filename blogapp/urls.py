from django.contrib import admin
from django.urls import path, include
from . import views
import blogapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('<int:blog_id>/', views.detail, name="detail"),
    path('new/', views.new, name="new"),
    path('create', blogapp.views.create, name="create"),
    path('<int:blog_id>/delete/', views.delete, name='delete'),
    path('<int:blog_id>/edit/', blogapp.views.edit, name='edit'),
    path('<int:blog_id>/update/', blogapp.views.update, name='update'),
    path('<int:blog_id>/comments/', blogapp.views.add_comment, name='add_comment'),
]
