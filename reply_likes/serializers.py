from rest_framework import serializers
from .models import ReplyLike
from django.db import IntegrityError

class ReplyLikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = ReplyLike
        fields = [
            'id', 'owner', 'reply', 'created_at'
        ]
    
    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })