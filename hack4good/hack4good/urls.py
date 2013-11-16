from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

from accounts.views import root

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hack4good.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', root), 
    url(r'^relief/', include('relief.urls')),
    url(r'^accounts/', include('accounts.urls')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
