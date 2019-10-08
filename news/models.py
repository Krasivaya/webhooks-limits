from django.db import models
from django.core.exceptions import ObjectDoesNotExist

# Editor model
class Editor(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name
    class Meta:
        ordering = ['first_name']

#Tag model
class tags(models.Module):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name