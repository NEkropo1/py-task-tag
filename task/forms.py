from django import forms
from django.forms import CheckboxSelectMultiple

from task.models import Task, Tag


class TaskForm(forms.ModelForm):
    tag = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=CheckboxSelectMultiple,
    )

    class Meta:
        model = Task
        fields = [
            "content",
            "deadline",
            "tag",
        ]
