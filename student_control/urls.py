from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.views.static import serve

from student_control_app.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),
    url(r'^$', index, name='root_url'),
    url(r'^teacher/(?P<teacher_id>\d+)/$', teacher, name='teacher_details'),
    url(r'^subject/(?P<subject_id>\d+)/$', subject, name='subject_details'),
    url(r'^activity/(?P<activity_id>\d+)/$', activity, name='activity_details'),
    url(r'^students/', students, name='students_list'),
    url(r'^teachers/', teachers, name='teachers_list'),
    url(r'^subjects/', subjects, name='subjects_list'),
]
