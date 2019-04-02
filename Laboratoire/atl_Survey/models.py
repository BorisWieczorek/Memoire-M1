# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division

import random

import otree.models
from otree.db import models
from otree import widgets
from otree.common import Currency as c, currency_range, safe_json
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer
# </standard imports>

from django import forms

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'atl_Survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    sex = models.IntegerField(initial=None,
                              choices=[(1, 'Femme'), (0, 'Homme')],
                              verbose_name='Sexe',
                              widget=widgets.RadioSelect())
    sisters_brothers = models.IntegerField(initial=None,
                                           choices=[(1, 'Oui'), (0, 'Non')],
                                           verbose_name='Avez-vous des frères et soeurs',
                                           widget=widgets.RadioSelect())
    religion = models.IntegerField(initial=None,
                                   choices=[(0, 'Catholique'),
                                            (1, 'Juive'),
                                            (2, 'Musulmane'),
                                            (3, 'Protestante'),
                                            (4, 'Autres religions'),
                                            (5, 'Aucune')],
                                   verbose_name='Religion',
                                   widget=widgets.RadioSelect())
    religion_practice = models.IntegerField(initial='0',
                                            verbose_name='Pratiquez-vous régulièrement votre religion ? (de 0: Jamais,'
                                                         'à 5: Toujours)',
                                            widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '5'}))
    student = models.IntegerField(initial=None,
                                  choices=[(1, 'Oui'), (0, 'Non')],
                                  verbose_name='Etes-vous étudiant(e) ?',
                                  widget=widgets.RadioSelect())
    field_of_studies = models.IntegerField(initial=None,
                                           choices=[(0, 'Economie-Gestion'),
                                                    (1, 'Droit'),
                                                    (2, 'Sciences politiques'),
                                                    (3, 'Psychologie'),
                                                    (4, 'Autres sciences sociales'),
                                                    (5, 'Mathématiques'),
                                                    (6, 'Sciences'),
                                                    (7, 'Autres')],
                                           verbose_name='Discipline étudiée (actuellement ou lorsque vous étiez étudiant) ?',
                                           widget=widgets.RadioSelect())
    level_of_study = models.IntegerField(initial=None,
                                         choices=[(0, 'Licence'),
                                                  (1, 'Master'),
                                                  (2, 'Doctorat'),
                                                  (3, 'Autres')],
                                         verbose_name="Niveau d'études",
                                         widget=widgets.RadioSelect())
    couple = models.IntegerField(initial=None,
                                 choices=[(1, 'Oui'), (0, 'Non')],
                                 verbose_name='Etes-vous en couple ?',
                                 widget=widgets.RadioSelect())
    previous_participation = models.IntegerField(initial=None,
                                                 choices=[(1, 'Oui'), (0, 'Non')],
                                                 verbose_name='Avez-vous déjà participé à une expérience en laboratoire ?',
                                                 widget=widgets.RadioSelect())
    boring_task = models.IntegerField(initial=None,
                                      choices=[(0, 'Très ennuyeuses'),
                                               (1, 'Plutot ennuyeuses'),
                                               (2, 'Peu ennuyeuses'),
                                               (3, 'Pas du tout ennuyeuses')],
                                      verbose_name="Selon vous, les tâches que vous avez accomplies au début de "
                                                   "l'expérience (le curseur qui devait être placé au milieu d'un trait) "
                                                   "étaient ?",
                                      widget=widgets.RadioSelect())
    risk_aversion = models.IntegerField(initial='0',
                                        choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                        widget=widgets.RadioSelectHorizontal())
