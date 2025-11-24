from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Volunteers, Disasters, ReliefMaterials,VolunteerAssignments
from .serializers import VolunteerSerializer, DisasterSerializer, ReliefMaterialSerializer,VolunteerAssignmentSerializer

# ==========================================
# 1. VOLUNTEERS
# ==========================================

@api_view(['GET', 'POST'])
def volunteer_list(request):
    # GET: List all volunteers
    if request.method == 'GET':
        volunteers = Volunteers.objects.all()
        serializer = VolunteerSerializer(volunteers, many=True)
        return Response(serializer.data)

    # POST: Add a new volunteer
    elif request.method == 'POST':
        serializer = VolunteerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def volunteer_detail(request, pk):
    # DELETE: Remove a specific volunteer by ID
    try:
        volunteer = Volunteers.objects.get(pk=pk)
        volunteer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Volunteers.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


# ==========================================
# 2. DISASTERS
# ==========================================

@api_view(['GET', 'POST'])
def disaster_list(request):
    if request.method == 'GET':
        disasters = Disasters.objects.all()
        serializer = DisasterSerializer(disasters, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DisasterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def disaster_detail(request, pk):
    try:
        disaster = Disasters.objects.get(pk=pk)
        disaster.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Disasters.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


# ==========================================
# 3. MATERIALS
# ==========================================

@api_view(['GET', 'POST'])
def material_list(request):
    if request.method == 'GET':
        materials = ReliefMaterials.objects.all()
        serializer = ReliefMaterialSerializer(materials, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ReliefMaterialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def material_detail(request, pk):
    try:
        material = ReliefMaterials.objects.get(pk=pk)
        material.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ReliefMaterials.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    from .models import VolunteerAssignments # <--- Add this to imports at the top
from .serializers import VolunteerAssignmentSerializer # <--- Add this too

@api_view(['GET', 'POST'])
def assignment_list(request):
    # GET: Show all deployments
    if request.method == 'GET':
        assignments = VolunteerAssignments.objects.select_related('volunteer', 'disaster').all()
        serializer = VolunteerAssignmentSerializer(assignments, many=True)
        return Response(serializer.data)

    # POST: Deploy a volunteer
    elif request.method == 'POST':
        serializer = VolunteerAssignmentSerializer(data=request.data)
        if serializer.is_valid():
            assignment = serializer.save()
            
            # --- AUTOMATION: Update Volunteer Status to 'Busy' ---
            volunteer = assignment.volunteer
            volunteer.availability_status = 'Busy'
            volunteer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def assignment_detail(request, pk):
    try:
        assignment = VolunteerAssignments.objects.get(pk=pk)
        
        # --- AUTOMATION: Free the volunteer (Set back to 'Available') ---
        volunteer = assignment.volunteer
        volunteer.availability_status = 'Available'
        volunteer.save()
        
        assignment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except VolunteerAssignments.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)