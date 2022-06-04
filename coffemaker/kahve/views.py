from django.shortcuts import render

from kahve.models import KahveModel

# Create your views here.
def index(request):
    return render(request, 'kahve/index.html')

def about(request):
    return render(request, 'kahve/about.html')

def products(request):
    kahve = KahveModel.objects.all()
    context={
        "kahveler":kahve,
    }
    return render(request, 'kahve/products.html', context)

def store(request):
    return render(request, 'kahve/store.html')
               