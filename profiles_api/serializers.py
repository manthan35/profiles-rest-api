from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """serializes a name filed for testing out APIViews"""
    name = serializers.CharField(max_length=10)