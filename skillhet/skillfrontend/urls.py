from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about-us', views.about_us, name='about_us'),
    path('contact-us', views.contact, name='contact'),
    path('details/<int:cat_id>', views.details, name='details'),
    path('enquery_form_submit', views.enquery_form_submit, name='enquery_form_submit'), 
]