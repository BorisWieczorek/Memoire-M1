# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class SurveyPage(Page):
    form_model = models.Player
    form_fields = ['sex', 'sisters_brothers',
                   #'religion', 'religion_practice',
                   'student', 'field_of_studies',
                   'level_of_study', 'couple',
                   'previous_participation',
                   #'boring_task',
                   'risk_aversion']


class MerciPage(Page):
    pass


page_sequence = [
    SurveyPage,
    #MerciPage
]
