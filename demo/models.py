# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ckeditor.fields import RichTextField



class Question(models.Model):
    
    question = models.CharField(max_length=255, unique=True)
    answer = models.CharField(max_length=255)
    explanation = RichTextField()
    
    
    def __str__(self):
        return self.question
    
    