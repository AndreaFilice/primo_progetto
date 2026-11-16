from django.urls import path
from news.views import home, articoloDetailView, listaArticoli, giornalistaDetailView, queryBase, listaGiornalisti, \
    indice

app_name = "news"
urlpatterns = [
    path('', home, name='homeview'),
    path("articoli/<int:pk>", articoloDetailView, name="articolo_detail"),
    path("lista_articoli/<int:pk>", listaArticoli, name="lista_articoli_giornalista"),
    path("giornalisti/<int:pk>", giornalistaDetailView, name="giornalistaDetailView"),
    path("lista_articoli/", listaArticoli, name="lista_articoli"),
    path("lista_giornalisti/", listaGiornalisti, name="listaGiornalisti"),
    path("query/", queryBase, name="queryBase"),
    path("indice/", indice, name="indice")
]