from rest_framework import serializers
from .models import MedProfile

class MedProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedProfile
        fields = '__all__'