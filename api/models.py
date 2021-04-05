from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=32)
    link = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    upvotes_amount = models.IntegerField(default=0, editable=False)

    def upvote(self):
        """
        Extra model method for adding upvotes for specific post.
        """
        self.upvotes_amount += 1
        self.save()

    def less_comments(self):
        """
        Extra model method to return only recent part of the comments for specific post.
        """
        return Comment.objects.filter(post=self).order_by("-created_at")[:5]

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
