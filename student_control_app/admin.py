from django.apps import apps
from django.contrib import admin

for model in apps.get_app_config('student_control_app').models.values():
    admin.site.register(model)
