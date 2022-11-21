from django import forms

from backend.apps.pessoas.models.clienteModels import ClienteModel

class CreateClienteForm(forms.ModelForm):

    class Meta:
        model = ClienteModel
        fields = [
            'nome', 'cpf', 'email', 'telefone1', 'telefone2',
            'logradouro', 'numero', 'complemento', 'bairro', 'cidade',
            'estado', 'pais', 'cep'
        ]
        labels = {
            'nome' : "Seu nome*",
            'cpf' : "Seu CPF*",
            'email' : "Seu e-mail*",
            'telefone1' : "Telefone para contato primario",
            'telefone2' : "Telefone para contato extra",
            'logradouro' : "Logradouro",
            'numero' : "Numero",
            'complemento' : "Complemento",
            'bairro' : "bairro",
            'cidade' : "Cidade",
            'estado' : "Estado",
            'pais': "País",
            'cep' : "CEP"
        }
        widgets= {
            'nome' : forms.TextInput(
                attrs={
                    'placeholder': 'Carlos Ausente',
                }
            ),
            #TODO melhorar a validação
            'cpf' : forms.NumberInput(
                attrs={
                    'placeholder': '12345678900',
                }
            ),
            'email' : forms.EmailInput(
                attrs={
                    'placeholder': 'carlos@ausente.com',
                }
            ),
            'telefone1' : forms.NumberInput(
                attrs={
                    'placeholder': '081987654321',
                }
            ),
            'telefone2' : forms.NumberInput(
                attrs={
                    'placeholder': '081987654321',
                }
            ),
            'logradouro' : forms.TextInput(
                attrs={
                    'placeholder': 'Rua Ali',
                }
            ),
            'numero' : forms.TextInput(
                attrs={
                    'placeholder': 'AN001',
                }
            ),
            'complemento' : forms.TextInput(
                attrs={
                    'placeholder': 'Perto do Posto',
                }
            ),
            'bairro' : forms.TextInput(
                attrs={
                    'placeholder': 'bairro do sonho',
                }
            ),
            'cidade' : forms.TextInput(
                attrs={
                    'placeholder': 'Recife',
                }
            ),
            'estado' : forms.TextInput(
                attrs={
                    'placeholder': 'Pernambuco',
                }
            ),
            'pais' : forms.TextInput(
                attrs={
                    'placeholder': 'Brasil',
                }
            ),
            'cep' : forms.NumberInput(
                attrs={
                    'placeholder': '51000012',
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super(CreateClienteForm, self).__init__(*args, **kwargs)
        self.fields['telefone2'].required = False
        self.fields['logradouro'].required = False
        self.fields['numero'].required = False
        self.fields['complemento'].required = False
        self.fields['bairro'].required = False
        self.fields['cidade'].required = False
        self.fields['estado'].required = False
        self.fields['pais'].required = False
        self.fields['cep'].required = False

