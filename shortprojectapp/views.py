from django.shortcuts import render, redirect
from .models import BloodDonor
from .forms import BloodDonorForm

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')


def load_form(request):
    form = BloodDonorForm
    context = {'form': form}
    return render(request, 'index.html', context)

def add(request):
    form = BloodDonorForm(request.POST)
    form.save()
    return redirect('/show')

def show(request):
    donor_form = BloodDonor.objects.all
    context = {'donor_form': donor_form}
    return render(request, 'show.html', context)

def edit(request, id):
    blood_donor = BloodDonor.objects.get(id = id)
    context = {'blood_donor': blood_donor}
    return render(request, 'edit.html', context)
    return redirect('/show')

def update(request, id):
    blood_donor = BloodDonor.objects.get(id = id)
    form = BloodDonorForm(request.POST, instance = blood_donor)
    form.save()
    return redirect('/show')

def delete(request, id):
    blood_donor = BloodDonor.objects.get(id = id)
    blood_donor.delete()
    return redirect('/show')

def search(request):
    given_input = request.POST['name']
    blood_group = BloodDonor.objects.filter( donor_blood_group__iexact = given_input )
    context = {'donor_form': blood_group}
    return render(request, 'show.html', context) 