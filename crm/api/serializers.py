from rest_framework import serializers
from .models import Cliente, Lead, Interacao

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'

class InteracaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interacao
        fields = '__all__'
