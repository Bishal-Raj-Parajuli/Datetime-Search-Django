from time import strptime
from django.shortcuts import render
import datetime as dt

from django.views.generic import ListView
from .models import Checkup, Doctor

class HomeView(ListView):
    '''Using Class Based View to List all Objects'''

    template_name = 'coreapp/index.html'

    def get_queryset(self):
        '''Overriding default get_queryset function and creating custom Query'''
        
        doctor = self.request.GET.get('doctor','')
        start_date = self.request.GET.get('start_date','')
        end_date = self.request.GET.get('end_date','')
        if (doctor != '') and (not (start_date and end_date)):
            obj = Checkup.objects.filter(doctor=doctor)
        elif start_date and end_date and (not doctor):
            py_start_date = dt.datetime.strptime(start_date, '%Y-%m-%dT%H:%M')
            py_end_date = dt.datetime.strptime(end_date, '%Y-%m-%dT%H:%M')
            obj =Checkup.objects.filter(created_at__gte=py_start_date, created_at__lte=py_end_date)
        elif start_date and (not(end_date and doctor)):
            py_start_date = dt.datetime.strptime(start_date, '%Y-%m-%dT%H:%M')
            obj =Checkup.objects.filter(created_at__gte=py_start_date, created_at__lte=dt.datetime.now())
        elif doctor and start_date and end_date:
            py_start_date = dt.datetime.strptime(start_date, '%Y-%m-%dT%H:%M')
            py_end_date = dt.datetime.strptime(end_date, '%Y-%m-%dT%H:%M')
            obj = Checkup.objects.filter(doctor=doctor,created_at__gte=py_start_date, created_at__lte=py_end_date)
        else:
            obj = Checkup.objects.all()
        return obj

    def get_context_data(self, *args, **kwargs):
        '''Sending Multiple Object in the Template'''

        context = super().get_context_data(**kwargs)
        context['doctor_list'] = Doctor.objects.all()
        return context