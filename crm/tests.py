import pytest
from django.urls import reverse
from rest_framework import status
from crm.models import Cliente, Lead, Interacao

@pytest.mark.django_db
def test_create_cliente(client):
    url = reverse('cliente-list')
    data = {
        'nome': 'John Doe',
        'email': 'john.doe@example.com',
        'telefone': '1234567890'
    }
    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Cliente.objects.count() == 1

@pytest.mark.django_db
def test_create_lead(client):
    url = reverse('lead-list')
    data = {
        'cliente_id': 1,
        'descricao': 'Novo lead'
    }
    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Lead.objects.count() == 1

@pytest.mark.django_db
def test_create_interacao(client):
    url = reverse('interacao-list')
    data = {
        'lead_id': 1,
        'descricao': 'Nova interacao'
    }
    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Interacao.objects.count() == 1
