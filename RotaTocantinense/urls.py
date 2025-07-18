from django.urls import path, include

urlpatterns = [
    path('', include('Home.urls')),  # Include the URLs from the tarefas app
]
