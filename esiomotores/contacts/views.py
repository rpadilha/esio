from django.contrib import messages
from django.core import mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from esiomotores.contacts.forms import ContactForm


def contact (request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)


def create (request):
    form = ContactForm(request.POST)

    if not form.is_valid():
        return render(request, 'contact.html', {'form': form})

    contact = form.save(commit=False)
    contact.ipaddr = _get_ip_address(request, form.cleaned_data)
    contact.save()

    _send_mail('Nova mensagem do site',
               contact.email,
               #'rvprepresentacao@gmail.com',
                'tonare@gmail.com',
               'contact_email.txt',
               {'contact': contact})

    messages.success(request, 'Mensagem enviada com sucesso!')
    return HttpResponseRedirect('/contato/')


def new (request):
    return render(request, 'contact.html',
                  {'form': ContactForm()})


def _send_mail (subject, from_, to, template_name, context):
    body = render_to_string(template_name, context)
    mail.send_mail(subject, body, from_, [to])


def _get_ip_address (request, context):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        return x_forwarded_for.split(',')[-1]
    return request.META.get('REMOTE_ADDR')
