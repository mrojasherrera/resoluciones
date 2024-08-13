from django.urls import path
from resoluciones import views


urlpatterns = [
    path('resoluciones/', views.resoluciones_all, name='resoluciones_all')
]
