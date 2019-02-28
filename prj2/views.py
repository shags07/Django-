# \books\views.py

from django.shortcuts import render

def search_form(request):
    return render(request, 'prj2/search_form.html')
