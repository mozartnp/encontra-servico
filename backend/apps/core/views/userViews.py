from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect

from backend.apps.custom_user.models import CustomUser

class LoginCustomView(LoginView):
    """
    Class View para Login de User
    """
    template_name = 'user/login.html'

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)