from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('perfil/', views.perfil, name='perfil'),
    path('cupons/', views.cupons, name='cupons'),
    path('sobrenos/', views.sobrenos, name='sobrenos'),
    path('passeios/', views.passeios, name='passeios'),
    path('passeio/<int:passeio_id>/', views.passeio_detalhes, name='passeio_detalhes'),
    path('hospedagens/', views.hospedagens, name='hospedagens'),
    path('hospedagem/<int:hospedagem_id>/', views.hospedagem_detalhes, name='hospedagem_detalhes'),
    path('hospedagem/<int:hospedagem_id>/', views.hospedagem_detalhes, name='hospedagem_detalhes'),
    path('eventos/', views.eventos, name='eventos'),
    path('evento/<int:evento_id>/', views.evento_detalhes, name='evento_detalhes'),
    path('politica-privacidade/', views.politica_privacidade, name='politica_privacidade'),
    path('termos-servico/', views.termos_servico, name='termos_servico'),
]