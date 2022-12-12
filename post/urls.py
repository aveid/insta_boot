from django.urls import path

from . import views

urlpatterns = [
    path("posts/", views.get_all_posts, name="posts"),
    path("posts/<int:pk>/", views.detail_post, name="detail_post"),
]