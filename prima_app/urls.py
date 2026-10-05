from django.urls import path
from prima_app.views import homepage, welcome, lista, chi_siamo, variabili, indice

app_name = "prima_app"
urlpatterns = [
    path("", indice, name="indice"),
    path("welcome", welcome, name="welcome"),
    path("lista", lista, name="lista"),
    path("chi_siamo", chi_siamo, name="chiSiamo"),
    path("variabili", variabili, name="variabili"),
    path("homepage", homepage, name="homepage")
]