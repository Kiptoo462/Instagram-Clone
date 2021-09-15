from django.test import TestCase

# Create your tests here.

from .models import Profile,Post,Comment,Following

class FollowingTestClass(TestCase):
    def setUp(self):
        self.victor=Following(username='victor',followed='Benard')
                            
    def test_instance(self):
        self.assertTrue(isinstance(self.Victor,Following))

class CommentTestClass(TestCase):
    def setUp(self):
        self.first=Comment(post=1,
                            username='Victor',
                            comment='The Heros',
                            date='September 15, 2021, 23:32 p.m.',
                            count=0)

    def test_instance(self):
        self.assertTrue(isinstance(self.first,Comment))