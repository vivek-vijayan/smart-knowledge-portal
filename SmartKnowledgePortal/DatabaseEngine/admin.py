from django.contrib import admin
from django.apps import apps
# Register your models here.

post_models = apps.get_app_config('DatabaseEngine').get_models()

for model in post_models:
    admin.site.register(model)