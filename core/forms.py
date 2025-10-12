from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Row, Column, HTML
from .models import ServiceOrder, ContactMessage, BookOrder


class ServiceOrderForm(forms.ModelForm):
    """Форма заказа услуги"""
    
    class Meta:
        model = ServiceOrder
        fields = ['service', 'full_name', 'email', 'phone', 'organization', 'message', 'preferred_date']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5}),
            'preferred_date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'service': 'Выберите услугу',
            'full_name': 'Ваше имя',
            'email': 'Email',
            'phone': 'Телефон',
            'organization': 'Организация (необязательно)',
            'message': 'Опишите ваш запрос',
            'preferred_date': 'Предпочтительная дата',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('service', css_class='form-select mb-3'),
            Row(
                Column('full_name', css_class='form-group col-md-6 mb-3'),
                Column('email', css_class='form-group col-md-6 mb-3'),
            ),
            Row(
                Column('phone', css_class='form-group col-md-6 mb-3'),
                Column('organization', css_class='form-group col-md-6 mb-3'),
            ),
            Field('preferred_date', css_class='form-control mb-3'),
            Field('message', css_class='form-control mb-3'),
            Submit('submit', 'Отправить заявку', css_class='btn btn-primary btn-lg')
        )


class ContactForm(forms.ModelForm):
    """Форма обратной связи"""
    
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 6}),
        }
        labels = {
            'name': 'Ваше имя',
            'email': 'Email',
            'subject': 'Тема',
            'message': 'Сообщение',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-6 mb-3'),
                Column('email', css_class='form-group col-md-6 mb-3'),
            ),
            Field('subject', css_class='form-control mb-3'),
            Field('message', css_class='form-control mb-3'),
            Submit('submit', 'Отправить сообщение', css_class='btn btn-primary btn-lg')
        )


class BookOrderForm(forms.ModelForm):
    """Форма заказа книги"""
    
    class Meta:
        model = BookOrder
        fields = ['book', 'full_name', 'email', 'phone', 'address', 'quantity', 'message']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
            'message': forms.Textarea(attrs={'rows': 3}),
            'quantity': forms.NumberInput(attrs={'min': 1, 'value': 1}),
        }
        labels = {
            'book': 'Книга',
            'full_name': 'Ваше имя',
            'email': 'Email',
            'phone': 'Телефон',
            'address': 'Адрес доставки',
            'quantity': 'Количество',
            'message': 'Дополнительные пожелания (необязательно)',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('book', css_class='form-select mb-3'),
            Row(
                Column('full_name', css_class='form-group col-md-6 mb-3'),
                Column('email', css_class='form-group col-md-6 mb-3'),
            ),
            Row(
                Column('phone', css_class='form-group col-md-6 mb-3'),
                Column('quantity', css_class='form-group col-md-6 mb-3'),
            ),
            Field('address', css_class='form-control mb-3'),
            Field('message', css_class='form-control mb-3'),
            Submit('submit', 'Оформить заказ', css_class='btn btn-primary btn-lg')
        )

