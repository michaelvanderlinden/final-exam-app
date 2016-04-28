from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^mrw/class-is-done.gif', hello.views.gif, name='gif'),
    url(r'^robots.txt', hello.views.robots, name='robots'),
    url(r'^posts/:id$', hello.views.posts, name = 'posts'),
    url(r'^posts/new$', hello.views.postsnew, name = 'postsnew'),
    url(r'^admin/', include(admin.site.urls)),
]
