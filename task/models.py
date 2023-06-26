from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    content = models.TextField()
    created = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    tag = models.ManyToManyField(
        Tag,
        related_name="tasks",
        blank=True,
        null=True,
        default=None,
    )

    class Meta:
        ordering = [
            "-is_completed",
            "-created"
        ]

    def toggle_stance(self):
        self.is_completed = (not self.is_completed)

    def __str__(self) -> str:
        return self.content
