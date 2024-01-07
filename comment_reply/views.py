from .models import CommentReply
from .serializers import CommentReplySerializer, CommentReplyDetailSerializer
from rest_framework import generics, permissions 
from social.permissions import IsOwnerOrReadOnly

class CommentReplyList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CommentReplySerializer
    queryset = CommentReply.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CommentReplyDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentReplyDetailSerializer
    queryset = CommentReply.objects.all()