from django.db import models
from django.utils.translation import gettext_lazy as _

class Topic(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title

class Subtopic(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return f"{self.topic.title} — {self.title}"
