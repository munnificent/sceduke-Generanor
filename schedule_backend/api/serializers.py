# api/serializers.py

from rest_framework import serializers
from .models import Schedule, Lesson

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['day', 'subject', 'lesson_type', 'time', 'custom_time', 'cabinet']

class ScheduleSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True)
    unique_link = serializers.UUIDField(read_only=True)

    class Meta:
        model = Schedule
        fields = ['unique_link', 'faculty', 'course', 'lessons']

    def create(self, validated_data):
        lessons_data = validated_data.pop('lessons')
        schedule = Schedule.objects.create(**validated_data)
        for lesson_data in lessons_data:
            Lesson.objects.create(schedule=schedule, **lesson_data)
        return schedule
