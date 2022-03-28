from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


# class StartView(LoginRequiredMixin, TemplateView):
class StartView(TemplateView):
    template_name = 'start.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Inicio'
        return context


# Pagina de No permisos
class NotPermsView(TemplateView):
    template_name = 'notperms.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data (**kwargs)
        context['title'] = 'Sin Permisos de Acceso'
        return context
