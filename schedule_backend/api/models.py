# api/models.py

from django.db import models
import uuid

class Schedule(models.Model):
    unique_link = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    faculty = models.CharField(max_length=100)
    course = models.IntegerField()

    def __str__(self):
        return f"{self.faculty} - {self.course}"

class Lesson(models.Model):
    schedule = models.ForeignKey(Schedule, related_name='lessons', on_delete=models.CASCADE)
    day = models.CharField(max_length=20)
    subject = models.CharField(max_length=200, blank=True)
    lesson_type = models.CharField(max_length=50, blank=True)
    time = models.CharField(max_length=50, blank=True)
    custom_time = models.CharField(max_length=50, blank=True)
    cabinet = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.day} - {self.subject}"
