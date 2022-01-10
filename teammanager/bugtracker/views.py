from django.shortcuts import render
from django.views import generic
from .models import Project
from .models import Bug
from .models import Activity
# Create your views here.
class IndexView(generic.ListView):
    template_name = "bugtracker/index.html"
    context_object_name = "data"

    def get_queryset(self):
        data_set = {
            'projects': Project.objects.all(),
            'bugs': Bug.objects.all(),
            'activities': Activity.objects.all(),
        }
        return data_set

class LoginView(generic.TemplateView):
    template_name = "bugtracker/login.html"
