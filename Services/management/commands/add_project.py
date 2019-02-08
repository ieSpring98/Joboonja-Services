import datetime
import random

from django.core.management import BaseCommand

from Services.models import Project, ProjectSkill, Skill


class Command(BaseCommand):
    help = "Add a project"

    def handle(self, *args, **options):
        projects = [
            {
                "name": "طراحی فرم بیمه مانند بیمیتو با ری اکت",
                "description": "بنده نیاز دارم امکانات شبیه سایت بیمیتو داشته باشم. فرم بیمه+فرم یادآوری",
                "skills": ["React"],
                "imageUrl": "FUCK"
            },
            {
                "name": "تولید گزارشات مختلف از روی یک دیتابیس",
                "description": "سلام و خسته نباشید ما یک دیتابیس داریم که دارای جدوال مختلفی هستش نیار به یک برنامه نویس که دارای مهارت کافی در زمینه مای اسکیول باشه و مقدار کمی جاوا برای اینکه بتونه روی این دیتا بیس کوئری های خوب , بهینه بنویسه...)",
                "skills": ["Java", "MySQL"],
                "imageUrl": "FUCK"
            },
            {
                "name": "آموزش و همکاری در طراحی مدار جمع کننده مربوط به مقاله ",
                "description": "با سلامپروژه مربوط به طراحی مدار جمع کننده موجود در مقاله پیوست می باشد.",
                "skills": ["C", "Java", "Linux"],
                "imageUrl": "FUCK"
            },
            {
                "name": " طراحي سايت مرتبط با بورس",
                "description": "طراحی سایت با قلبلیت های: چت روم و اخبار و مشاهده در موبایل و اقصال به ای پی آی و داشبورد حرفه ای و جذاب و نسخه تریال و دوزبانه.",
                "skills": ["PHP", "Java", "HTML"],
                "imageUrl": "FUCK"
            },
            {
                "name": " پروژه نظارتی امنیتی چشم ",
                "description": "تیم گیک لب (آزمایشگاه گیک) قصد دارد یک پروژه نظارتی امنیتی را برونسپاری کند.این پروژه شامل بخش های مختلفی است که نیاز به تخصص های ذکر شده داردما به دوستانی برنامه نویس هستند نیاز داریم نه کسانی که کد نویس هستند.قطعا برنامه نویس واقعی مفهوم این جمله را درک می کند کد ها باید تماما بر اساس استاندارد های ارائه شده نوشته شوند توضیحات بیشتر قابل ارائه در این بخش نیست.",
                "skills": ["Java", "PHP"],
                "imageUrl": "FUCK"
            }
        ]

        project = random.choice(projects)
        projectSkills = []
        now = int(datetime.datetime.now().timestamp())
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), datetime.datetime.now().timestamp() * 1000)
        instance = Project.objects.create(name=project["name"], description=project["description"],
                                          imageUrl=project["imageUrl"],
                                          budget=random.randint(5, 50) * 100000,
                                          deadline=datetime.datetime.fromtimestamp(random.randint(now + 300,
                                                                                                  now + 1800)))
        for skill in project["skills"]:
            print(skill)
            projectSkills.append(ProjectSkill.objects.create(skill=Skill.objects.get(name=skill),
                                                             point=random.randint(1, 5), project=instance))
