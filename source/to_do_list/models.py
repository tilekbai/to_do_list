from django.db import models
status_choice = [("new", "Новая"), ("in_progress", "В процессе"), ("done", "Сделано")]

# Create your models here.

class Problem(models.Model):
    description = models.TextField(max_length=3000, null=False, blank=False)
    detailed_description = models.TextField(max_length=7000, null=True, blank=True)
    status = models.CharField(max_length=30, choices=status_choice, null=False, default="new")
    dead_line = models.DateField(blank=False)

    class Meta:
        db_table = "problems"
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"


    def __str__(self):
        return f'{self.id}. {self.description}. {self.detailed_description}. {self.status}: {self.dead_line}'
