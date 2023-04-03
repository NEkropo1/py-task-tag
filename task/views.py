from django.shortcuts import render
from django.views import generic

from task.forms import TaskForm
from task.models import Task, Tag


# Create your views here.

class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    queryset = Task.objects.select_related("tag")


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.select_related("tag")


class TagListView(generic.ListView):
    model = Tag
