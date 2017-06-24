# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from demo.models import Question

class QuestionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Question, QuestionAdmin)
