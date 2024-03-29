from rest_framework import serializers

from Services.models import Skill, Project, ProjectSkill


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('name',)


class ProjectSerializer(serializers.ModelSerializer):
    skills = serializers.SerializerMethodField()
    deadline = serializers.SerializerMethodField()
    creationDate = serializers.SerializerMethodField()

    def get_skills(self, obj):
        result = [{
            'name': item.skill.name,
            'point': item.point
        } for item in ProjectSkill.objects.filter(project=obj)]
        return result

    def get_deadline(self, obj):
        return round(obj.deadline.timestamp() * 1000)

    def get_creationDate(self, obj):
        return round(obj.creationDate.timestamp() * 1000)

    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'imageUrl', 'budget', 'deadline', 'creationDate', 'skills')
