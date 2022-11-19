from django.http import Http404
from django.views.generic import DetailView

from backend.apps.custom_user.models import CustomUser
from backend.apps.pessoas.models.clienteModels import ClienteModel
from backend.apps.pessoas.models.empresaModels import EmpresaModel

class DashboardDetailView(DetailView):
    template_name = 'dashboard/dashboard.html'
    model = CustomUser

    def get_object(self, queryset=None):
        if self.request.user.is_client:
            queryset = ClienteModel.objects.filter(user=self.request.user)
        elif not self.request.user.is_client:
            queryset = EmpresaModel.objects.filter(user=self.request.user)

        if queryset:
            obj = queryset.get()
            return obj
        
        raise Http404(f"No {queryset.model._meta.verbose_name} found matching the query")