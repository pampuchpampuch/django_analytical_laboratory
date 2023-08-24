from badania.models import TypBadan, Zlecenie, Badanie
from datetime import datetime, timezone
def _load():
    t1=TypBadan.objects.create(nazwa='TSH',
                                jednostka='mU/l',
                                min_wart_ref=0.32,
                                maks_wart_ref=5)
    t2=TypBadan.objects.create(nazwa='B12',
                                jednostka='pg/ml',
                                min_wart_ref=197,
                                maks_wart_ref=771)
    t3=TypBadan.objects.create(nazwa='ABC',
                                jednostka='pg/ml',
                                min_wart_ref=197,
                                maks_wart_ref=771)
    z1=Zlecenie.objects.create(imie='Parzak',
                                nazwisko='Pampuchpampuch',
                                opis='pampuchy nie mają krwi i tak')

_load()
