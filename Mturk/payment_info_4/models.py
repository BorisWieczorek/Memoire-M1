from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import numpy as np


doc = """
This application provides a webpage instructing participants how to get paid.
Examples are given for the lab and Amazon Mechanical Turk (AMT).
"""

class Constants(BaseConstants):
    name_in_url = 'payment_info_4'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            p.alea = np.random.choice([1, 2, 3], replace=True, p=[1/3, 1/3, 1/3])


class Group(BaseGroup):
    pass

class Player(BasePlayer):
    gain = models.CurrencyField()
    alea = models.IntegerField()
    total_gain = models.CurrencyField()

    def random_payoffs(self):
        if self.alea == 1:
            self.gain = self.participant.vars['Total2']
        elif self.alea == 2 :
            self.gain = self.participant.vars['Total1']
        else :
            self.gain = self.participant.vars['realisation_Holt_Laury'][0]



