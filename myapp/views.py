from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from myapp.models import Clientes
from django.urls import reverse_lazy


# Create your views here.

class ClientesList(ListView):
    model = Clientes
    queryset = Clientes.objects.all()

class ClientesCreate(CreateView):
    model = Clientes
    fields = '__all__'
    success_url = reverse_lazy('myapp:list')

class ClientesUpdate(UpdateView):
    model = Clientes
    fields = '__all__'
    success_url = reverse_lazy('myapp:list')

class ClientesDetail(DetailView):
    queryset = Clientes.objects.all()

class ClientesDelete(DeleteView):
    model = Clientes
    fields = '__all__'
    success_url = reverse_lazy('myapp:list')