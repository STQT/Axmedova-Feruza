"""
Tests for core application
"""
from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from datetime import date
from .models import (
    Profile, Service, Publication, Project, BlogPost,
    Achievement, Testimonial, ServiceOrder, ContactMessage
)


class ProfileModelTest(TestCase):
    """Tests for Profile model"""
    
    def setUp(self):
        self.profile = Profile.objects.create(
            full_name='Test Sociologist',
            email='test@example.com',
            phone='+123456789',
            bio='Test bio',
            education='Test education',
            specialization='Test specialization',
            experience_years=10
        )
    
    def test_profile_creation(self):
        """Test profile was created correctly"""
        self.assertEqual(self.profile.full_name, 'Test Sociologist')
        self.assertEqual(self.profile.experience_years, 10)
    
    def test_profile_str(self):
        """Test string representation"""
        self.assertEqual(str(self.profile), 'Test Sociologist')


class ServiceModelTest(TestCase):
    """Tests for Service model"""
    
    def setUp(self):
        self.service = Service.objects.create(
            title='Test Service',
            description='Test description',
            is_active=True
        )
    
    def test_service_creation(self):
        """Test service was created correctly"""
        self.assertEqual(self.service.title, 'Test Service')
        self.assertTrue(self.service.is_active)
    
    def test_service_ordering(self):
        """Test service ordering"""
        service2 = Service.objects.create(
            title='Service 2',
            description='Description 2',
            order=1
        )
        services = Service.objects.all()
        self.assertEqual(services[0].order, 0)
        self.assertEqual(services[1].order, 1)


class ViewsTest(TestCase):
    """Tests for views"""
    
    def setUp(self):
        self.client = Client()
        self.profile = Profile.objects.create(
            full_name='Test Sociologist',
            email='test@example.com',
            phone='+123456789',
            bio='Test bio',
            education='Test education',
            specialization='Test specialization',
            experience_years=10
        )
    
    def test_index_view(self):
        """Test index page loads successfully"""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
    
    def test_about_view(self):
        """Test about page loads successfully"""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')
    
    def test_services_view(self):
        """Test services page loads successfully"""
        response = self.client.get(reverse('services'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'services.html')
    
    def test_contact_view_get(self):
        """Test contact page GET request"""
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')
    
    def test_contact_view_post(self):
        """Test contact form submission"""
        data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'subject': 'Test Subject',
            'message': 'Test message'
        }
        response = self.client.post(reverse('contact'), data)
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.assertEqual(ContactMessage.objects.count(), 1)
    
    def test_blog_view(self):
        """Test blog page loads successfully"""
        response = self.client.get(reverse('blog'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog.html')
    
    def test_portfolio_view(self):
        """Test portfolio page loads successfully"""
        response = self.client.get(reverse('portfolio'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio.html')
    
    def test_publications_view(self):
        """Test publications page loads successfully"""
        response = self.client.get(reverse('publications'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'publications.html')


class BlogPostModelTest(TestCase):
    """Tests for BlogPost model"""
    
    def setUp(self):
        self.post = BlogPost.objects.create(
            title='Test Post',
            content='Test content',
            is_published=True,
            published_at=timezone.now()
        )
    
    def test_blogpost_creation(self):
        """Test blog post was created correctly"""
        self.assertEqual(self.post.title, 'Test Post')
        self.assertTrue(self.post.is_published)
    
    def test_slug_generation(self):
        """Test slug is generated automatically"""
        self.assertIsNotNone(self.post.slug)
    
    def test_increment_views(self):
        """Test views counter increment"""
        initial_views = self.post.views_count
        self.post.increment_views()
        self.assertEqual(self.post.views_count, initial_views + 1)


class PublicationModelTest(TestCase):
    """Tests for Publication model"""
    
    def setUp(self):
        self.publication = Publication.objects.create(
            title='Test Publication',
            authors='Test Author',
            year=2024,
            publication_type='article'
        )
    
    def test_publication_creation(self):
        """Test publication was created correctly"""
        self.assertEqual(self.publication.title, 'Test Publication')
        self.assertEqual(self.publication.year, 2024)
    
    def test_publication_str(self):
        """Test string representation"""
        expected = 'Test Publication (2024)'
        self.assertEqual(str(self.publication), expected)


class ProjectModelTest(TestCase):
    """Tests for Project model"""
    
    def setUp(self):
        self.project = Project.objects.create(
            title='Test Project',
            description='Test description',
            start_date=date(2024, 1, 1),
            role='Test Role',
            organization='Test Org'
        )
    
    def test_project_creation(self):
        """Test project was created correctly"""
        self.assertEqual(self.project.title, 'Test Project')
        self.assertEqual(self.project.role, 'Test Role')
    
    def test_is_ongoing(self):
        """Test is_ongoing property"""
        self.assertTrue(self.project.is_ongoing)
        
        self.project.end_date = date(2024, 12, 31)
        self.project.save()
        self.assertFalse(self.project.is_ongoing)


class FormTests(TestCase):
    """Tests for forms"""
    
    def setUp(self):
        self.service = Service.objects.create(
            title='Test Service',
            description='Test description'
        )
    
    def test_contact_form_valid(self):
        """Test contact form with valid data"""
        from .forms import ContactForm
        
        data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'subject': 'Test',
            'message': 'Test message'
        }
        form = ContactForm(data=data)
        self.assertTrue(form.is_valid())
    
    def test_service_order_form_valid(self):
        """Test service order form with valid data"""
        from .forms import ServiceOrderForm
        
        data = {
            'service': self.service.id,
            'full_name': 'John Doe',
            'email': 'john@example.com',
            'phone': '+123456789',
            'message': 'Test order message'
        }
        form = ServiceOrderForm(data=data)
        self.assertTrue(form.is_valid())

