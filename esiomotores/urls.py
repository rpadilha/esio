from django.conf.urls import url, include
from django.contrib import admin
from django.http import HttpResponse
from esiomotores.core import views as core_views
from esiomotores.contacts import views as contact_views
from esiomotores.blog import views as blog_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', core_views.home, name='home'),
    url(r'^contato/$', contact_views.contact, name='contacts'),
    url(r'^institucional/$', core_views.about, name='about'),
    url(r'^noticia/(?P<slug>[\w-]*)/$', blog_views.one_blog, name='one_blog'),
    url(r'^noticias/(?P<category>[\w-]*)/(?P<page>[1-9]|[1-9][0-9])/$', blog_views.blog, name='blog'),
    url(r'^noticias/pesquisa/(?P<search>[\w ]*)/(?P<page>[1-9]|[1-9][0-9])/$', blog_views.search, name='search'),
    url(r'^solucoes/$', core_views.solutions, name='solutions'),
    url(r'^s3direct/', include('s3direct.urls')),
    # url(r'^robots.txt', lambda x: HttpResponse("User-Agent: *\nDisallow: /admin/", content_type="text/plain"), name="robots_file"),

]
