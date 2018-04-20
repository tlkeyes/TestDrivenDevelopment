"""
Definition of urls for Superlists.
"""

from django.conf.urls import include, url
from lists import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', Superlists.views.home, name='home'),
    # url(r'^Superlists/', include('Superlists.Superlists.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^$', views.home_page, name='home'),
]
