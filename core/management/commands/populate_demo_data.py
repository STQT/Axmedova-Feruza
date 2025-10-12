"""
Management command to populate database with demo data
Usage: python manage.py populate_demo_data
"""
from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import date, timedelta
from core.models import (
    Profile, Service, Publication, Project, BlogPost,
    Achievement, Testimonial, Book
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

        # Create Blog Posts with rich HTML content
        blog_posts_data = [
            {
                'title': 'Социология в эпоху цифровизации',
                'slug': 'sociologiya-v-epohu-cifrovizacii',
                'content': '''
                    <h2>Введение</h2>
                    <p>Цифровизация меняет все аспекты нашей жизни, включая способы проведения социологических исследований. 
                    <strong>Онлайн-опросы</strong>, <strong>анализ больших данных</strong>, <strong>искусственный интеллект</strong> - 
                    все это открывает новые возможности для социологов.</p>
                    
                    <h3>Современные тренды</h3>
                    <ul>
                        <li><strong>Big Data анализ</strong> - обработка огромных массивов данных из социальных сетей</li>
                        <li><strong>Машинное обучение</strong> - автоматическое выявление паттернов в поведении</li>
                        <li><strong>Онлайн-исследования</strong> - проведение опросов через интернет-платформы</li>
                        <li><strong>Цифровая этнография</strong> - изучение онлайн-сообществ</li>
                    </ul>
                    
                    <h3>Преимущества цифровых методов</h3>
                    <ol>
                        <li>Быстрый сбор данных</li>
                        <li>Большой охват аудитории</li>
                        <li>Снижение затрат</li>
                        <li>Возможность автоматизации</li>
                    </ol>
                    
                    <blockquote>
                        <p><em>"Цифровая социология - это не просто новые методы, это новый способ понимания общества."</em></p>
                    </blockquote>
                    
                    <h3>Вызовы и проблемы</h3>
                    <p>Несмотря на очевидные преимущества, цифровая социология сталкивается с рядом <span style="color: #e74c3c;">важных проблем</span>:</p>
                    <ul>
                        <li>Проблемы конфиденциальности данных</li>
                        <li>Цифровое неравенство</li>
                        <li>Вопросы валидности онлайн-данных</li>
                        <li>Этические дилеммы</li>
                    </ul>
                    
                    <h3>Заключение</h3>
                    <p>Цифровизация социологии - это неизбежный процесс, который требует от исследователей 
                    <strong>новых компетенций</strong> и <strong>критического мышления</strong>. 
                    Важно найти баланс между традиционными и цифровыми методами.</p>
                ''',
                'excerpt': 'Как цифровые технологии меняют социологическую науку: новые методы, возможности и вызовы',
                'category': 'Методология',
                'tags': 'цифровизация, социология, технологии, big data',
                'is_published': True,
                'published_at': timezone.now() - timedelta(days=7)
            },
            {
                'title': 'Социальная стратификация: теория и практика',
                'slug': 'socialnaya-stratifikaciya',
                'content': '''
                    <h2>Что такое социальная стратификация?</h2>
                    <p><strong>Социальная стратификация</strong> - это иерархическое расположение индивидов и социальных групп 
                    в обществе на основе неравенства в доступе к ресурсам, власти и престижу.</p>
                    
                    <h3>Основные теории стратификации</h3>
                    
                    <h4>1. Марксистская теория</h4>
                    <p>Карл Маркс рассматривал общество как разделенное на <span style="color: #3498db;">классы</span> 
                    на основе отношения к средствам производства:</p>
                    <ul>
                        <li><strong>Буржуазия</strong> - владельцы средств производства</li>
                        <li><strong>Пролетариат</strong> - наемные работники</li>
                    </ul>
                    
                    <h4>2. Веберианская теория</h4>
                    <p>Макс Вебер предложил многомерную модель стратификации, включающую:</p>
                    <ol>
                        <li><strong>Класс</strong> (экономическое положение)</li>
                        <li><strong>Статус</strong> (социальный престиж)</li>
                        <li><strong>Власть</strong> (политическое влияние)</li>
                    </ol>
                    
                    <h4>3. Функционалистская теория</h4>
                    <p>Согласно <em>Дэвису и Муру</em>, стратификация необходима для общества, 
                    так как она мотивирует людей занимать важные позиции.</p>
                    
                    <h3>Современные тенденции</h3>
                    <table border="1" cellpadding="10" style="border-collapse: collapse; width: 100%;">
                        <thead>
                            <tr style="background-color: #3498db; color: white;">
                                <th>Аспект</th>
                                <th>Тенденция</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Мобильность</td>
                                <td>Снижение вертикальной мобильности</td>
                            </tr>
                            <tr style="background-color: #ecf0f1;">
                                <td>Средний класс</td>
                                <td>Размывание границ среднего класса</td>
                            </tr>
                            <tr>
                                <td>Неравенство</td>
                                <td>Рост имущественного неравенства</td>
                            </tr>
                        </tbody>
                    </table>
                    
                    <h3>Измерение стратификации</h3>
                    <p>Социологи используют различные индикаторы для измерения социальной позиции:</p>
                    <ul>
                        <li>Доход и богатство</li>
                        <li>Уровень образования</li>
                        <li>Профессиональный престиж</li>
                        <li>Стиль жизни</li>
                    </ul>
                    
                    <blockquote style="border-left: 4px solid #3498db; padding-left: 20px; color: #555;">
                        <p><em>"Общество без стратификации невозможно, но степень неравенства может и должна регулироваться."</em></p>
                    </blockquote>
                    
                    <h3>Выводы</h3>
                    <p>Понимание механизмов социальной стратификации критически важно для:</p>
                    <ul>
                        <li><strong>Анализа</strong> социального неравенства</li>
                        <li><strong>Разработки</strong> социальной политики</li>
                        <li><strong>Прогнозирования</strong> социальных изменений</li>
                    </ul>
                ''',
                'excerpt': 'Обзор основных теорий социальной стратификации: от Маркса до современности',
                'category': 'Теория',
                'tags': 'стратификация, теория, общество, неравенство, классы',
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

        # Create Books
        books_data = [
            {
                'title': 'Социология образования: теория и практика',
                'slug': 'sociologiya-obrazovaniya-teoriya-i-praktika',
                'author': 'Ахмедова Ф.М.',
                'description': '''
                    <h2>О книге</h2>
                    <p>Данная монография посвящена комплексному анализу <strong>социологии образования</strong> 
                    как важнейшей отрасли социологического знания.</p>
                    
                    <h3>Основное содержание</h3>
                    <ul>
                        <li>Теоретические основы социологии образования</li>
                        <li>Образование как социальный институт</li>
                        <li>Социальное неравенство в образовании</li>
                        <li>Современные тенденции развития образования</li>
                        <li>Эмпирические исследования в области образования</li>
                    </ul>
                    
                    <h3>Для кого эта книга</h3>
                    <p>Книга предназначена для:</p>
                    <ul>
                        <li><strong>Студентов</strong> социологических факультетов</li>
                        <li><strong>Аспирантов</strong> и молодых исследователей</li>
                        <li><strong>Преподавателей</strong> высших учебных заведений</li>
                        <li><strong>Практиков</strong> в области образования</li>
                    </ul>
                    
                    <blockquote style="border-left: 4px solid #3498db; padding-left: 20px;">
                        <p><em>"Образование - это не только передача знаний, но и важнейший механизм социализации и социальной мобильности."</em></p>
                    </blockquote>
                ''',
                'short_description': 'Комплексный анализ социологии образования: теория, методология и эмпирические исследования',
                'publisher': 'Издательство "Университет"',
                'publication_year': 2023,
                'isbn': '978-5-9916-1234-5',
                'pages': 324,
                'language': 'Русский',
                'price': 1500.00,
                'is_available': True,
                'is_featured': True,
                'order': 1
            },
            {
                'title': 'Методы социологических исследований',
                'slug': 'metody-sociologicheskih-issledovaniy',
                'author': 'Ахмедова Ф.М.',
                'description': '''
                    <h2>Описание</h2>
                    <p>Учебное пособие, охватывающее <strong>весь спектр методов</strong> современных социологических исследований.</p>
                    
                    <h3>Структура книги</h3>
                    <ol>
                        <li><strong>Количественные методы</strong>
                            <ul>
                                <li>Опросы и анкетирование</li>
                                <li>Статистический анализ</li>
                                <li>Эксперимент в социологии</li>
                            </ul>
                        </li>
                        <li><strong>Качественные методы</strong>
                            <ul>
                                <li>Глубинное интервью</li>
                                <li>Фокус-группы</li>
                                <li>Наблюдение</li>
                                <li>Кейс-стади</li>
                            </ul>
                        </li>
                        <li><strong>Смешанные методы</strong>
                            <ul>
                                <li>Триангуляция данных</li>
                                <li>Последовательный дизайн</li>
                                <li>Параллельный дизайн</li>
                            </ul>
                        </li>
                    </ol>
                    
                    <h3>Особенности издания</h3>
                    <ul>
                        <li>✓ Практические примеры из реальных исследований</li>
                        <li>✓ Пошаговые инструкции</li>
                        <li>✓ Задания для самостоятельной работы</li>
                        <li>✓ Глоссарий основных терминов</li>
                    </ul>
                    
                    <p><span style="color: #e74c3c;"><strong>Новинка!</strong></span> 
                    В книге представлены современные цифровые методы исследований.</p>
                ''',
                'short_description': 'Практическое руководство по количественным и качественным методам социологических исследований',
                'publisher': 'Издательство "Социология"',
                'publication_year': 2024,
                'isbn': '978-5-9916-5678-9',
                'pages': 456,
                'language': 'Русский',
                'price': 1800.00,
                'is_available': True,
                'is_featured': True,
                'order': 2
            },
            {
                'title': 'Социальная структура современного общества',
                'slug': 'socialnaya-struktura-sovremennogo-obschestva',
                'author': 'Ахмедова Ф.М., Иванов И.И.',
                'description': '''
                    <h2>О монографии</h2>
                    <p>Монография посвящена анализу <strong>трансформации социальной структуры</strong> 
                    в условиях глобализации и цифровизации.</p>
                    
                    <h3>Основные темы</h3>
                    <table border="1" cellpadding="10" style="border-collapse: collapse; width: 100%;">
                        <thead>
                            <tr style="background-color: #3498db; color: white;">
                                <th>Глава</th>
                                <th>Содержание</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Глава 1</td>
                                <td>Теоретические подходы к анализу социальной структуры</td>
                            </tr>
                            <tr style="background-color: #ecf0f1;">
                                <td>Глава 2</td>
                                <td>Классовая структура и социальная мобильность</td>
                            </tr>
                            <tr>
                                <td>Глава 3</td>
                                <td>Средний класс: кризис или трансформация?</td>
                            </tr>
                            <tr style="background-color: #ecf0f1;">
                                <td>Глава 4</td>
                                <td>Новые социальные группы в цифровую эпоху</td>
                            </tr>
                        </tbody>
                    </table>
                    
                    <h3>Научная значимость</h3>
                    <p>Работа основана на <strong>эмпирических данных</strong> масштабного исследования, 
                    проведенного в 2022-2023 годах в трех регионах страны.</p>
                    
                    <blockquote>
                        <p><em>"Понимание социальной структуры - ключ к пониманию динамики общественного развития."</em></p>
                    </blockquote>
                ''',
                'short_description': 'Анализ трансформации социальной структуры в условиях глобализации и цифровизации',
                'publisher': 'Издательство "Наука"',
                'publication_year': 2023,
                'isbn': '978-5-02-040789-3',
                'pages': 512,
                'language': 'Русский',
                'price': 2200.00,
                'is_available': True,
                'is_featured': False,
                'order': 3
            }
        ]

        for book_data in books_data:
            Book.objects.get_or_create(
                title=book_data['title'],
                defaults=book_data
            )
        self.stdout.write(self.style.SUCCESS(f'✓ {len(books_data)} Books created'))

        self.stdout.write(self.style.SUCCESS('\n' + '='*50))
        self.stdout.write(self.style.SUCCESS('✅ Demo data successfully populated!'))
        self.stdout.write(self.style.SUCCESS('='*50))
        self.stdout.write(self.style.SUCCESS('\nYou can now:'))
        self.stdout.write(self.style.SUCCESS('1. Visit http://127.0.0.1:8000'))
        self.stdout.write(self.style.SUCCESS('2. Visit http://127.0.0.1:8000/books (NEW!)'))
        self.stdout.write(self.style.SUCCESS('3. Login to admin at http://127.0.0.1:8000/admin'))

