from rest_framework import serializers
from .models import Comment

class CommentSerializers(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'post', 'created_at', 'updated_at', 'content', 'is_owner', 'profile_id', 'profile_image'
        ]

class CommentDetailSerializer(CommentSerializer):
    post = serializers.ReadOnlyField(source='post.id')