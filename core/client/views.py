from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, UpdateView, ListView, DetailView

from core.client.forms import ClientForm
from core.client.models import Client
from core.mixins import ValidatePermissionRequiredMixin


# Creación de Clientes
class ClientCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = Client
    template_name = 'create_client.html'
    form_class = ClientForm
    permission_required = 'user.add_user'
    success_url = reverse_lazy('client:client_list')
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                if form.is_valid():
                    form.save()
                    messages.info(request, 'Cliente creado satisfactoriamente!!')
                else:
                    messages.error(request, form.errors)
            else:
                data['error'] = 'No ingresado datos en los campos'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entity'] = 'Creación de Clientes'
        context['title'] = 'Creación de Clientes'
        context['action'] = 'add'
        context['list_url'] = self.success_url
        return context


# Edicion de Clientes
class ClientUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'create_client.html'
    success_url = reverse_lazy('client:client_list')
    permission_required = 'user.change_user'
    url_redirect = success_url

    # def __init__(self, **kwargs):
    #     super().__init__(kwargs)
    #     self.object = None

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                if form.is_valid():
                    form.save()
                    messages.info(request, f'Cliente actualizado satisfactoriamente!')
                else:
                    messages.error(request, form.errors)
            else:
                data['error'] = 'No ha ingresado datos en los campos'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de Cliente'
        context['list_url'] = self.success_url
        context['entity'] = 'Edición de Cliente'
        context['action'] = 'edit'
        return context


# Listado de Clientes
class ClientListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = Client
    template_name = 'list_client.html'
    permission_required = 'user.add_user'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                client = list(Client.objects.values(
                    'id',
                    'client',
                    'nit_client',
                    'address_client',
                    'phone_client',
                    'mail_client',
                    'active_client',
                ).order_by('-client'))
                return JsonResponse(client, safe=False)
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Clientes'
        context['create_url'] = reverse_lazy('client:client_create')
        context['list_url'] = reverse_lazy('client:client_list')
        context['entity'] = 'Clientes'
        return context


# Detalle Cliente
class ClientDetailView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DetailView):
    model = Client
    template_name = 'detail_client.html'
    permission_required = 'user.change_user'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return super(ClientDetailView, self).get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Detalle Cliente'
        context['entity'] = 'Detalle Cliente'
        context['list_url'] = reverse_lazy('client:client_list')
        return context
