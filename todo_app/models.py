from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)        # Titre obligatoire
    description = models.TextField(blank=True)      # Description facultative
    due_date = models.DateField(null=True, blank=True)  # Date d’échéance facultative
    due_time = models.TimeField(null=True, blank=True)  # Heure facultative
    completed = models.BooleanField(default=False)     # Statut terminé/incomplet

    created_at = models.DateTimeField(auto_now_add=True)  # Date de création
    updated_at = models.DateTimeField(auto_now=True)      # Date de mise à jour

    def __str__(self):
        return self.title