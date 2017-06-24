# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from demo.models import Question

class Home(ListView):
    model = Question
    

class QuestionDetail(DetailView):
    model = Question


