from django.conf.urls.static import static
from django.urls import path

from bpmprometro import settings
from core.client.views import *

app_name = 'client'

urlpatterns = [
    path('add/', ClientCreateView.as_view(), name='client_create'),
    path('list/', ClientListView.as_view(), name='client_list'),
    path('update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('detail/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
