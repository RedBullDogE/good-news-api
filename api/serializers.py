from .models import Post, Comment
from rest_framework import serializers


class CommentUnderPostSerializer(serializers.ModelSerializer):
    """
    Serializer for Comment model, provides short and informative fields.
    """

    post = serializers.SlugRelatedField("title", read_only=True)

    class Meta:
        model = Comment
        fields = ["post", "author", "content"]


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for Comment model, which covers all model fields and
    should be used for details or creating comments.
    """

    class Meta:
        model = Comment
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for Post model, which covers all fields.
    """

    comments = CommentUnderPostSerializer(
        many=True,
        read_only=True,
        source="less_comments"
    )

    class Meta:
        model = Post
        fields = "__all__"
