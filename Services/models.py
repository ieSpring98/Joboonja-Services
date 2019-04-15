import uuid
from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return "{}: {}".format(self.id, self.name)


class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    imageUrl = models.TextField()
    budget = models.IntegerField()
    deadline = models.DateTimeField()
    creationDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}: {}".format(self.id, self.title)


class ProjectSkill(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    point = models.IntegerField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return "{} -> {}({})".format(self.project, self.skill, self.point)
