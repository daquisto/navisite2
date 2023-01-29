# pages/views.py
from django.urls import reverse
from django.views import generic

from .models import Guitar


class GuitarBase:
    """ Base values for guitar classes """
    model = Guitar
    fields = '__all__'


class HomePageView(GuitarBase, generic.ListView):
    """ Home Page
    Will display all records in the Guitar model"""


class GuitarDetail(GuitarBase, generic.DetailView):
    """ Display details of the guitar record """


class GuitarAdd(GuitarBase, generic.CreateView):
    """ Create a new guitar record """
    def get_success_url(self):
        return reverse('home')


class GuitarUpdate(GuitarBase, generic.UpdateView):
    """ To update guitar records """
    def get_success_url(self):
        return reverse('home')


class GuitarDelete(GuitarBase, generic.DeleteView):
    """ TO delete the guitar record """
    def get_success_url(self):
        return reverse('home')




