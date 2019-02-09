from django.core.management import BaseCommand

from Services.models import Skill


class Command(BaseCommand):
    help = "Add some skills"

    def handle(self, *args, **options):
        skills = [
            'HTML', 'CSS', 'Javascript', 'Django', 'Node.js', 'React', 'C++', 'Python', 'Java', 'Photoshop', 'MySQL',
            'SQL', 'C', 'Linux', 'PHP', 'Android', 'SEO'
        ]
        Skill.objects.all().delete()
        Skill.objects.bulk_create([
            Skill(name=item) for item in skills
        ])
