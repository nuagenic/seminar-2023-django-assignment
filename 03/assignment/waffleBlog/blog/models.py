from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "글"
        verbose_name_plural = "글 목록"


class Comment(models.Model):
    description = models.CharField(max_length=300)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by  = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    is_updated = models.BooleanField(default=False)

    class Meta:
        verbose_name = "댓글"
        verbose_name_plural = "댓글 목록"


class Tag(models.Model):
    content = models.CharField(unique=True, primary_key=True, max_length=100)
    posts = models.ManyToManyField(Post)
    comments = models.ManyToManyField(Comment)
