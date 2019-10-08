from django.db import models

# Editor model
class Editor(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name
    try:
        editor = Editor.objects.get(email = 'example@gmail.com')
        print('Editor Found')
    except DoesNotExist:
        print('Editor was not found')