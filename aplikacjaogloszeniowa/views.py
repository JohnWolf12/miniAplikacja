from django.shortcuts import render, redirect

from aplikacjaogloszeniowa.forms import AnnouncementForm


def index(request):
    context = {

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
