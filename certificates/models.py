from django.db import models


class Certificate(models.Model):
    course_name = models.CharField(max_length=120)
    course_link = models.URLField()
    certificate_link = models.URLField()

    def __str__(self) -> str:
        return self.course_name


