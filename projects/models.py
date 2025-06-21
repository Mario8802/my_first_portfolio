from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    tech_stack = models.CharField(max_length=255)
    github_link = models.URLField()
    live_demo_link = models.URLField(blank=True, null=True)
    screenshot = models.ImageField(upload_to='projects/', blank=True, null=True)

    def __str__(self):
        return self.name
