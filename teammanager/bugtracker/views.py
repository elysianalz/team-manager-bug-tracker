from django.shortcuts import render
from django.views import generic
from .models import Project
from .models import Bug
from .models import Activity

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

class ProjectsView(generic.ListView):
    template_name = "bugtracker/projectspage.html"
    context_object_name = "data"

    def get_queryset(self):
        data_set = {
            'projects': Project.objects.all(),
        }
        return data_set

class ProjectView(generic.ListView):
    template_name = "bugtracker/project.html"
    context_object_name = "data"

    def get_queryset(self):
        data_set = {
            'project': Project.objects.get(pk=self.kwargs['pk']),
            'bugs': Bug.objects.filter(project_id=self.kwargs['pk']),
        }
        return data_set

class BugView(generic.DetailView):
    template_name="bugtracker/bug.html"
    context_object_name = "data"

    def get_queryset(self):
        return Bug.objects.filter(pk=self.kwargs['bpk'])

class ReportBugView(generic.ListView):
    template_name = "bugtracker/bugreportform.html"
    context_object_name = "data"

    def get_queryset(self):
        return Project.objects.get(pk=self.kwargs['pk'])

class LoginView(generic.TemplateView):
    template_name = "bugtracker/login.html"
