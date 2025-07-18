from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),  # Include the URLs from the tarefas app
]
