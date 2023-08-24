from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from badania.models import TypBadan, Zlecenie, Badanie, ZlecenieForm, BadanieForm
# Create your views here.
def index(request):
    zlecenia= Zlecenie.objects.all()
    context={"zlecenia": zlecenia}
    return render(request, "badania/index.html", context)

def dodawanie_zlecenia(request):
    form=ZlecenieForm()

    if request.method == 'POST':
        form=ZlecenieForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/badania')
    context={'form':form}
    return render(request, "badania/dodawanie_zlecenia.html",context)

def edycja_zlecenia(request,pk):
    zlecenie=get_object_or_404(Zlecenie,pk=pk)
    form=ZlecenieForm(instance=zlecenie)
    form_badanie=BadanieForm()

    badania=zlecenie.wyniki.all()
    zrobione_pk=[b.typBadania.pk for b in badania]
    typy=TypBadan.objects.exclude(pk__in=zrobione_pk)

    form_badanie.fields['typBadania'].queryset=typy

    if request.method=='POST':
        if 'zlecenie_form' in request.POST:
            form=ZlecenieForm(request.POST,instance=zlecenie)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/badania/"+str(pk)+"/edycja_zlecenia")


        elif 'badanie_form' in request.POST:
            form_badanie=BadanieForm(request.POST)
            if form_badanie.is_valid():
                badanie=form_badanie.save(commit=False)
                badanie.zlecenie=zlecenie
                badanie.save()
                return HttpResponseRedirect("/badania/"+str(pk)+"/edycja_zlecenia")

    context={'form':form, 'form_badanie':form_badanie, 'badania':badania, 'zlecenie':zlecenie}

    return render(request, "badania/edycja_zlecenia.html",context)

def usuwanie(request, pk):
    zlecenie=get_object_or_404(Zlecenie,pk=pk)
    zlecenie.delete()
    return HttpResponseRedirect('/badania')
