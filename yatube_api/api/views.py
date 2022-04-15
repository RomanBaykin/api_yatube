from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthorOrReadOnly


from posts.models import Post, Comment, Group
from .serializers import PostSerializer, CommentSerializer
from .serializers import GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    """Представление Post"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated, IsAuthorOrReadOnly)

    def perform_create(self, serializer):
        """Берём автора из запроса и автоматом сохраняем как автора поста"""
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """Представление Comment"""
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated, IsAuthorOrReadOnly)

    def get_queryset(self):
        """Переопределение queryset для получения коммента к посту"""
        post_id = self.kwargs.get('post_id')
        new_queryset = Comment.objects.filter(post=post_id)
        return new_queryset

    def perform_create(self, serializer):
        """Берём автора из запроса и автоматом сохраняем как автора коммента"""
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Представление Group"""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
