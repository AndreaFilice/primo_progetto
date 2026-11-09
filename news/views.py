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


def listaArticoli(request, pk=None):
    if(pk == None):
        articoli = Articolo.objects.all()
    else:
        articoli = Articolo.objects.filter(giornalista_id=pk)

    context = {"articoli": articoli}

    return render(request, "lista_articoli.html", context)

def queryBase(request):
    articoli_cognome = Articolo.objects.filter(giornalista__cognome='Rossi')
    numero_totale_articoli = Articolo.objects.count()
    giornalista_1 = Giornalista.objects.get(id=1)

    numero_articoli_giornalista_1 = Articolo.objects.filter(giornalista=giornalista_1).count()
    articoli_ordinati = Articolo.objects.order_by('-visualizzazioni')
    articoli_senza_visualizzazioni = Articolo.objects.filter(visualizzazioni=0)
    articolo_piu_visualizzato = Articolo.objects.order_by('-visualizzazioni').first()
    giornalisti_data . Giornalista.objects.filter(anno_di_nascita_gt=datetime.date(1990, 1, 1))

    articoli_del_giorno . Articolo.objects.filter(data=datetime.date(2023, 1, 1))
    articoli_periodo = Articolo.objects.filter(data_range=(datetime.date(2023, 1, 1), datetime.date(2023, 12, 31)))
    giornalisti_nati = Giornalista.objects.filter(anno_di_nascita_lt=datetime.date(1980, 1, 1))
    articoli_giornalisti = Articolo.objects.filter(giornalista_in=giornalisti_nati)
    giornalista_giovane = Giornalista.objects.order_by('anno_di_nascita').first()
    giornalista_anziano = Giornalista.objects.order_by('-anno_di_nascita').first()

    ultimi = Articolo.objects.order_by('-data')[:5]
    articoli_minime_visualizzazioni = Articolo.objects.filter(visualizzazioni_gte=100)
    articoli_parola = Articolo.objects.filter(titolo_icontains='importante')

    context = {'articoli_cognome': articoli_cognome, 'numero totale articoli': numero_totale_articoli}