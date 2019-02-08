from django.core.management import BaseCommand

from Services.models import Skill


class Command(BaseCommand):
    help = "Add some skills"

    def handle(self, *args, **options):
        skills = [
            'HTML', 'CSS', 'Javascript', 'Django', 'Nodejs', 'React', 'C++', 'Python', 'Java', 'Photoshop', 'MySQL'
            , 'C', 'Linux'
        ]
        Skill.objects.all().delete()
        Skill.objects.bulk_create([
            Skill(name=item) for item in skills
        ])
