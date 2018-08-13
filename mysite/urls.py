from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from core import views as core_views
from core.views import check_profile , download_profile

urlpatterns = [
   url(r'^admin/', include(admin.site.urls)),
    url(r'^$', core_views.home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^check_profile/$', check_profile, name='check_profile'),
    url(r'^download_profile/$', download_profile, name='download_profile'),
]
