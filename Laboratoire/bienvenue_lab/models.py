from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

doc = """
Bienvenue
"""


class Constants(BaseConstants):
    name_in_url = 'bienvenue_lab'
    players_per_group = None
    num_rounds = 1



class Subsession(BaseSubsession):

    def creating_session(self):
        for p in self.get_players():
            p.participant.vars['Prediction'] = 0



class Group(BaseGroup):
    def set_payoffs(self):
        for p in self.get_players():
            p.participant.vars['Prediction'] = p.prediction




class Player(BasePlayer):
    prediction = models.IntegerField(
        min=0, max=100,
        doc="""The mean of contribute by the player""",
    )
