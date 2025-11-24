from rest_framework import serializers
from .models import Volunteers, Disasters, ReliefMaterials,VolunteerAssignments

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

        # ... existing serializers ...

class VolunteerAssignmentSerializer(serializers.ModelSerializer):
    # These lines fetch the actual NAMES instead of just IDs
    volunteer_name = serializers.CharField(source='volunteer.first_name', read_only=True)
    disaster_name = serializers.CharField(source='disaster.disaster_name', read_only=True)

    class Meta:
        model = VolunteerAssignments
        fields = '__all__'