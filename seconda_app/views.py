from django.shortcuts import render

# Create your views here.
def esempio_if(request):
    dict = { 'var1': 200, 'var2': 200, 'var3': 300 }
    return render(request, "es_if.html", dict)

def esempio_if_elif(request):
    dict = { 'var1': 200, 'var2': 200, 'var3': 300 }
    return render(request, "if_else_elif.html", dict)