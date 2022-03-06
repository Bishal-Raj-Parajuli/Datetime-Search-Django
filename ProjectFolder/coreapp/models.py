from django.db import models

class TimeStamp(models.Model):
    '''Creation of a Abstract Time Stamp Model'''

    created_at = models.DateTimeField(auto_now_add=True, editable=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Patient(TimeStamp):
    '''Creation of a Patient Model'''

    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    contact_no = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return str(self.name)

class Doctor(TimeStamp):
    '''Creation of Doctor Model'''

    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    contact_no = models.CharField(max_length=15, unique=True)   
    department = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)

class Checkup(TimeStamp):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='checkup')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='checkup')

    def __str__(self):
        return str(self.pk)