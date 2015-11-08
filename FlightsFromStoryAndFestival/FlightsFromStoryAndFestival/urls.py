from django.conf.urls import include, url
from django.contrib import admin
#from authentication import views
#from metrics import views as metrics_views
#from metrics.views import MetricsViewSet
#from logs import views as logs_views
from rest_framework.urlpatterns import format_suffix_patterns
from alerts import views as alerts_views
from alerts.views import AlertsViewSet

from stories import views as stories_views
from stories.views import StoriesViewSet


#modify_metric_values = MetricsViewSet.as_view({
#        'post': 'create',
#        'delete': 'destroy'
#})


alert_views_values = AlertsViewSet.as_view({
                         'post': 'alerts_post',
                         'get': 'alerts_get'
})

story_views_values = StoriesViewSet.as_view({
                         'post': 'stories_post',
                         'get':  'stories_get'
})

urlpatterns = [
    url(r'^admin/?$', include(admin.site.urls)),
    url(r'^', include('rest_framework_swagger.urls')),
#    url(r'^login/?$', views.get_token),
#    url(r'^test-token/?$', views.test_auth),
#    url(r'^metrics/(?P<user_token>[A-Za-z0-9]+)/_names/?$', metrics_views.list_metric_names),
#    url(r'^metrics/(?P<user_token>[A-Za-z0-9]+)/_values/?$', metrics_views.list_metric_values),
#    url(r'^metrics/(?P<user_token>[A-Za-z0-9]+)/(?P<metric_name>[A-Za-z0-9_.-]+)/?$', modify_metric_values, name='modify_metrics'),
#    url(r'^logs/(?P<user_token>[A-Za-z0-9]+)/?$', logs_views.list_logs),
#    url(r'^logs/(?P<user_token>[A-Za-z0-9]+)/(?P<log_name>[A-Za-z0-9_.-]+)/?$', logs_views.post_logs),

#    url(r'^alerts/(?P<user_token>[A-Za-z0-9]+)/?$', alert_views_values, name='alerts'),
#    url(r'^alerts/(?P<user_token>[A-Za-z0-9]+)/(?P<id>[0-9]+)/?$', alerts_views.alert_detail,name='alerts_detail'),

    url(r'^stories/(?P<user_token>[A-Za-z0-9]+)/?$', story_views_values, name='stories'),
    url(r'^stories/(?P<user_token>[A-Za-z0-9]+)/(?P<id>[0-9]+)/?$', stories_views.stories_detail,name='stories_detail'),

    url(r'^festivals/(?P<user_token>[A-Za-z0-9]+)/?$', alert_views_values, name='festivals'),
    url(r'^festivals/(?P<user_token>[A-Za-z0-9]+)/(?P<id>[0-9]+)/?$', alerts_views.alert_detail,name='festivals_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
