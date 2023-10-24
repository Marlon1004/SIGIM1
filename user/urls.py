from django.urls import path
from user import views



urlpatterns = [

    #path('', views.login, name="Login"),

    path('registro', views.register, name="Registro"),

    #path('home', views.home, name="Home"),
    #path('grupos', views.grupos, name="Grupos"),
    #path('convocatorias', views.convocatorias, name="Convocatorias"),
    #path('resultados', views.resultados, name="Resultados"),
]