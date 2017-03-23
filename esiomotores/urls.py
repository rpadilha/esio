from django.conf.urls import url
from django.contrib import admin
from esiomotores.core import views as core_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', core_views.home),
]
