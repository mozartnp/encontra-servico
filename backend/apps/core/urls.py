from django.contrib.auth.views import LogoutView
from django.urls import path, reverse_lazy
from django.views.generic.base import RedirectView

from backend.apps.core.views.userViews import LoginCustomView, CreateUserCreateView

app_name = 'core'

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='core:login_custom')),

    path('login/', LoginCustomView.as_view(), name='login_custom'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('core:login_custom')), name='logout_custom'),
    path('create_user/', CreateUserCreateView.as_view(), name='create_user')
]