from rest_framework import serializers
from core.models import Post, NASA


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'title',
            'description'
        )

class NASASerializer(serializers.ModelSerializer):
    class Meta:
        model = NASA
        fields = ('link','title','author','summary', 'added_ts','published', 'article_id', 'author_img_url', 'article_img_url')