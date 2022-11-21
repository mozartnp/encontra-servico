from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import DetailView, ListView

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_client:
            context['categorias'] = set(EmpresaModel.objects.all().values_list('categoria'))
        return context

    def post(self, request, *args, **kwargs):
        categoria = request.POST.get('categoria')
        return HttpResponseRedirect(reverse('core:lista_empresas', kwargs={"categoria" : categoria}))

class ListCompanyListView(ListView):
    template_name = 'dashboard/lista_empresa.html'

    def get_queryset(self):
        queryset = EmpresaModel.objects.filter(categoria=self.kwargs['categoria'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
