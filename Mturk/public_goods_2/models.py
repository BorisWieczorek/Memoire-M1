from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random
import numpy as np

doc = """
Jeu de bien public 2
"""


class Constants(BaseConstants):
    name_in_url = 'public_goods_2'
    players_per_group = None
    num_rounds = 1
    players = 4

    instructions_template = 'public_goods_2/instructions.html'
    interface_contribute_template = 'public_goods_2/interface_contribute.html'

    # """Amount allocated to each player"""
    endowment = c(50)
    multiplier_A = 0.02
    gain_B = 2
    initial = 1 #allocation de départ
    red = 200 #number of red balls
    color1 = "yellow"
    color2 = "blue"

class Subsession(BaseSubsession):

    def creating_session(self):
        self.session.vars['Color1'] = Constants.color1
        self.session.vars['Total_contribution2'] = 0
        self.session.vars['UrnB2'] = 0
        self.session.vars['Initial2'] = Constants.initial
        self.session.vars['Player'] = Constants.players
        for p in self.get_players():
            p.participant.vars['Contribution2'] = 0
            p.participant.vars['UrnA2'] = 0
            p.participant.vars['Total2'] = 0


    def vars_for_admin_report(self):
        contributions = [p.contribution for p in self.get_players() if p.contribution != None]
        if contributions:
            return {
                'avg_contribution': sum(contributions)/len(contributions),
                'min_contribution': min(contributions),
                'max_contribution': max(contributions),
            }
        else:
            return {
                'avg_contribution': '(no data)',
                'min_contribution': '(no data)',
                'max_contribution': '(no data)',
            }



class Group(BaseGroup):
    total_contribution = models.CurrencyField()
    individual_share = models.CurrencyField()
    urnB = models.CurrencyField()


    def set_payoffs(self):
        self.total_contribution = sum([p.contribution for p in self.get_players()])
        for p in self.get_players():
            p.urnA = (Constants.endowment - p.contribution)*Constants.multiplier_A
        self.urnB = np.random.choice([0, Constants.gain_B/1], replace=True, p=[(Constants.red - self.total_contribution)/Constants.red, 1 - ((Constants.red - self.total_contribution)/Constants.red)])
        self.session.vars['Total_contribution2'] = self.total_contribution
        self.session.vars['UrnB2'] = self.urnB
        for p in self.get_players():
            p.payoff = Constants.initial + p.urnA + self.urnB
            p.participant.vars['Contribution2'] = p.contribution
            p.participant.vars['UrnA2'] = p.urnA
            p.participant.vars['Total2'] = p.payoff





class Player(BasePlayer):
    contribution = models.IntegerField(
       min=0, max=Constants.endowment,
        doc="""The amount contributed by the player""",
    )
    urnA = models.CurrencyField(
    )
