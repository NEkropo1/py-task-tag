from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from task.forms import TaskForm
from task.models import Task, Tag


# Create your views here.

class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    queryset = Task.objects.select_related("tag")
    success_url = reverse_lazy("task:tasks")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "task/task_form.html"
    success_url = reverse_lazy("task:tasks")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("task:tasks")
    template_name = "task/task_confirm_delete.html"


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.all()
    context_object_name = "tasks"


class ToggleTaskStanceView(generic.View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.toggle_stance()
        task.save()
        return redirect(reverse_lazy("task:tasks"))


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    queryset = Tag.objects.all()
    success_url = reverse_lazy("task:tags")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    template_name = "task/tag_form.html"
    success_url = reverse_lazy("task:tags")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("task:tags")
    template_name = "task/tag_confirm_delete.html"


class TagListView(generic.ListView):
    model = Tag
    fields = "__all__"
    context_object_name = "tags"

