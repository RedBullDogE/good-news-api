from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveAPIView

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
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = DefaultPostListPagination


class CommentViewSet(ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class UpvotePostView(RetrieveAPIView):
    queryset = Post.objects.all()

    def retrieve(self, request, *args, **kwargs):
        post = self.get_object()
        post.upvote()

        serializer = PostSerializer(post)

        return Response(serializer.data)
