import django
from django.conf.urls import url

try:
    from django.views.i18n import javascript_catalog
    jsc_view = javascript_catalog
except ImportError:
    from django.views.i18n import JavaScriptCatalog
    jsc_view = JavaScriptCatalog.as_view()

from jet.views import add_bookmark_view, remove_bookmark_view, toggle_application_pin_view, model_lookup_view

app_name = 'jet'
urlpatterns = [
    url(
        r'^add_bookmark/$',
        add_bookmark_view,
        name='add_bookmark'
    ),
    url(
        r'^remove_bookmark/$',
        remove_bookmark_view,
        name='remove_bookmark'
    ),
    url(
        r'^toggle_application_pin/$',
        toggle_application_pin_view,
        name='toggle_application_pin'
    ),
    url(
        r'^model_lookup/$',
        model_lookup_view,
        name='model_lookup'
    ),
    url(
        r'^jsi18n/$',
        jsc_view,
        name='jsi18n'
    ),
]

if django.VERSION[:2] < (1, 8):
    from django.conf.urls import patterns
    urlpatterns = patterns('', *urlpatterns)
