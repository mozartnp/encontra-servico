from django import forms

from backend.apps.pessoas.models.empresaModels import EmpresaModel

class CreateEmpresaForm(forms.ModelForm):

    class Meta:
        model = EmpresaModel
        fields = [
            'nome_fantasia', 'razao_social', 'cnpj', 'ie', 'email',
            'telefone1', 'telefone2', 'logradouro', 'numero', 'complemento',
            'bairo', 'cidade', 'estado', 'pais', 'complemento', 'cep'
        ]
        labels = {
            'nome_fantasia' : "Nome Fantasia da Empresa*",
            'razao_social' : "Razão Social da Empresa",
            'cnpj' : "CNPJ da Empresa*",
            'ie' : "Inscrição Estaudal da Empresa",
            'email' : "E-mail institucional*",
            'telefone1' : "Telefone para contato primario",
            'telefone2' : "Telefone para contato extra",
            'logradouro' : "Logradouro",
            'numero' : "Numero",
            'complemento' : "Complemento",
            'bairo' : "Bairo",
            'cidade' : "Cidade",
            'estado' : "Estado",
            'pais': "País",
            'cep' : "CEP"
        }
        widgets= {
            'nome_fantasia' : forms.TextInput(
                attrs={
                    'placeholder': 'Mario Encanadores',
                }
            ),
            'razao_social' : forms.TextInput(
                attrs={
                    'placeholder': 'Mario CORP',
                }
            ),
            #TODO melhorar a validação
            'cnpj' : forms.NumberInput(
                attrs={
                    'placeholder': '12345678900123',
                }
            ),
            'ie' : forms.NumberInput(
                attrs={
                    'placeholder': '123456780',
                }
            ),
            'email' : forms.EmailInput(
                attrs={
                    'placeholder': 'mario@encanadores.com',
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
            'bairo' : forms.TextInput(
                attrs={
                    'placeholder': 'Bairo do sonho',
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
        super(CreateEmpresaForm, self).__init__(*args, **kwargs)
        self.fields['ie'].required = False
        self.fields['telefone2'].required = False
        self.fields['logradouro'].required = False
        self.fields['numero'].required = False
        self.fields['complemento'].required = False
        self.fields['bairo'].required = False
        self.fields['cidade'].required = False
        self.fields['estado'].required = False
        self.fields['pais'].required = False
        self.fields['cep'].required = False

