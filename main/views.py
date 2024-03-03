from django.shortcuts import render

def index(request):
    test = 5
    result = test + 10
    return render(request, 'main/index.html', {"result": result})
