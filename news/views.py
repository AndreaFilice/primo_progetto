from multiprocessing import context

from django.db.models import Model
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404

from news.models import Giornalista, Articolo

# Create your views here.
"""
VERSIONE 1 HOME RESPONSE

def home(request):
    articoli = ""
    giornalisti = ""

    for art in Articolo.objects.all():
        articoli += (art.titolo + "<br>")

    for gio in Giornalista.objects.all():
        giornalisti += (gio.nome + "<br>")

    response = "Articoli:<br>" + articoli + "<br>Giornalisti:<br>" + giornalisti;

    return HttpResponse("<h1>" + response + "</h1>")
"""

"""
VERSIONE 2 HOME RESPONSE
In questa versione, in confronto alla prima, cambia la modalità di raccolta dei dati.
Se nella prima versione concatenavamo più stringhe coi valori letti dal database, in questa versione aggiungiamo direttamente -
ad un Array i valori dei vari articoli.

def home(request):
    articoli = []
    giornalisti = []

    for art in Articolo.objects.all():
        articoli.append(art.titolo)

    for gio in Giornalista.objects.all():
        giornalisti.append(gio.nome)

    response = str(articoli) + "<br>" + str(giornalisti);

    return HttpResponse("<h1>" + response + "</h1>")
"""

def home(request):
    articoli = Articolo.objects.all()
    giornalisti = Giornalista.objects.all()

    context = {"articoli": articoli, "giornalisti": giornalisti}
    print(context)

    return render(request, "homepage_news.html", context)

def articoloDetailView(request, pk):
    articolo = get_object_or_404(Articolo, pk=pk)
    context = {"articolo": articolo}
    return render(request, "articolo_detail.html", context)
