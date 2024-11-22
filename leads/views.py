from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings

from .models import Stage, Lead, LeadActivity
from .serializers import StageSerializer, LeadSerializer, LeadActivitySerializer


class StageViewSet(viewsets.ModelViewSet):
    queryset = Stage.objects.all()
    serializer_class = StageSerializer


class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

    @action(detail=True, methods=['post'])
    def send_email(self, request, pk=None):
        lead = self.get_object()
        send_mail(
            subject=f"Follow-up with {lead.name}",
            message=f"Lead Details:\n\nName: {lead.name}\nEmail: {lead.email}\nPhone: {lead.phone}\nMessage: {lead.message}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[lead.email],
        )
        return Response({"message": "Email sent successfully!"})


class LeadActivityViewSet(viewsets.ModelViewSet):
    queryset = LeadActivity.objects.all()
    serializer_class = LeadActivitySerializer
