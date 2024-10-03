from rest_framework import serializers
from .models import User

# class BookSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Book
#         fields = '__all__'
#
# class CommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = '__all__'
#
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'