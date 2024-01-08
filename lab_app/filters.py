# from django_filters import FilterSet
import django_filters

from .models import Patient, File

class PatientFilter(django_filters.FilterSet): 
    class Meta:
        model = Patient
        fields = {
            "full_name": ['icontains'],
        }


class FileFilter(django_filters.FilterSet):
    # full_name = django_filters.CharFilter(field_name="patient__full_name", lookup_expr='iexact')
    class Meta:
        model = File
        fields = {
            "patient__full_name": ["icontains"],
        }
        
    
        
        
