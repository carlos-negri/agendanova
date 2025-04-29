from django import forms

from .models import Servico

class ServicoModelForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = '__all__'


        error_messages = {
            'nome': {'required': 'O nome do serviço é um campo obrigatório.', 'unique':'Serviço já cadastrado'},
            'preco': {'required': 'O preço do serviço é um campo obrigatório.'},
            'descricao': {'required': 'A descrição do serviço é um campo obrigatório.'},
        }