from rest_framework import viewsets
from .models import Cliente, Lead, Interacao
from .serializers import ClienteSerializer, LeadSerializer, InteracaoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

class InteracaoViewSet(viewsets.ModelViewSet):
    queryset = Interacao.objects.all()
    serializer_class = InteracaoSerializer
