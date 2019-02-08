import uuid
from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)


class ProjectSkill(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    point = models.IntegerField()


class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    imageUrl = models.TextField()
    budget = models.IntegerField()
    deadline = models.DateTimeField()
    skills = models.ForeignKey(ProjectSkill, on_delete=models.CASCADE, default=None)
