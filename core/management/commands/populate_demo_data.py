"""
Management command to populate database with demo data
Usage: python manage.py populate_demo_data
"""
from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import date, timedelta
from core.models import (
    Profile, Service, Publication, Project, BlogPost,
    Achievement, Testimonial
)


class Command(BaseCommand):
    help = 'Populate database with demo data for testing'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting to populate demo data...'))

        # Create Profile
        if not Profile.objects.exists():
            profile = Profile.objects.create(
                full_name='Ахмедова Феруза Медетовна',
                birth_date=date(1980, 5, 15),
                education='Национальный университет Узбекистана, Факультет социологии, 2002',
                academic_degree='Доктор социологических наук',
                academic_title='Профессор',
                bio='''Феруза Медетовна Ахмедова - ведущий социолог, специалист в области социальной структуры, 
                       социальных изменений и общественного развития. Автор более 100 научных публикаций, 
                       включая 5 монографий. Руководитель крупных международных исследовательских проектов.
                       
                       Более 20 лет опыта преподавательской и научно-исследовательской деятельности.
                       Член редакционных коллегий ведущих социологических журналов.''',
                specialization='Социальная структура общества, социология образования, методы социологических исследований',
                experience_years=20,
                languages='Русский, Узбекский, Английский',
                email='f.akhmedova@example.com',
                phone='+998 90 123 45 67',
                address='Ташкент, Узбекистан',
                linkedin='https://linkedin.com/in/fakhmedova',
                researchgate='https://researchgate.net/profile/F_Akhmedova',
                orcid='0000-0001-2345-6789'
            )
            self.stdout.write(self.style.SUCCESS('✓ Profile created'))
        else:
            self.stdout.write(self.style.WARNING('Profile already exists'))

        # Create Services
        services_data = [
            {
                'title': 'Социологические исследования',
                'description': 'Проведение комплексных социологических исследований для организаций, государственных структур и научных учреждений',
                'price_from': 150000,
                'duration': 'от 1 месяца',
                'icon': 'fas fa-search',
                'order': 1
            },
            {
                'title': 'Консультации по социальным проектам',
                'description': 'Экспертные консультации по разработке и реализации социальных проектов и программ',
                'price_from': 50000,
                'duration': '1-2 часа',
                'icon': 'fas fa-users',
                'order': 2
            },
            {
                'title': 'Анализ данных',
                'description': 'Статистический анализ социологических данных, интерпретация результатов',
                'price_from': 80000,
                'duration': 'от 1 недели',
                'icon': 'fas fa-chart-line',
                'order': 3
            },
            {
                'title': 'Разработка опросников',
                'description': 'Создание профессиональных анкет и опросников для различных типов исследований',
                'price_from': 30000,
                'duration': '3-5 дней',
                'icon': 'fas fa-clipboard-list',
                'order': 4
            },
            {
                'title': 'Образовательные программы',
                'description': 'Проведение тренингов, семинаров и курсов по социологии',
                'price_from': 100000,
                'duration': '1-3 дня',
                'icon': 'fas fa-graduation-cap',
                'order': 5
            },
            {
                'title': 'Научная экспертиза',
                'description': 'Рецензирование научных работ, экспертиза исследовательских проектов',
                'price_from': 40000,
                'duration': '1-2 недели',
                'icon': 'fas fa-certificate',
                'order': 6
            }
        ]

        for service_data in services_data:
            Service.objects.get_or_create(
                title=service_data['title'],
                defaults=service_data
            )
        self.stdout.write(self.style.SUCCESS(f'✓ {len(services_data)} Services created'))

        # Create Publications
        publications_data = [
            {
                'title': 'Социальная стратификация в современном обществе',
                'publication_type': 'book',
                'authors': 'Ахмедова Ф.М.',
                'year': 2023,
                'publisher': 'Издательство "Наука"',
                'pages': '324',
                'isbn': '978-5-02-040123-4',
                'abstract': 'Монография посвящена исследованию процессов социальной стратификации...',
                'keywords': 'социология, стратификация, социальная структура',
                'is_featured': True
            },
            {
                'title': 'Методология социологических исследований в XXI веке',
                'publication_type': 'article',
                'authors': 'Ахмедова Ф.М., Иванов И.И.',
                'year': 2024,
                'journal': 'Социологические исследования',
                'volume': '12',
                'pages': '45-67',
                'doi': '10.12345/socis.2024.12.45',
                'abstract': 'Статья анализирует современные методы социологических исследований...',
                'keywords': 'методология, социология, исследования',
                'citation_count': 15,
                'is_featured': True
            },
            {
                'title': 'Образование и социальная мобильность',
                'publication_type': 'article',
                'authors': 'Ахмедова Ф.М.',
                'year': 2023,
                'journal': 'Вопросы образования',
                'volume': '8',
                'pages': '120-145',
                'doi': '10.12345/education.2023.8.120',
                'abstract': 'Исследование взаимосвязи образования и социальной мобильности...',
                'keywords': 'образование, социальная мобильность, общество',
                'citation_count': 23,
                'is_featured': True
            }
        ]

        for pub_data in publications_data:
            Publication.objects.get_or_create(
                title=pub_data['title'],
                defaults=pub_data
            )
        self.stdout.write(self.style.SUCCESS(f'✓ {len(publications_data)} Publications created'))

        # Create Projects
        projects_data = [
            {
                'title': 'Социальная адаптация молодежи',
                'description': 'Комплексное исследование процессов социальной адаптации молодежи в условиях современного общества',
                'start_date': date(2023, 1, 1),
                'end_date': date(2024, 12, 31),
                'role': 'Научный руководитель',
                'organization': 'Национальный университет Узбекистана',
                'funding': 'Министерство науки и образования',
                'results': 'Опубликовано 5 статей, проведено 3 конференции',
                'order': 1
            },
            {
                'title': 'Цифровизация и социальные изменения',
                'description': 'Анализ влияния цифровых технологий на социальные структуры и процессы',
                'start_date': date(2024, 6, 1),
                'end_date': None,
                'role': 'Главный исследователь',
                'organization': 'Институт социологии',
                'funding': 'Международный научный фонд',
                'results': 'Проект в процессе реализации',
                'is_active': True,
                'order': 2
            }
        ]

        for project_data in projects_data:
            Project.objects.get_or_create(
                title=project_data['title'],
                defaults=project_data
            )
        self.stdout.write(self.style.SUCCESS(f'✓ {len(projects_data)} Projects created'))

        # Create Blog Posts
        blog_posts_data = [
            {
                'title': 'Социология в эпоху цифровизации',
                'slug': 'sociologiya-v-epohu-cifrovizacii',
                'content': '''Цифровизация меняет все аспекты нашей жизни, включая способы проведения 
                              социологических исследований. Онлайн-опросы, анализ больших данных, 
                              искусственный интеллект - все это открывает новые возможности для социологов.
                              
                              В этой статье я расскажу о современных трендах в социологии...''',
                'excerpt': 'Как цифровые технологии меняют социологическую науку',
                'category': 'Методология',
                'tags': 'цифровизация, социология, технологии',
                'is_published': True,
                'published_at': timezone.now() - timedelta(days=7)
            },
            {
                'title': 'Социальная стратификация: теория и практика',
                'slug': 'socialnaya-stratifikaciya',
                'content': '''Социальная стратификация - один из ключевых концептов социологии.
                              В этой статье мы рассмотрим основные теории стратификации...''',
                'excerpt': 'Обзор теорий социальной стратификации',
                'category': 'Теория',
                'tags': 'стратификация, теория, общество',
                'is_published': True,
                'published_at': timezone.now() - timedelta(days=14)
            }
        ]

        for blog_data in blog_posts_data:
            BlogPost.objects.get_or_create(
                slug=blog_data['slug'],
                defaults=blog_data
            )
        self.stdout.write(self.style.SUCCESS(f'✓ {len(blog_posts_data)} Blog posts created'))

        # Create Achievements
        achievements_data = [
            {
                'title': 'Лауреат премии "Лучший социолог года"',
                'description': 'Премия Ассоциации социологов за выдающийся вклад в развитие социологии',
                'date': date(2023, 11, 15),
                'organization': 'Ассоциация социологов Узбекистана',
                'order': 1
            },
            {
                'title': 'Диплом за лучшую научную работу',
                'description': 'Награда за монографию по социальной стратификации',
                'date': date(2024, 3, 20),
                'organization': 'Министерство науки',
                'order': 2
            }
        ]

        for achievement_data in achievements_data:
            Achievement.objects.get_or_create(
                title=achievement_data['title'],
                defaults=achievement_data
            )
        self.stdout.write(self.style.SUCCESS(f'✓ {len(achievements_data)} Achievements created'))

        # Create Testimonials
        testimonials_data = [
            {
                'client_name': 'Александр Петров',
                'client_position': 'Директор',
                'client_organization': 'Институт социальных исследований',
                'text': 'Отличный специалист! Провела качественное исследование, результаты превзошли ожидания.',
                'rating': 5,
                'is_approved': True
            },
            {
                'client_name': 'Мария Соколова',
                'client_position': 'Руководитель проекта',
                'client_organization': 'НКО "Развитие"',
                'text': 'Профессиональный подход, глубокое понимание проблематики. Рекомендую!',
                'rating': 5,
                'is_approved': True
            },
            {
                'client_name': 'Джамшид Каримов',
                'client_position': 'Заведующий кафедрой',
                'client_organization': 'Национальный университет',
                'text': 'Ценный опыт сотрудничества. Высокий уровень научной экспертизы.',
                'rating': 5,
                'is_approved': True
            }
        ]

        for testimonial_data in testimonials_data:
            Testimonial.objects.get_or_create(
                client_name=testimonial_data['client_name'],
                defaults=testimonial_data
            )
        self.stdout.write(self.style.SUCCESS(f'✓ {len(testimonials_data)} Testimonials created'))

        self.stdout.write(self.style.SUCCESS('\n' + '='*50))
        self.stdout.write(self.style.SUCCESS('✅ Demo data successfully populated!'))
        self.stdout.write(self.style.SUCCESS('='*50))
        self.stdout.write(self.style.SUCCESS('\nYou can now:'))
        self.stdout.write(self.style.SUCCESS('1. Visit http://127.0.0.1:8000'))
        self.stdout.write(self.style.SUCCESS('2. Login to admin at http://127.0.0.1:8000/admin'))

