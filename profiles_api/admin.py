from django.contrib import admin

# 27. Enable django admin (Register newly created model with django admin to display this model in admin interface)
from profiles_api import models

# Register model to be visible in admin site
admin.site.register(models.UserProfile)
