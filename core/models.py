from django.db import models

class Disasters(models.Model):
    disaster_id = models.AutoField(primary_key=True)
    disaster_name = models.CharField(max_length=255)
    disaster_type = models.CharField(max_length=50)
    start_date = models.DateField(blank=True, null=True)
    severity_level = models.IntegerField(blank=True, null=True)

    latitude = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'disasters'

class Volunteers(models.Model):
    volunteer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(unique=True, max_length=255)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    skills = models.TextField(blank=True, null=True)
    availability_status = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'volunteers'

class ReliefMaterials(models.Model):
    material_id = models.AutoField(primary_key=True)
    material_name = models.CharField(max_length=100)
    material_type = models.CharField(max_length=50, blank=True, null=True)
    unit_of_measurement = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'relief_materials'

class Warehouses(models.Model):
    warehouse_id = models.AutoField(primary_key=True)
    warehouse_name = models.CharField(max_length=100)
    location = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warehouses'

class AidAgencies(models.Model):
    agency_id = models.AutoField(primary_key=True)
    agency_name = models.CharField(max_length=100)
    agency_type = models.CharField(max_length=50, blank=True, null=True)
    contact_person = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aid_agencies'

class AffectedAreas(models.Model):
    area_id = models.AutoField(primary_key=True)
    disaster = models.ForeignKey(Disasters, models.DO_NOTHING, blank=True, null=True)
    area_name = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
    population_affected = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'affected_areas'

class Inventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    material = models.ForeignKey('ReliefMaterials', models.DO_NOTHING, blank=True, null=True)
    warehouse = models.ForeignKey('Warehouses', models.DO_NOTHING, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventory'

class VolunteerAssignments(models.Model):
    assignment_id = models.AutoField(primary_key=True)
    volunteer = models.ForeignKey(Volunteers, models.DO_NOTHING, blank=True, null=True)
    area = models.ForeignKey(AffectedAreas, models.DO_NOTHING, blank=True, null=True)
    role = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'volunteer_assignments'

class MaterialDistribution(models.Model):
    distribution_id = models.AutoField(primary_key=True)
    material = models.ForeignKey('ReliefMaterials', models.DO_NOTHING, blank=True, null=True)
    area = models.ForeignKey(AffectedAreas, models.DO_NOTHING, blank=True, null=True)
    agency = models.ForeignKey(AidAgencies, models.DO_NOTHING, blank=True, null=True)
    quantity_distributed = models.IntegerField(blank=True, null=True)
    distribution_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'material_distribution'