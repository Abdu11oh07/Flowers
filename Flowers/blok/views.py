from django.shortcuts import render, get_object_or_404
from .models import Turlar, Gullar

def index(request):
    turlar = Turlar.objects.all()
    gullar = Gullar.objects.all()
    context = {
        "turlar": turlar,
        "gullar": gullar
    }
    return render(request, 'type.html', context)

def posts_by_turlar(request, turlar_id):
    turlar = get_object_or_404(Turlar, id=turlar_id)
    gullar = Gullar.objects.filter(type_id=turlar_id)
    context = {
        "turlar": turlar,
        "gullar": gullar
    }
    return render(request, 'type.html', context)

def posts_by_gullar(request, gullar_id):
    gul = get_object_or_404(Gullar, id=gullar_id)
    context = {
        'gul': gul
    }
    return render(request, 'gulllar_detail.html', context)
