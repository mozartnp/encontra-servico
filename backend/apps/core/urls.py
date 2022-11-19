from django.contrib.auth.views import LogoutView
from django.urls import path, reverse_lazy
from django.views.generic.base import RedirectView

from backend.apps.core.views.dashboardViews import DashboardDetailView
from backend.apps.core.views.userViews import LoginCustomView, CreateUserCreateView
from backend.apps.core.views.pessoasViews import CreateClienteCreateView

app_name = 'core'

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='core:login_custom')),

    path('login/', LoginCustomView.as_view(), name='login_custom'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('core:login_custom')), name='logout_custom'),
    path('create_user/', CreateUserCreateView.as_view(), name='create_user'),

    path('criando_cliente/', CreateClienteCreateView.as_view(), name='criando_cliente'),

    path('dashboard/', DashboardDetailView.as_view(), name='dashboard')
]