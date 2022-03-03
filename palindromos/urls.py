from django.urls import path
from .views import show_palindromos, create_palindromos, delete_palindromos

urlpatterns = [
    path('', show_palindromos, name='show_palindromos'),
    path('new', create_palindromos, name='create_palindromos'),
    path('delete/<int:id>', delete_palindromos, name='delete_palindromos')
]