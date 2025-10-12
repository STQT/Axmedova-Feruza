from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('publications/', views.publications, name='publications'),
    path('publications/<int:pk>/', views.publication_detail, name='publication_detail'),
    path('blog/', views.blog, name='blog'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('contact/', views.contact, name='contact'),
    path('order/', views.order_service, name='order_service'),
    path('order/<int:service_id>/', views.order_service, name='order_service_direct'),
]

