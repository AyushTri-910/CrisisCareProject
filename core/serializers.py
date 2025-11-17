from rest_framework import serializers
from .models import Volunteers, Disasters, ReliefMaterials

# This converts the Volunteers model to JSON
class VolunteerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volunteers
        fields = '__all__' # This means "include every column"

class DisasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disasters
        fields = '__all__'

class ReliefMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReliefMaterials
        fields = '__all__'