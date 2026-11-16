from django.urls import path
from prova_pratica_1_B.views import massimo, pari, studenti, indice

app_name = "prova_pratica_1_B"
urlpatterns = [
    path("indice", indice, name="indice"),
    path("massimo", massimo, name="massimo"),
    path("pari", pari, name="pari"),
    path("studenti", studenti, name="studenti")
]