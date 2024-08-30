from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    # Custom field to include the author's username in the serialized data
    # 'source' specifies that this value should come from the 'author.username' field
    # 'read_only=True' means this field is for display purposes only and cannot be modified
    author_name = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        # The model that this serializer is based on
        model = Post
        
        # Fields to include in the serialized representation
        fields = ['id', 'title', 'slug', 'content', 'author_name', 'created_at', 'updated_at']
        
        # Fields that are read-only and should not be included in the deserialization process
        read_only_fields = ['id', 'created_at', 'updated_at', 'author']

class PostDetailsSerializer(serializers.ModelSerializer):
    # Custom field to include the author's username in the serialized data
    # 'source' specifies that this value should come from the 'author.username' field
    # 'read_only=True' means this field is for display purposes only and cannot be modified
    author_name = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        # The model that this serializer is based on
        model = Post
        
        # Fields to include in the serialized representation
        fields = ['id', 'title', 'slug', 'content', 'author_name', 'created_at', 'updated_at']
        
        # Fields that are read-only and should not be included in the deserialization process
        read_only_fields = ['id', 'created_at', 'updated_at', 'author']
