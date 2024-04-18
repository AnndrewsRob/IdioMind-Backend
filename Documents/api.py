from rest_framework import viewsets , permissions
from .models import PDFDocument
from .serializers import PDFDocumentCreateSerializer,PDFDocumentListSerializer,TranslatePromptSerializer
from rest_framework.response import Response
from rest_framework import status
from .utils import translate_word
from rest_framework.views import APIView

class PDFDocumentListViewSet(viewsets.ModelViewSet):
    queryset = PDFDocument.objects.all()
    serializer_class = PDFDocumentListSerializer

    def get_permissions(self):
        if self.action == 'create':
            # Solo permitir la creación de PDFs a usuarios autenticados
            return [permissions.IsAuthenticated()]
        else:
            # Permitir todas las demás operaciones a cualquier usuario
            return [permissions.AllowAny()]
    

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return PDFDocument.objects.filter(user=user)
        else:
            return PDFDocument.objects.none()
        
class PDFDocumentCreateViewSet(viewsets.ModelViewSet):
    queryset = PDFDocument.objects.all()
    serializer_class = PDFDocumentCreateSerializer

    def get_permissions(self):
        if self.action == 'create':
            # Solo permitir la creación de PDFs a usuarios autenticados
            return [permissions.IsAuthenticated()]
        else:
            # Permitir todas las demás operaciones a cualquier usuario
            return [permissions.AllowAny()]
        
        
    def perform_create(self, serializer):
        # Asignar automáticamente el usuario autenticado al crear el PDF
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return PDFDocument.objects.filter(user=user)
        else:
            return PDFDocument.objects.none()
        


class TranslateWordViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = TranslatePromptSerializer(data=request.data)
        if serializer.is_valid():
            word = serializer.validated_data['word']
            language = serializer.validated_data['language']
            sentence = serializer.validated_data.get('sentence')
            
            # Llama a tu función de traducción
            translation_data = translate_word(word, language, sentence)
            
            # Retorna la respuesta en formato JSON
            return Response(translation_data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)