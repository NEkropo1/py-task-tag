from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=255)


class Task(models.Model):
    content = models.TextField()
    created = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
        related_name="tasks",
    )

    class Meta:
        ordering = [
            "-is_completed",
            "-created"
        ]

    def __str__(self) -> str:
        return self.content

