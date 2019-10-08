from django.test import TestCase
from .models import Editor, Article, tags

# Editor test
class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.Carine= Editor(first_name = 'Carine', last_name ='I. SEMWAGA', email ='semwagacarine@gmail.com')

# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Carine,Editor))

# Testing Save Method
    def test_save_method(self):
        self.Carine.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)