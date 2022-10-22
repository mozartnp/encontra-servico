from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.views.generic import CreateView

from backend.apps.custom_user.models import CustomUser
from backend.apps.custom_user.forms import CreateUserForms

class LoginCustomView(LoginView):
    """
    Class View para Login de User
    """
    template_name = 'user/login.html'

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)

class CreateUserCreateView(CreateView):
    """
    Class Create View to create a new User
    """
    model = CustomUser
    template_name = 'user/create_user.html'
    form_class = CreateUserForms