from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView

from .models import Document, Section
from .serializers import DocumentSerializer, SectionSerializer


class DocumentListAPIView(GenericAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    def get(self, request):
        data = self.get_serializer(self.get_queryset(), many=True).data
        return Response(data={'notifications': data}, status=status.HTTP_200_OK)


class DocumentInstanceAPIView(GenericAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

    def get(self, request, doc_name):
        sections = self.get_queryset().filter(document__title_en=doc_name)
        data = self.get_serializer(sections, many=True).data
        return Response(data={
            'document_title': doc_name,
            'sections': data
        }, status=status.HTTP_200_OK)


class SectionAPIView(GenericAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

    def get(self, request, section_uuid):
        section = get_object_or_404(self.get_queryset(), uuid=section_uuid)
        data = self.get_serializer(section).data
        return Response(data={
            'document_title': section.document.title_en,
            'section': data
        }, status=status.HTTP_200_OK)
