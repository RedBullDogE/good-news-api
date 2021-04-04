from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class DefaultPostListPagination(PageNumberPagination):
    """
    Class for default pagination configuration for PostViewSet
    """

    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 50


class PostViewSet(ModelViewSet):
    """
    API endpoint that allows manipulate post data.
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = DefaultPostListPagination

    @action(detail=True, methods=["get"])
    def upvote(self, request, pk=None):
        post = self.get_object()
        post.upvote()

        serializer = PostSerializer(post)

        return Response(serializer.data)


class CommentViewSet(ModelViewSet):
    """
    API endpoint that allows manipulate comment data.
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(post=self.kwargs["post_pk"])
