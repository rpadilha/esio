from django.db.models import Q
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.shortcuts import resolve_url as r
from math import ceil
from esiomotores.blog.models import Blogs
from esiomotores.blog.forms import BlogSearchForm
from esiomotores.core.forms import CustomerMKTForm
from esiomotores.functions import register_customer


def blog(request, category, page):
    if request.method == 'POST':
        # Será usando para processar a pesquisa por notícias
        if 'search' in request.POST:
            return redirectToSearch(request)
        else:
            return register_customer(request, r('blog', category=category, page=page))
    else:
        # IF CATEGORY está entre ['geral', 'catalogos', 'eventos', 'novidades', 'promocoes', 'outros']
        # Será mostrada uma página de notícias (independente de categoria)
        if category in ['geral', Blogs.CATALOG, Blogs.EVENT, Blogs.NEWS, Blogs.PROMO, Blogs.OTHER]:
            return showFullBlogPage(request, category, page)

        # Caso contrário, será mostrada uma notícia específica
        else:
            raise Http404


def one_blog(request, slug):
    if request.method == 'POST':
        # Será usando para processar a pesquisa por notícias
        if 'search' in request.POST:
            return redirectToSearch(request)
        else:
            return register_customer(request, r('one_blog', slug=slug))
    else:
        return showEspecificBlog(request, slug)


def search(request, page, search):
    if request.method == 'POST':
        # Será usando para processar a pesquisa por notícias
        if 'search' in request.POST:
            return redirectToSearch(request)
        else:
            return register_customer(request, r('search', search=search, page=page))
    else:
        return showSearchPage(request, page, search)


def notfound(request):
    return render(request, 'notfound.html', {'formSearch': BlogSearchForm(), 'form': CustomerMKTForm()})


#######################
## Support Functions ##
#######################
def showEspecificBlog(request, slug):
    blog = get_object_or_404(Blogs.objects.prefetch_related('contents_set').filter(publish=True), slug=slug)
    return render(request, 'blog.html', {'blog': blog, 'formSearch': BlogSearchForm(), 'form': CustomerMKTForm()})


def showFullBlogPage(request, category, page):
    qs = Blogs.objects.prefetch_related('contents_set').filter(publish=True)

    if not category == 'geral':
        qs = qs.filter(category = category)
    else:
        qs = qs.filter(~Q(contents__text='Não existe conteúdo cadastrado para esta categoria.'))

    try:
        page = int(page)
    except:
        raise Http404

    # Slice no QS para mostrar apenas os 5 registros referentes à página que está sendo acessada
    categorized_blogs = get_list_or_404(qs[5*(page-1):5*page])

    stats = get_blog_stats(category, qs.count(), page)
    return render(request, 'categories.html',
                  {'categorized_blogs': categorized_blogs, 'stats': stats,
                   'formSearch': BlogSearchForm(), 'form': CustomerMKTForm()})


def showSearchPage(request, page, search):
    page = int(page)
    category = 'pesquisa'
    qs = Blogs.objects.prefetch_related('contents_set').filter(publish=True)
    qs = qs.filter(Q(title__contains=search) | Q(contents__text__contains=search)).distinct()
    qs = qs.filter(~Q(contents__text='Não existe conteúdo cadastrado para esta categoria.'))

    try:
        categorized_blogs = get_list_or_404(qs[5*(page-1):5*page])
    except:
        return notfound(request)

    stats = get_blog_stats(category, qs.count(), page, search)

    return render(request, 'categories.html',
                  {'categorized_blogs': categorized_blogs, 'stats': stats,
                   'formSearch': BlogSearchForm(), 'form': CustomerMKTForm()})


def redirectToSearch(request):
    form = BlogSearchForm(request.POST)
    form.is_valid()

    return HttpResponseRedirect(r('search', page=1, search=form.cleaned_data['search']))


def get_blog_stats(category, blogs, page, search=''):
    stats = {'category': category, 'total': blogs, 'actual_page': page, 'total_pages': ceil(blogs/5)}

    if page == 1:
        stats['previous'] = False
    else:
        stats['previous'] = True
        if category is None:
            stats['previous_link'] = Blogs.BLOG_DIR + str(page - 1) + '/'
        elif category == 'pesquisa':
            stats['previous_link'] = Blogs.BLOG_DIR + category + '/' + str(search) + '/' + str(page - 1) + '/'
        else:
            stats['previous_link'] = Blogs.BLOG_DIR + category + '/' + str(page-1) + '/'

    if page*5 < blogs:
        stats['next'] = True
        if category is None:
            stats['next_link'] = Blogs.BLOG_DIR + str(page + 1) + '/'
        elif category == 'pesquisa':
            stats['next_link'] = Blogs.BLOG_DIR + category + '/' + str(search) + '/' + str(page + 1) + '/'
        else:
            stats['next_link'] = Blogs.BLOG_DIR + category + '/' + str(page+1) + '/'
    else:
        stats['next'] = False

    return stats


def _get_blog_months():
    values = []
    qs = Blogs.objects.all()

    for blog in qs:
        values.append(str(blog.created_at.year) + '/' + str(blog.created_at.month))

    return remove_duplicates(values)


def remove_duplicates (values):
    output = []
    seen = set()
    for value in values:
        if value not in seen:
            output.append(value)
            seen.add(value)
    return output
