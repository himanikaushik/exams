from django.conf.urls.defaults import patterns, include, url
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('core.views',
    # Examples:
    url(r'^(?P<exam_group>[-\w]+)/$', 'exam_group', name='exam_group'),
    url(r'^(?P<exam_group>[-\w]+)/(?P<specialization>[-\w]+)/$', 'specialization', name='specialization'),
    url(r'^(?P<exam_group>[-\w]+)/(?P<specialization>[-\w]+)/(?P<exam>[-\w]+)/$', 'exam', name='exam'),
)
