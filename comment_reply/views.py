from .models import CommentReply
from .serializers import CommentReplySerializer, CommentReplyDetailSerializer
from rest_framework import generics, permissions, filters
from social.permissions import IsOwnerOrReadOnly
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend

class CommentReplyList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CommentReplySerializer
    queryset = CommentReply.objects.annotate(
        reply_likes_count=Count('replylike', distinct=True),
    ).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend
    ]
    filterset_fields = [
        'comment',
    ]

class CommentReplyDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentReplyDetailSerializer
    queryset = CommentReply.objects.all()

    