from django.test import TestCase
from .models import Editor, Article, tags

# Editor test
class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.Carine= Editor(first_name = 'Carine', last_name ='I. SEMWAGA', email ='semwagacarine@gmail.com')
