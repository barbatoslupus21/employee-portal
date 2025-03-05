from rest_framework import serializers
from .models import LeaveRouting
from .models import LeaveRequest, LeaveType

class LeaveRoutingSerializer(serializers.ModelSerializer):
    title = serializers.ReadOnlyField(source='approver.name')
    date = serializers.SerializerMethodField()

    class Meta:
        model = LeaveRouting
        fields = ['title', 'date', 'status']

    def get_date(self, obj):
        return obj.approved_at if obj.status == "Approved" else obj.request_at
    