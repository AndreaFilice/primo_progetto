from django.shortcuts import render
import random

# Create your views here.
def indice(request):
    return render(request, "indice_prova.html")

def massimo(request):
    dict = { 'var1': random.randint(1, 20), 'var2': random.randint(1, 20), 'var3': random.randint(1, 20) }
    return render(request, "massimo.html", dict)

def pari(request):
    lista_numeri = []
    i = 0
    numeri_pari = 0

    for i in range(0, 30):
        lista_numeri.append(random.randint(1, 20))

    for value in lista_numeri:
        if(value % 2 == 0): 
            numeri_pari += 1

    dict = {'dict': {'Valori': lista_numeri, 'Numeri Pari': numeri_pari}}
    return render(request, "pari.html", dict)

def studenti(request):
    dict_studenti = {'studenti': {"Andrea Filice": True, "Simone Gallotti": True, "Riccardo De Diana": False, "Gioele Tolotta": False, "Gerevini Morgan": True}}

    return render(request, "studenti.html", dict_studenti)