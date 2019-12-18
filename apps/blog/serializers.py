from rest_framework import serializers
from apps.blog.models import *



class TagSerializer(serializers.ModelSerializer):
    name_value = serializers.CharField()
    class Meta:
        model = Tag
        fields = ['name_value', 'color']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['user', 'text', 'date']

    # def create(self, validated_data):
    #     validated_data['writer_name'] = self.request.user.username
    #     return Comment.objects.create(**validated_data)


class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    post_title_value = serializers.CharField()
    post_description_value = serializers.CharField()
    text_value = serializers.CharField()
    count_comments = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['count_comments','id','tags', 'date', 'image',
                  'post_title_value', 'text_value','post_description_value']

    def get_count_comments(self, obj):
        return obj.comments.count()


class PostDescriptionSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    post_title_value = serializers.CharField()
    post_description_value = serializers.CharField()

    class Meta:
        model = Post
        fields = ['id','tags', 'date', 'image', 'post_title_value',
                  'post_description_value']

