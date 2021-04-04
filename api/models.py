from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=32)
    link = models.CharField(max_length=128, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    upvotes_count = models.IntegerField(default=0, editable=False)

    def upvote(self):
        self.upvotes_count += 1
        self.save()

    def __str__(self):
        return f"{self.title} | {self.author}"

    class Meta:
        ordering = ["created_at"]


class Comment(models.Model):
    author = models.CharField(max_length=32)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return f"by author: {self.author} for post:"

    class Meta:
        ordering = ["created_at"]
