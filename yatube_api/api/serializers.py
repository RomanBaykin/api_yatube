from posts.models import Post, Comment, Group
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор данных из модели Post"""
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор данных из модели Comment"""
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор данных из модели Group"""
    class Meta:
        model = Group
        fields = '__all__'
