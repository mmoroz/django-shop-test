from django.shortcuts import render

def index(request):
    context = {
        'title':'Home page',
        'h1content':'Магазин мебели HOME!'
    }
    return render(request, 'main/index.html', context=context)
