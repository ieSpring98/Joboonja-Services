from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from Services.models import Skill, Project
from Services.serializers import SkillSerializer, ProjectSerializer


class CustomJSONRenderer(JSONRenderer):
    charset = 'utf-8'


class ServicesView(ViewSet):
    renderer_classes = (CustomJSONRenderer,)

    def get_skills(self, request):
        skills = Skill.objects.all()
        return Response(SkillSerializer(skills, many=True).data)

    def get_projects(self, request):
        projects = Project.objects.order_by('-creationDate')
        return Response(ProjectSerializer(projects, many=True).data)
