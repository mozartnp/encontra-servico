from django import forms
from django.contrib.auth.forms import UserCreationForm

from backend.apps.custom_user.models import CustomUser

class CreateUserForms(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = (
            'username', 
            'is_client',
            'password1',
            'password2'
        )
        labels = {
            'is_client' : 'Procura serviço?'
        }
        widgets= {
            'username' : forms.TextInput(
                attrs={
                    'placeholder': 'Digite seu username.',
                }
            ),
        }
    
    def __init__(self, *args, **kwargs):
        super(CreateUserForms, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(
            attrs={
                'placeholder': 'Sua senha deve conter A-Z a-z 0-9',
            }
        )
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={
                'placeholder': 'Repita sua senha.',
            }
        )