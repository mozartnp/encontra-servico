from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from django.urls import reverse_lazy

from backend.apps.custom_user.models import CustomUser
from backend.apps.custom_user.forms import CreateUserForms

class LoginCustomView(LoginView):
    """
    Class View para Login de User
    """
    template_name = 'user/login.html'

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('core:create_user'))
        return super().dispatch(request, *args, **kwargs)

class CreateUserCreateView(CreateView):
    """
    Class Create View to create a new User
    """
    model = CustomUser
    template_name = 'user/create_user.html'
    form_class = CreateUserForms

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            try:
                self.request.user.user_company
                return HttpResponseRedirect(reverse_lazy('core:dashboard'))
            except:
                pass
            try:
                self.request.user.user_client
                return HttpResponseRedirect(reverse_lazy('core:dashboard'))
            except:
                pass
            if self.request.user.is_client:
                return HttpResponseRedirect(reverse_lazy('core:criando_cliente'))
            elif not self.request.user.is_client:
                return HttpResponseRedirect(reverse_lazy('core:criando_empresa'))

        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        '''
        Define o redirect dependendo do tipo de usuário.
        '''
        user = authenticate(self.request, username=self.request.POST['username'], password=self.request.POST['password1'])
        login(self.request, user)
        if self.object.is_client:
            return reverse_lazy('core:criando_cliente')
        elif not self.object.is_client:
            return reverse_lazy('core:criando_empresa')

        return reverse_lazy('core:login_custom')