from django.contrib.auth.views import *
from django.shortcuts import redirect
from django.urls import reverse_lazy

from bpmprometro import settings


# Login para iniciar sesion
class LoginFormView(LoginView):
    template_name = 'login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(settings.LOGIN_REDIRECT_URL)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Iniciar sesión'
        return context


# Recuperar contraseña
class FormResetPasswordView(PasswordResetView):
    template_name = 'reset_password_form.html'
    email_template_name = 'reset_password_email.html'
    success_url = reverse_lazy('password_reset_done')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Recuperar contraseña'
        return context


# Envío de contraseña para recuperación
class ResetPasswordDoneView(PasswordResetDoneView):
    template_name = 'reset_password_done.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Contraseña enviada'
        return context


# Cambiar contraseña
class ResetConfirmPasswordView(PasswordResetConfirmView):
    template_name = 'reset_password_confirm.html'
    success_url = reverse_lazy('password_reset_complete')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Cambiar contraseña'
        return context


# Confirmación de contraseña actualizada
class ResetCompletePasswordView(PasswordResetCompleteView):
    template_name = 'reset_password_complete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Contraseña actualizada'
        return context
