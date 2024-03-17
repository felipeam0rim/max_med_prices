from django.shortcuts import render
from rest_framework import generics, viewsets, filters
from rest_framework.pagination import PageNumberPagination
from .models import MedProfile
from .serializers import MedProfileSerializer

class MedProfileListCreate(generics.ListCreateAPIView):
    queryset = MedProfile.objects.all()
    # queryset = MedProfile.objects.get_queryset().order_by('profile_id')
    serializer_class = MedProfileSerializer

class MedProfilePagination(PageNumberPagination):
    page_size = 25


class MedProfileViewSet(viewsets.ModelViewSet):
    pagination_class = MedProfilePagination
    serializer_class = MedProfileSerializer
    queryset = MedProfile.objects.all()
    # filter_backends = (filters.SearchFilter)
    # search_fields = ('__all__')