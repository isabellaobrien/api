from django.db import models
from django.contrib.auth.models import User
from comment_reply.models import CommentReply

class ReplyLike(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    reply = models.ForeignKey(CommentReply, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'reply']
    
    def __str__(self):
        return f'{self.owner} {self.reply}'
