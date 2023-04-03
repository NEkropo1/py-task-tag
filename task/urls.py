from django.urls import path

from task.views import TaskListView, TagListView, TaskCreateView

urlpatterns = [
    path("", TaskListView.as_view(), name="tasks"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tags/", TagListView.as_view(), name="tags"),
]

app_name = "task"
