from multiprocessing import context

from django.db.models import Model
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404

from news.models import Giornalista, Articolo
from django.db.models import Q

import datetime

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


def listaArticoli(request, pk=None):
    if(pk == None):
        articoli = Articolo.objects.all()
    else:
        articoli = Articolo.objects.filter(giornalista_id=pk)

    context = {"articoli": articoli}

    return render(request, "lista_articoli.html", context)

"""
def queryBase(request):
    articoli_cognome = Articolo.objects.filter(giornalista__cognome='Rossi')
    numero_totale_articoli = Articolo.objects.count()
    giornalista_1 = Giornalista.objects.get(id=2)

    numero_articoli_giornalista_1 = Articolo.objects.filter(giornalista=giornalista_1).count()
    giornalisti_data = Giornalista.objects.filter(anno_di_nascita__gt=datetime.date(1990, 1, 1))

    articoli_del_giorno = Articolo.objects.filter(data=datetime.date(2023, 1, 1))
    articoli_periodo = Articolo.objects.filter(data__range=(datetime.date(2023, 1, 1), datetime.date(2023, 12, 31)))
    giornalisti_nati = Giornalista.objects.filter(anno_di_nascita__lt=datetime.date(1980, 1, 1))
    articoli_giornalisti = Articolo.objects.filter(giornalista__in=giornalisti_nati)
    giornalista_giovane = Giornalista.objects.order_by('anno_di_nascita').first()
    giornalista_anziano = Giornalista.objects.order_by('-anno_di_nascita').first()

    ultimi = Articolo.objects.order_by('-data')[:5]

    articoli_mese_anno = Articolo.objects.filter(data__month=1, data__year=2023)

    data = datetime.date(1990, 1, 1)
    visualizzazioni = 50
    articoli_con_and = Articolo.objects.filter(giornalista__anno_di_nascita__gt=data, visualizzazioni__gte=visualizzazioni)

    articoli_con_or = Articolo.objects.filter(Q(giornalista__anno_di_nascita__gt=data) | Q(visualizzazioni__lte=visualizzazioni))
    articoli_con_not = Articolo.objects.filter(~Q(giornalista__anno_di_nascita__lt=data))
    articoli_con_not = Articolo.objects.exclude(giornalista__anno_di_nascita__lt=data)

    context = {
        'articoli_cognome': articoli_cognome,
        'numero_totale_articoli': numero_totale_articoli,
        'giornalista_1': giornalista_1,
        'numero_articoli_giornalista_1': numero_articoli_giornalista_1,
        'giornalisti_data': giornalisti_data,
        'articoli_del_giorno': articoli_del_giorno,
        'articoli_periodo': articoli_periodo,
        'giornalisti_nati': giornalisti_nati,
        'articoli_giornalisti': articoli_giornalisti,
        'giornalista_giovane': giornalista_giovane,
        'giornalista_anziano': giornalista_anziano,
        'ultimi': ultimi,
        'articoli_mese_anno': articoli_mese_anno,
        'data': data,
        'visualizzazioni': visualizzazioni,
        'articoli_con_and': articoli_con_and,
        'articoli_con_or': articoli_con_or,
        'articoli_con_not': articoli_con_not,
    }

    return render(request, "query.html", context)
"""