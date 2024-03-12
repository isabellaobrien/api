from rest_framework import generics, permissions
from .models import ReplyLike
from .serializers import ReplyLikeSerializer
from social.permissions import IsOwnerOrReadOnly

class ReplyLikeList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ReplyLikeSerializer
    queryset = ReplyLike.objects.all()

    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)

class ReplyLikeDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ReplyLikeSerializer
    queryset = ReplyLike.objects.all()
