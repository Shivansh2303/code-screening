from rest_framework import viewsets
from .models import Post
from .serializers import PostListSerializer

class PostListViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PostListSerializer
    queryset = Post.objects.all().order_by('-timestamp') 
