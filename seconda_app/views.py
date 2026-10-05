from django.shortcuts import render
import datetime

# Create your views here.
def esempio_if(request):
    dict = { 'var1': 200, 'var2': 200, 'var3': 300 }
    return render(request, "es_if.html", dict)

def esempio_if_elif(request):
    dict = { 'var1': 200, 'var2': 200, 'var3': 300 }
    return render(request, "if_else_elif.html", dict)

def es_for(request):
    dict = { 'list1': [1, datetime.date(2019, 7, 16), 'Do not give up!'], 'list2': [1, datetime.date(2019, 7, 16), 'Do not give up!'], 'my_dict' : {'chiave1': 'Valore 1', 'chiave2': 'Valore 2'} }
    return render(request, "es_for.html", dict)