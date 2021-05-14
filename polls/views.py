
# Create your views here.
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import PersonCreationForm
from .models import Person, City , District, State, Country


def all_data(request):
    data=Person.objects.all()
    return render(request,'polls/alldata.html',{'pdata':data})

def person_create_view(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('person_add')
    return render(request, 'polls/home.html', {'form': form})


def person_update_view(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonCreationForm(instance=person)
    if request.method == 'POST':
        form = PersonCreationForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_change', pk=pk)
    return render(request, 'polls/home.html', {'form': form})


# AJAX
def load_states(request):
    country_id = request.GET.get('country_id')
    states = State.objects.filter(country_id=country_id)
    return render(request, 'polls/statelist.html', {'states': states})
    #return JsonResponse(list(states.values('id', 'name')), safe=False)

# AJAX
def load_districts(request):
    state_id = request.GET.get('state_id')
    districts = District.objects.filter(state_id=state_id)
    return render(request, 'polls/district.html', {'districts': districts})
    # return JsonResponse(list(cities.values('id', 'name')), safe=Fa

# AJAX
def load_cities(request):
    district_id = request.GET.get('district_id')
    cities = City.objects.filter(district_id=district_id).all()
    return render(request, 'polls/citylist.html', {'cities': cities})
    # return JsonResponse(list(cities.values('id', 'name')), safe=Fa