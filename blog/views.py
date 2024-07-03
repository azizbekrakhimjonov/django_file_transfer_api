from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from .models import File
from .serializers import FileSerializer

class FileUploadView(generics.CreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    parser_classes = [MultiPartParser, FormParser]

class FileListView(generics.ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

