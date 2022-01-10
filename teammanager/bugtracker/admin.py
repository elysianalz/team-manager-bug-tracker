from django.contrib import admin
from .models import Project
from .models import Bug
from .models import Activity
# Register your models here.
admin.site.register(Project)
admin.site.register(Bug)
admin.site.register(Activity)
