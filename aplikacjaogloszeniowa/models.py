from django.db import models


class Kategoria(models.Model):
    nazwa = models.CharField(max_length=50)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "kategoria"
        verbose_name_plural = "kategorie"


class Ogloszenie(models.Model):
    nazwa = models.CharField(max_length=100)
    cena = models.DecimalField(max_digits=9, decimal_places=2)
    opis = models.TextField(blank=True, max_length=1000)
    kategoria = models.ForeignKey(Kategoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "ogłoszenie"
        verbose_name_plural = "ogłoszenia"
