from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class List(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    task_name = models.CharField(max_length=50)
    description = models.TextField(max_length=150, blank=True)
    complete = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.task_name

    class Meta:
        order_with_respect_to = 'user'