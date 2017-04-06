from django.contrib import messages
from django.http import HttpResponseRedirect
from esiomotores.core.forms import CustomerMKTForm
from esiomotores.blog.models import Blogs


def register_customer(request, path):
    form = CustomerMKTForm(request.POST)

    if not form.is_valid():
        messages.error(request, form.errors['email'])

    else:
        customer = form.save(commit=False)
        customer.save()
        messages.success(request, 'Cadastro realizado com sucesso!')

    return HttpResponseRedirect(path + '#cadastro')


def get_blog_content():
    """This function should return a dict with the last 3 blog previews to the home view"""
    blog_preview = []
    qs = Blogs.objects.prefetch_related('contents_set').filter(publish=True)

    for blog in qs[0:3]:
        content = {}

        content['title'] = blog.title
        content['slug'] = blog.slug

        for blogcontent in blog.contents_set.all():
            if len(blogcontent.text) > 0:
                content['preview'] = blogcontent.text
                break

        blog_preview.append(content)

    return blog_preview