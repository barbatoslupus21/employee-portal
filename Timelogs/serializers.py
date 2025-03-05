from rest_framework import serializers
from .models import EmployeeTimelogs

class EmployeeTimelogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeTimelogs
        fields = ['log_date', 'time_in', 'time_out']
