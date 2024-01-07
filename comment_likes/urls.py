from django.urls import path
from comment_likes import views

urlpatterns = [
    path('comment-likes/', views.CommentLikeList.as_view()),
    path('comment-likes/<int:pk>', views.CommentLikeDetail.as_view()),
]