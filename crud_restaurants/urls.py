from django.urls import path, include
from .views import *

urlpatterns = [
    path('add/', add_form, name='add_form'),
    path('delete/', delete_form, name='delete_form'),
    path('restaurants/', restaurants_index, name='all_restaurants'),
    path('restaurants/edit', edit_index, name='edit_form'),
    path('update/', update_form, name='update_form'),
    path('about/', about_page, name='about'),
    path('', landing_page, name='home'),
]