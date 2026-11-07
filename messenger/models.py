from django.db import models

# Create your models here.

from django.contrib.auth.models import User


class Post(models.Model):
    content = models.TextField(blank=True)
    media = models.FileField(upload_to="posts_media/", blank=True)
    link = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.content[:50] or f"Публикация {self.pk}"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    media = models.FileField(
        upload_to="comments_media/", blank=True)

    def __str__(self):
        return self.content[:50]


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked_posts')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('post', 'user')  # Один лайк на пост від користувача