from django.contrib import admin
from .models import Project
from .models import Bug
from .models import Activity
from .models import Position
from .models import User
from .models import Status
from .models import Flag
from .models import Employment
from .models import Assignment
from .models import Report
from .models import BugAssign
# Register your models here.
admin.site.register(Project)
admin.site.register(Bug)
admin.site.register(Activity)
admin.site.register(Position)
admin.site.register(User)
admin.site.register(Status)
admin.site.register(Flag)
admin.site.register(Employment)
admin.site.register(Assignment)
admin.site.register(Report)
admin.site.register(BugAssign)
