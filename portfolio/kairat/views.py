from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView

from kairat.forms import ContactForm


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'kairat/index.html'
    success_url = reverse_lazy('/')

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('/')

