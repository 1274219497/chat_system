from django.conf.urls import include, url
from django.contrib import admin
from chat_web import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'chat_web_application.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.index),
    url(r'^cli/',views.click,name="click")
]
