from rest_framework import serializers
from apps.blog.models import *



class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name', 'color']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['writer_name', 'text', 'date']

    def create(self, validated_data):
        validated_data['writer_name'] = self.request.user.username
        return Comment.objects.create(**validated_data)


class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = ['comments', 'tags', 'date', 'image',
                  'post_title', 'text','post_description']


class PostDescriptionSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = ['comments', 'tags', 'date', 'image', 'post_title',
                  'post_description']

