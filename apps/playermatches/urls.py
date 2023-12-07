from django.urls import path
from . import views

app_name = 'playermatches'

urlpatterns = [
    path('', views.list_playermatches, name='list_playermatches'),
    path('adicionar/<int:id_client>/', views.add_playermatch, name='add_playermatch'),
    path('excluir/<int:id_playermatch>/', views.delete_playermatch, name='delete_playermatch'),
    path('excluir-item/<int:id_playermatch_item>/', views.delete_playermatch_item, name='delete_playermatch_item'),
    path('adicionar-item/<int:id_playermatch>/', views.add_playermatch_item, name='add_playermatch_item'),
    path('editar-status/<int:id_playermatch>/', views.edit_playermatch_status, name='edit_playermatch_status'),
]