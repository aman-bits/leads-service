from rest_framework import serializers
from .models import Stage, Lead, LeadActivity


class StageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stage
        fields = '__all__'


class LeadActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadActivity
        fields = '__all__'


class LeadSerializer(serializers.ModelSerializer):
    stage = StageSerializer(read_only=True)
    stage_id = serializers.PrimaryKeyRelatedField(
        queryset=Stage.objects.all(), write_only=True, source='stage'
    )
    activities = LeadActivitySerializer(many=True, read_only=True)

    class Meta:
        model = Lead
        fields = '__all__'
