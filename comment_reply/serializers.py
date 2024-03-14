from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import CommentReply
from reply_likes.models import ReplyLike

class CommentReplySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    reply_like_id = serializers.SerializerMethodField()
    reply_likes_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_reply_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            reply_like = ReplyLike.objects.filter(
                 owner=user, reply=obj
            ).first()
            return reply_like.id if reply_like else None
        return None
    

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    class Meta:
        model = CommentReply
        fields = [
            'id', 'owner', 'comment', 'created_at', 'updated_at', 'content', 
            'is_owner', 'profile_id', 'profile_image', 'reply_like_id', 'reply_likes_count',
        ]

class CommentReplyDetailSerializer(CommentReplySerializer):
    comment = serializers.ReadOnlyField(source='comment.id')