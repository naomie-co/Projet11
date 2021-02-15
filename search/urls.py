from django.conf.urls import url, include

from . import views


#link to namespace in plateforme.urls.py
app_name = 'search'
urlpatterns = [
    url(r'^products/$', views.products, name='products'),
    url(r'^(?P<product_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^my_selection/(?P<user>\w+)/$', views.my_selection, name='my_selection'),
    url(r'^legal/$', views.legal, name='legal'),

]

