from django.forms import *

from core.client.models import Client


class ClientForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['active_client'].label = ''
        for form in self.visible_fields():
            form.field.widget.attrs['autocomplete'] = 'off'

    class Meta:
        model = Client
        fields = [
            'client',
            'nit_client',
            'address_client',
            'phone_client',
            'mail_client',
            'contact_client',
            'active_client'
        ]
        widgets = {
            'client': TextInput(attrs={'class': 'form-control', 'required': True}),
            'nit_client': TextInput(attrs={'class': 'form-control', 'required': True}),
            'address_client': TextInput(attrs={'class': 'form-control', 'required': True}),
            'phone_client': TextInput(attrs={'class': 'form-control', 'required': True}),
            'contact_client': TextInput(attrs={'class': 'form-control', 'required': True}),
            'mail_client': EmailInput(attrs={'class': 'form-control', 'required': True}),
            'active_client': NullBooleanSelect(attrs={'class': 'form-control', 'hidden': True})
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                data = form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
