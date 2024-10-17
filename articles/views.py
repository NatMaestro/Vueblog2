from django.shortcuts import render
from rest_framework.response import Response  # This is correct
from rest_framework import viewsets, status
from .serializers import ArticleSerializer
from .models import Article
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthor
from rest_framework.exceptions import PermissionDenied, NotAuthenticated

# Create your views here.

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by('-created_at')
    lookup_field  = 'slug'
    serializer_class = ArticleSerializer

    permission_classes = [IsAuthenticated, IsAuthor]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def handle_exception(self, exc):
        # Overriding to return JSON response for any exceptions
        if isinstance(exc, (PermissionDenied, NotAuthenticated)):
            return Response({'error': str(exc)}, status=status.HTTP_403_FORBIDDEN)
        return super().handle_exception(exc)

    
    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except Article.DoesNotExist:
            return Response({"detail": "Not Found"}, status=status.HTTP_404_NOT_FOUND)
    
        # Ensure DELETE is allowed
    def destroy(self, request, *args, **kwargs):
        article = self.get_object()
        self.perform_destroy(article)
        return Response(status=status.HTTP_204_NO_CONTENT)


def index(request):
    # This view will serve the Vue app
    return render(request, 'index.html')