from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from levelupapi.models import Post, RareUser, Category, Tag

class Posts(ViewSet):

    def create(self, request):

        rareuser = RareUser.objects.get(user=request.auth.user)

        post = Post()
        post.user_id = rareuser
        post.title = request.date["postTitle"]
        post.publication_date = ["postDate"]
        post.image_url = ["postImage"]
        post.content = ["postContent"]
        post.apporoved = ["approved"]

        category = Category.objects.get(pk=request.data["categoryId"])
        post.category = category

        try:
            post.save()
            serializer = PostSerializer(post, context={'request': request})
            return Response(serializer.data)

        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):

        try:
            post = Post.objects.get(pk=pk)
            serializer = PostSerializer(post, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):

        rareuser = RareUser.objects.get(user=request.auth.user)

        post = Post()
        post.user_id = rareuser
        post.title = request.date["postTitle"]
        post.publication_date = ["postDate"]
        post.image_url = ["postImage"]
        post.content = ["postContent"]
        post.apporoved = ["approved"]

        category = Category.objects.get(pk=request.data["categoryId"])
        post.category = category
        post.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk=None):

        try:
            post = Post.objects.get(pk=pk)
            post.delete()
    
            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Post.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):

        posts = Post.objects.all()

        category = self.request.query_params.get('category', None)
        if category is not None:
            category = posts.filter(categoryId=category)

        serializer = PostSerializer(
            posts, many=True, context={'request': request})
        return Response(serializer.data)
    
