from django.urls import path, include
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', include('Home.urls')),  # Include the URLs from the tarefas app
]




urlpatterns = [
    path('admin/', admin.site.urls),          # <-- Adicione essa linha
    path('', include('Home.urls')),           # Rota do seu app principal
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)