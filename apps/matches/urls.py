from django.urls import path
from . import views

app_name = 'matches'

urlpatterns = [
    path('', views.list_matches, name='list_matches'),
    path('adicionar/', views.add_match, name='add_match'),
    path('editar/<int:id_match>/', views.edit_match, name='edit_match'),
    path('excluir/<int:id_match>/', views.delete_match, name='delete_match'),
]