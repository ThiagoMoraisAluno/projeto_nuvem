from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'recipes/pages/home.html')


def base(request):
    return render(request, 'recipes/pages/base.html')


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html')


def contato(request):
    return render(request, 'recipes/pages/contato.html')
