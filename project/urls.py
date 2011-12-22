from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.views.generic.simple import direct_to_template

urlpatterns = patterns("")

# admin urls
from django.contrib import admin
admin.autodiscover()
urlpatterns += patterns("",
    url(r"^admin/", include(admin.site.urls)),
)

# custom urls
urlpatterns += patterns("",
    url(r"^$", direct_to_template, {"template": "pages/home.html"}, name="home"),
    url(r'^robots\.txt$', direct_to_template, 
        {'template': 'robots.txt', 'mimetype': 'text/plain'}),
    url(r'^google.html$', direct_to_template, 
        {'template': 'google.html', 'mimetype': 'text/html'}),
)

# --- Staticfiles urls ---
if settings.DJANGO_SERVE_PUBLIC:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
