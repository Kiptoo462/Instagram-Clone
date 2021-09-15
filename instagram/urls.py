from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url(r'^$',views.welcome,name = 'welcome'),
    url(r'^accounts/profile/$',views.profile,name = 'profile'),
    url(r'^profile/(\d+)',views.profile_others,name = 'visitprofile'),
    url(r'^search/profile$', views.search, name='profileresults'),
    url(r'^timeline$', views.timeline, name='timeline'),
    url(r'^profile_edit$', views.profile_edit, name='edit'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    