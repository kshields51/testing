''' 
I think I like the idea of Test Driven Development (TDD) because of the steps:
                1. Make the method/function with pass as its only line of execution
                2. Make the test (hint hint thats what this file is).
                3. Since the second argument represents a completed test you can
                    place that argument where pass is in the actual method
                    and you will have done TDD. Becuase the philosophy of make the
                    test pass and slowly build up the complexity holds true.    
'''
from unittest import TestCase
from blog import Blog

class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test', 'Test Author')

        self.assertEqual('Test', b.title)
        self.assertEqual('Test Author', b.author)
        self.assertListEqual([], b.posts)

    def test_repr(self):
        b = Blog('Test', 'Test Author')
        b2 = Blog('My Day', 'Rolf')

        self.assertEqual(b.__repr__(), 'Test by Test Author (0 posts)')
        self.assertEqual(b2.__repr__(), 'My Day by Rolf (0 posts)')

    def test_repr_multiple_posts(self):
        b = Blog('Test', 'Test Author' )
        b.posts = ['test']

        self.assertEqual(b.__repr__(), 'Test by Test Author (1 post)')
        
        