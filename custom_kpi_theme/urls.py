"""custom_kpi_theme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from kpi.urls import urlpatterns
from custom_kpi_theme.views import home

# urlpatterns += [
#
#     # include your urls here
#
# ]

urlpatterns = [
    url(r'^$', home, name='kpi-root'),
 ] + urlpatterns
