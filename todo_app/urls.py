from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),  # Page d'accueil : liste des tâches
    path('task/<int:pk>/', views.task_detail, name='task_detail'),  # Détail d'une tâche
    path('task/create/', views.task_create, name='task_create'),  # Créer une tâche
    path('task/<int:pk>/update/', views.task_update, name='task_update'),  # Modifier une tâche
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),  # Supprimer une tâche
    path('task/<int:pk>/toggle/', views.task_toggle, name='task_toggle'),  # Basculer état complétée
]

