from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view()),
    path("projects/", views.ProjectsView.as_view()),
    path("projects/<int:pk>/", views.ProjectView.as_view()),
    path("projects/<int:pk>/reportbug/", views.ReportBugView.as_view()),
    path("projects/<int:pk>/<int:bpk>", views.BugView.as_view()),
    path("login/", views.LoginView.as_view()),
]
