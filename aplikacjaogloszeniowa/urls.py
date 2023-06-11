from django.urls import path

from aplikacjaogloszeniowa import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dodanieogloszenia/', views.addAnnouncement_view, name="dodanieOgloszenia"),
]
