from django.contrib import admin
from . import models

registered_models = [models.Team]

admin.site.register(registered_models)

