from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^foo/', hello.views.foo, name='foo'),
    url(r'^mrw/semester-ends.gif', hello.views.gif, name='gif'),
    url(r'^admin/', include(admin.site.urls)),
]
