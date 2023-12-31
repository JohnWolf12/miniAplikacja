from django.urls import path

from aplikacjaogloszeniowa import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dodanieogloszenia/', views.addAnnouncement_view, name="dodanieOgloszenia"),
    path('ogloszenie/<int:id>', views.announcement_view, name="ogloszenie"),
    path('edycjaogloszenia/<int:id>', views.editAnnouncement_view, name="edycjaOgloszenia"),
    path('usuniecieogloszenia/<int:id>', views.deleteAnnouncement_view, name="usuniecieOgloszenia"),
]
