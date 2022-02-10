from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, CreateView, DeleteView, ListView, UpdateView
from .models import Code 

class AllCode(ListView):
    model = Code 


class CreateCode(CreateView):
    fields = "__all__"
    model = Code 


class UpdateCode(UpdateView):
    fields = "__all__"
    model = Code 

class DeleteCode(DeleteView):
    model = Code 
    success_url = reverse_lazy('codesnippets:code-list')

class ViewCode(DetailView):
    model = Code 