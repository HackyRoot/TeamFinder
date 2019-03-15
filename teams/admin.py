from django.contrib import admin
from . import models

registered_models = [models.Team, models.TeamManagement]

admin.site.register(registered_models)

