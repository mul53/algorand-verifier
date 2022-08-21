from django.contrib import admin

from main.models import App, AppVersion

# Register your models here.
admin.site.register(App)
admin.site.register(AppVersion)
