from django.urls import path
from . import views

app_name="badania"

urlpatterns = [path("",views.index,name="index"),
                path("<int:pk>/edycja_zlecenia",views.edycja_zlecenia,name="edycja_zlecenia"),
                path("dodawanie_zlecenia",views.dodawanie_zlecenia,name="dodawanie_zlecenia"),
                path('usuwanie/<int:pk>', views.usuwanie, name='usuwanie'),

]
