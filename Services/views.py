from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from Services.models import Skill, Project
from Services.serializers import SkillSerializer, ProjectSerializer


class ServicesView(ViewSet):
    renderer_classes = (JSONRenderer,)

    def get_skills(self, request):
        skills = Skill.objects.all()
        return Response(SkillSerializer(skills, many=True).data)

    def get_projects(self, request):
        projects = Project.objects.all()
        return Response(ProjectSerializer(projects, many=True).data)

