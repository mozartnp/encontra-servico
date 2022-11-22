from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from django.urls import reverse_lazy

from backend.apps.custom_user.models import CustomUser
from backend.apps.pessoas.models.clienteModels import ClienteModel
from backend.apps.pessoas.models.empresaModels import EmpresaModel
from backend.apps.pessoas.forms.clienteForms import CreateClienteForm
from backend.apps.pessoas.forms.empresaForms import CreateEmpresaForm

class CreateClienteCreateView(CreateView):
    """
    Classe para criar Cliente
    """
    model = ClienteModel
    template_name = 'user/create_user.html'
    form_class = CreateClienteForm
    success_url = reverse_lazy('core:dashboard')

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            if self.request.user.is_client:
                if self.request.user.user_client:
                    return HttpResponseRedirect(reverse_lazy('core:dashboard'))
                else:
                    return HttpResponseRedirect(reverse_lazy('core:criando_cliente'))
            else:
                if self.request.user.user_company:
                    return HttpResponseRedirect(reverse_lazy('core:dashboard'))
                else: 
                    return HttpResponseRedirect(reverse_lazy('core:criando_empresa'))
        else:
            return HttpResponseRedirect(reverse_lazy('core:login'))

    def form_valid(self, form, **kwargs):

        context = self.get_context_data(**kwargs)
        cliente = form.save(commit=False)
        custom_user = CustomUser.objects.filter(pk=self.request.user.pk).first()
        cliente.user = self.request.user
        cliente.save()
        return super().form_valid(form)

class CreateEmpresaCreateView(CreateView):
    """
    Classe para criar Empres
    """
    model = EmpresaModel
    template_name = 'user/create_user.html'
    form_class = CreateEmpresaForm
    success_url = reverse_lazy('core:dashboard')

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            if self.request.user.is_client:
                if self.request.user.user_client:
                    return HttpResponseRedirect(reverse_lazy('core:dashboard'))
                else:
                    return HttpResponseRedirect(reverse_lazy('core:criando_cliente'))
            else:
                if self.request.user.user_company:
                    return HttpResponseRedirect(reverse_lazy('core:dashboard'))
                else: 
                    return HttpResponseRedirect(reverse_lazy('core:criando_empresa'))
        else:
            return HttpResponseRedirect(reverse_lazy('core:login'))

    def form_valid(self, form, **kwargs):

        context = self.get_context_data(**kwargs)
        cliente = form.save(commit=False)
        custom_user = CustomUser.objects.filter(pk=self.request.user.pk).first()
        cliente.user = self.request.user
        cliente.save()
        return super().form_valid(form)