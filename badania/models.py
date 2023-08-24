from django.db import models
from django.forms import ModelForm, HiddenInput, BooleanField, SelectDateWidget
import datetime
from django.db import IntegrityError


class TypBadan(models.Model):
    nazwa=models.CharField(max_length=80, unique=True)
    jednostka=models.CharField(max_length=80)
    min_wart_ref=models.FloatField()
    maks_wart_ref=models.FloatField()

    def __str__(self):
        return self.nazwa

class Zlecenie(models.Model):
    imie=models.CharField(max_length=80)
    nazwisko=models.CharField(max_length=80)
    data=models.DateField(default=datetime.datetime.today)
    godzina=models.TimeField(default=datetime.datetime.now)
    opis=models.TextField(blank=True)

    @property
    def wykonane(self):
        return len(self.wyniki.all())==len(TypBadan.objects.all())

class Badanie(models.Model):
    typBadania=models.ForeignKey(TypBadan, on_delete=models.PROTECT, related_name='wyniki')
    wynik=models.FloatField()
    zlecenie=models.ForeignKey(Zlecenie, on_delete=models.CASCADE, related_name='wyniki')
    class Meta:
        constraints = [models.UniqueConstraint(fields=['typBadania','zlecenie'], name='badanie')]


    @property
    def w_normie(self):
        return self.typBadania.min_wart_ref<=self.wynik<=self.typBadania.maks_wart_ref

class ZlecenieForm(ModelForm):
    zlecenie_form = BooleanField(widget=HiddenInput, initial=True)
    class Meta:
        model=Zlecenie
        fields='__all__'

    def __init__(self, *args, **kwargs):
        super(ZlecenieForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class BadanieForm(ModelForm):
    badanie_form = BooleanField(widget=HiddenInput, initial=True)
    class Meta:
        model=Badanie
        exclude = ['zlecenie']

    def __init__(self, *args, **kwargs):
        super(BadanieForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
