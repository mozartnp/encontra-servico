from django.views.generic import CreateView
from django.urls import reverse_lazy

from backend.apps.custom_user.models import CustomUser
from backend.apps.pessoas.models.clienteModels import ClienteModel
from backend.apps.pessoas.forms.clienteForms import CreateClienteForm

class CreateClienteCreateView(CreateView):
    """
    Class Create View to create a new User
    """
    model = ClienteModel
    template_name = 'user/create_user.html'
    form_class = CreateClienteForm
    success_url = reverse_lazy('core:dashboard')

    def form_valid(self, form, **kwargs):

        context = self.get_context_data(**kwargs)
        cliente = form.save(commit=False)
        custom_user = CustomUser.objects.filter(pk=self.request.user.pk).first()
        print(custom_user)
        cliente.user = self.request.user
        cliente.save()
        return super().form_valid(form)