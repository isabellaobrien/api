from django.urls import path
from comment_reply import views

urlpatterns = [
    path('comment-reply/', views.CommentReplyList.as_view()),
    path('comment-reply/<int:pk>', views.CommentReplyDetail.as_view()),
]