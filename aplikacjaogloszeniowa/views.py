from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404

from aplikacjaogloszeniowa.forms import AnnouncementForm
from aplikacjaogloszeniowa.models import Kategoria, Ogloszenie


def index(request):
    kategorie = Kategoria.objects.all()
    if 'q' in request.GET:
        nazwa = request.GET.get("q")
    else:
        nazwa = ''
    if 'k' in request.GET:
        kategoria = request.GET.get("k")
    else:
        kategoria = ''
    if 'min' in request.GET:
        cenamin = request.GET.get("min")
        if cenamin == '':
            cmin = ''
            cenamin = '0'
        else:
            cmin = cenamin
    else:
        cmin = ''
        cenamin = '0'
    if 'max' in request.GET:
        cenamax = request.GET.get("max")
        if cenamax == '':
            cmax = ''
            cenamax = '99999999'
        else:
            cmax = cenamax
    else:
        cmax = ''
        cenamax = '99999999'
    if 'sort' in request.GET:
        sort = request.GET.get("sort")
    else:
        sort = ''
    if kategoria == '':
        if sort == '1':
            ogloszenia = Ogloszenie.objects.filter(nazwa__icontains=nazwa, cena__gte=cenamin,
                                                   cena__lte=cenamax).order_by('cena')
        elif sort == '2':
            ogloszenia = Ogloszenie.objects.filter(nazwa__icontains=nazwa, cena__gte=cenamin,
                                                   cena__lte=cenamax).order_by('-cena')
        else:
            ogloszenia = Ogloszenie.objects.filter(nazwa__icontains=nazwa, cena__gte=cenamin,
                                                   cena__lte=cenamax).order_by('-id')
    else:
        if sort == '1':
            ogloszenia = Ogloszenie.objects.filter(kategoria_id=kategoria, nazwa__icontains=nazwa, cena__gte=cenamin,
                                                   cena__lte=cenamax).order_by('cena')
        elif sort == '2':
            ogloszenia = Ogloszenie.objects.filter(kategoria_id=kategoria, nazwa__icontains=nazwa, cena__gte=cenamin,
                                                   cena__lte=cenamax).order_by('-cena')
        else:
            ogloszenia = Ogloszenie.objects.filter(kategoria_id=kategoria, nazwa__icontains=nazwa, cena__gte=cenamin,
                                                   cena__lte=cenamax).order_by('-id')
    paginator = Paginator(ogloszenia, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "kategorie": kategorie,
        "nazwa": nazwa,
        "kategoria": kategoria,
        "cenamin": cmin,
        "cenamax": cmax,
        "sort": sort,
        "page_obj": page_obj
    }
    return render(request, 'aplikacjaogloszeniowa/index.html', context)


def addAnnouncement_view(request):
    if request.method == 'POST':
        addannouncementform = AnnouncementForm(request.POST)
        if addannouncementform.is_valid():
            addannouncementform.save()
            return redirect("/")
    else:
        addannouncementform = AnnouncementForm()
    context = {
        'addannouncementform': addannouncementform
    }
    return render(request, 'aplikacjaogloszeniowa/announcementAdd.html', context)


def announcement_view(request, id):
    ogloszenie = get_object_or_404(Ogloszenie, pk=id)
    context = {
        'ogloszenie': ogloszenie
    }
    return render(request, 'aplikacjaogloszeniowa/announcement.html', context)


def editAnnouncement_view(request, id):
    ogloszenie = get_object_or_404(Ogloszenie, pk=id)
    if request.method == 'POST':
        editannouncementform = AnnouncementForm(request.POST, instance=ogloszenie)
        if editannouncementform.is_valid():
            editannouncementform.save()
            return redirect("/")
    else:
        editannouncementform = AnnouncementForm(instance=ogloszenie)
    context = {
        'editannouncementform': editannouncementform
    }
    return render(request, 'aplikacjaogloszeniowa/announcementEdit.html', context)


def deleteAnnouncement_view(request, id):
    Ogloszenie.objects.filter(id=id).delete()
    return redirect('/')
