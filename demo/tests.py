# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, Client
from demo.models import Question
from django.core.urlresolvers import reverse


QUESTION = 'In RichTextField I will add math jax code like'
ANSWER = 'Then the Front end Site should show the code as.'
EXPLANATION = '\left(\sqrt{7}-\dfrac{1}{\sqrt{7}}\right)^2'

### test models
class TestQestion(TestCase):
    
    
    
    
    def setUp(self):
        super(TestQestion, self).setUp()
        
    
    def test_01_question(self):
        
        q  = Question.objects.create(
            question=QUESTION,
            answer=ANSWER,
            explanation=EXPLANATION
            )
        
        
        
        self.assertIsInstance(q, Question, "correct Question object")
        self.assertEqual(q.question, QUESTION, "Correct QUESTION")
        self.assertEqual(q.answer, ANSWER, "Correct ANSWER")
        self.assertEqual(q.explanation, EXPLANATION, "Correct EXPLANATION")
        
        
       

### test views

class TestViewHome(TestCase):
    
    def setUp(self):
        super(TestViewHome, self).setUp()
        
        



    def test_01_view(self):
        client = Client()
        
        response = client.get(reverse('demo:home'))
        self.assertEqual(response.status_code, 200)
        
        
        q  = Question.objects.create(
            question=QUESTION,
            answer=ANSWER,
            explanation=EXPLANATION
            )
        
        response = self.client.get(reverse('demo:questiondetail', {'pk': q.id}))
        self.assertEqual(response.status_code, 200)
        
        