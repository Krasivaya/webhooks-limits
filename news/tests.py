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


# Articles test
class ArticleTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.Carine= Editor(first_name = 'Carine', last_name ='I. SEMWAGA', email ='semwagacarine@gmail.com')
        self.Carine.save_editor()

        # Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_article= Article(title = 'Test Article',post = 'This is a random test Post',editor = self.Carine)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()