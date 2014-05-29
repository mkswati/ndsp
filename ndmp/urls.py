from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from geonode.urls import *

urlpatterns = patterns('',

    # Static pages
	
url(r'^$', 'geonode.views.index', {'template': 'site_index.html'}, name='home'),
url(r'^riskinfo/$', TemplateView.as_view(template_name='riskinfo.html'), name='riskinfo'),
url(r'^faqs/$', TemplateView.as_view(template_name='faqs.html'), name='faqs'),
url(r'^nwg/$', TemplateView.as_view(template_name='nwg.html'), name='nwg'),
url(r'^casestudies/$', TemplateView.as_view(template_name='casestudies.html'), name='casestudies'),
url(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name='contact'),
url(r'^message/$', TemplateView.as_view(template_name='message.html'), name='message'),
url(r'^feedback/$', TemplateView.as_view(template_name='feedback.html'), name='feedback'),
url(r'^project/$', TemplateView.as_view(template_name='project.html'), name='project'),

url(r'^riskassessment/$', TemplateView.as_view(template_name='riskassessment.html'), name='riskassessment'),
	
 ) + urlpatterns

urlpatterns += patterns('', (r'^safe/', include('safe_geonode.urls')),)
