from django.contrib import admin
from .models import Patient, Doctor, Checkup

'''Registering Model in Admin Page'''
admin.site.register([Patient, Doctor, Checkup])
