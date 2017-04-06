from django.shortcuts import render
from django.shortcuts import resolve_url as r
from esiomotores.core.forms import CustomerMKTForm
from esiomotores.functions import register_customer, get_blog_content


def home(request):
    if request.method == 'POST':
        return register_customer(request, r('home'))
    else:
        blog_preview = get_blog_content()
        return render(request, 'index.html', {'blog_preview': blog_preview, 'form': CustomerMKTForm()})


def about(request):
    if request.method == 'POST':
        return register_customer(request, r('about'))
    else:
        return render(request, 'about.html', {'form': CustomerMKTForm()})


def solutions(request):
    if request.method == 'POST':
        return register_customer(request, r('solutions'))
    else:
        return render(request, 'solutions.html', {'form': CustomerMKTForm()})
