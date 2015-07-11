from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^users/$', views.user_list),
    url(r'^users/(?P<pk>[0-9]+)/$', views.user_detail)
]