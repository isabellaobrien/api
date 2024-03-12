from django.urls import path
from reply_likes import views

urlpatterns = [
    path('reply-likes/', views.ReplyLikeList.as_view()),
    path('reply-likes/<int:pk>/', views.ReplyLikeDetail.as_view()),
]