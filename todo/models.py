from django.db import models

# Create your models here.

class TODO(models.Model):
    case_Choices = [
        ("True","Done"),
        ("False","Undone"),
    ]
    inserted_by = models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Inserted By")
    todo_describe = models.CharField(max_length=150, verbose_name="Todo")
    todo_case = models.CharField(max_length=10, choices=case_Choices, default="False")
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.todo_describe

    