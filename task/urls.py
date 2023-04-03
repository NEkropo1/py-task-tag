from django.urls import path

from task.views import (
    TaskListView,
    TagListView,
    TaskCreateView,
    ToggleTaskStanceView,
    TaskUpdateView,
    TaskDeleteView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="tasks"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/update/<int:pk>/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/delete/<int:pk>/", TaskDeleteView.as_view(), name="task-delete"),
    path("tasks/toggle-stance/<int:pk>/", ToggleTaskStanceView.as_view(), name="toggle-task-stance"),
    path("tags/", TagListView.as_view(), name="tags"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/update/<int:pk>/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/delete/<int:pk>/", TagDeleteView.as_view(), name="tag-delete"),

]

app_name = "task"
