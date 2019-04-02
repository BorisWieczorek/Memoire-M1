from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import numpy as np

doc = """
Jeu de bien public 3
"""


class Constants(BaseConstants):
    name_in_url = 'public_goods_3'
    players_per_group = None
    num_rounds = 1
    players = 4

    instructions_template = 'public_goods_3/instructions.html'
    interface_contribute_template = 'public_goods_3/interface_contribute.html'

    # """Amount allocated to each player"""
    endowment = c(50) #ball per player
    multiplier_A = -0.04 #for private
    multiplier_B = -0.06 #for collective
    initial = 5 #allocation de départ
    color1 = "yellow"
    color2 = "blue"


class Subsession(BaseSubsession):

    def creating_session(self):
        self.session.vars['Color1'] = Constants.color1
        self.session.vars['Total_contribution1'] = 0
        self.session.vars['UrnB1'] = 0
        self.session.vars['Initial1'] = Constants.initial
        self.session.vars['Player'] = Constants.players
        for p in self.get_players():
            p.participant.vars['Contribution1'] = 0
            p.participant.vars['UrnA1'] = 0
            p.participant.vars['Total1'] = 0


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
        self.urnB = (self.total_contribution * Constants.multiplier_B) / Constants.players
        self.session.vars['Total_contribution1'] = self.total_contribution
        self.session.vars['UrnB1'] = self.urnB
        for p in self.get_players():
            p.payoff = Constants.initial + p.urnA + self.urnB
            p.participant.vars['Contribution1'] = p.contribution
            p.participant.vars['UrnA1'] = p.urnA
            p.participant.vars['Total1'] = p.payoff




class Player(BasePlayer):
    contribution = models.IntegerField(
       min=0, max=Constants.endowment,
        doc="""The amount contributed by the player""",
    )
    urnA = models.CurrencyField(
    )
