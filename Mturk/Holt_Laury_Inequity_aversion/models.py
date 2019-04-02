from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import numpy as np

doc = """
Ce document contient l'aversion au risque ainsi que l'aversion à l'inequité
"""

class Constants(BaseConstants):
    name_in_url = 'Holt_Laury_Inequity_aversion'
    players_per_group = None
    num_rounds = 1
    max_proba = 110
    proba_increment = 10
    proba_choices = list(range(10, max_proba, proba_increment))


class Subsession(BaseSubsession):

    def creating_session(self):
        for p in self.get_players():
            p.participant.vars['Total_contribution2'] = 0
            p.participant.vars['proba_1'] = 0
            p.participant.vars['proba_2'] = 0
            p.participant.vars['choix_player_ligne'] = 0
            p.participant.vars['realisation_Holt_Laury'] = 0

    def before_session_starts(self):
        players = self.get_players()
        random.shuffle(players)
        groupe_avec_1 = [players.pop(),]
        group_matrix = [groupe_avec_1]
        while players:
            new_group = [
                players.pop(),

            ]
            group_matrix.append(new_group)
        self.set_group_matrix(group_matrix)


class Group(BaseGroup):

    def calculate_payoff_InequityAversion(self):

        players = self.get_players()
        for p in players:
            if len(players) == 3:
                p.groupe_3_InequityAversion = 1
                if p.id_in_group == 1:
                    autres = [2, 3]
                    partner = self.get_player_by_id(random.choice(autres))
                else:
                    partner = self.get_player_by_id(1)
            else:
                p.groupe_3_InequityAversion = 0
                if p.id_in_group == 1:
                    partner = self.get_player_by_id(2)
                elif p.id_in_group == 2:
                    partner = self.get_player_by_id(3)
                elif p.id_in_group == 3:
                    partner = self.get_player_by_id(4)
                elif p.id_in_group == 4:
                    partner = self.get_player_by_id(1)
            print('voilà mon partenaire: ', partner)
            partner_line_Inequity = partner.random_choice_line_InequityAversion
            partner_choice_Inequity = partner.response_choisi_InequityAversion
            if partner_choice_Inequity == "option A":
                p.payoff_Inequity += 3
            else:
                p.payoff_Inequity += partner_line_Inequity


class Player(BasePlayer):

    groupe_3_InequityAversion = models.IntegerField()
    response_choisi_InequityAversion = models.CharField()
    payoff_Inequity =  models.IntegerField(initial=0)
    random_choice_line_InequityAversion = models.IntegerField()
    response_choisi = models.CharField()
    choix_Holt_laury = models.CharField()
    ligne_Holt_Laury = models.IntegerField()
    realisation_gain_Holt_Laury = models.FloatField()
    # the choices between loteries Holt & Laury (2002)
    response_10 = models.CharField(choices=['option A', 'option B'],
                                   widget=widgets.RadioSelectHorizontal(),
                                   verbose_name='')
    response_20 = models.CharField(choices=['option A', 'option B'],
                                   widget=widgets.RadioSelectHorizontal(),
                                   verbose_name='')
    response_30 = models.CharField(choices=['option A', 'option B'],
                                   widget=widgets.RadioSelectHorizontal(),
                                   verbose_name='')
    response_40 = models.CharField(choices=['option A', 'option B'],
                                   widget=widgets.RadioSelectHorizontal(),
                                   verbose_name='')
    response_50 = models.CharField(choices=['option A', 'option B'],
                                   widget=widgets.RadioSelectHorizontal(),
                                   verbose_name='')
    response_60 = models.CharField(choices=['option A', 'option B'],
                                   widget=widgets.RadioSelectHorizontal(),
                                   verbose_name='')
    response_70 = models.CharField(choices=['option A', 'option B'],
                                   widget=widgets.RadioSelectHorizontal(),
                                   verbose_name='')
    response_80 = models.CharField(choices=['option A', 'option B'],
                                   widget=widgets.RadioSelectHorizontal(),
                                   verbose_name='')
    response_90 = models.CharField(choices=['option A', 'option B'],
                                   widget=widgets.RadioSelectHorizontal(),
                                   verbose_name='')
    response_100 = models.CharField(choices=['option A', 'option B'],
                                    widget=widgets.RadioSelectHorizontal(),
                                    verbose_name='')


    #the choices for inequity aversion:
    response_Inequity_0 = models.CharField(choices=['option A', 'option B'],
                                   widget=widgets.RadioSelectHorizontal(),
                                   verbose_name='')
    response_Inequity_1 = models.CharField(choices=['option A', 'option B'],
                                   widget=widgets.RadioSelectHorizontal(),
                                   verbose_name='')
    response_Inequity_2 = models.CharField(choices=['option A', 'option B'],
                                   widget=widgets.RadioSelectHorizontal(),
                                   verbose_name='')
    response_Inequity_3 = models.CharField(choices=['option A', 'option B'],
                                   widget=widgets.RadioSelectHorizontal(),
                                   verbose_name='')
    response_Inequity_4 = models.CharField(choices=['option A', 'option B'],
                                   widget=widgets.RadioSelectHorizontal(),
                                   verbose_name='')
    response_Inequity_5 = models.CharField(choices=['option A', 'option B'],
                                   widget=widgets.RadioSelectHorizontal(),
                                   verbose_name='')
    response_Inequity_6 = models.CharField(choices=['option A', 'option B'],
                                   widget=widgets.RadioSelectHorizontal(),
                                   verbose_name='')
    response_Inequity_7 = models.CharField(choices=['option A', 'option B'],
                                   widget=widgets.RadioSelectHorizontal(),
                                   verbose_name='')
    response_Inequity_8 = models.CharField(choices=['option A', 'option B'],
                                   widget=widgets.RadioSelectHorizontal(),
                                   verbose_name='')
    response_Inequity_9 = models.CharField(choices=['option A', 'option B'],
                                   widget=widgets.RadioSelectHorizontal(),
                                   verbose_name='')
    response_Inequity_10 = models.CharField(choices=['option A', 'option B'],
                                    widget=widgets.RadioSelectHorizontal(),
                                    verbose_name='')

    def calculate_payoff_Holt_Laury(self):
        self.ligne_Holt_Laury = random.choice(Constants.proba_choices)
        self.response_choisi = 'response_{}'.format(self.ligne_Holt_Laury)
        self.choix_Holt_laury = getattr(self, 'response_{}'.format(self.ligne_Holt_Laury))
        if self.choix_Holt_laury == 'option A':
            self.realisation_gain_Holt_Laury = \
                np.random.choice(
                [2.0, 1.60], 1,
                p=[(self.ligne_Holt_Laury/100), 1-(self.ligne_Holt_Laury/100)]
            )
        else:
            self.realisation_gain_Holt_Laury = \
                np.random.choice(
                [3.85, 0.10], 1,
                p=[(self.ligne_Holt_Laury/100), 1-(self.ligne_Holt_Laury/100)]
            )
        self.participant.vars['proba_1'] = self.ligne_Holt_Laury
        self.participant.vars['proba_2'] = 100 - self.ligne_Holt_Laury
        self.participant.vars['choix_player_ligne'] = self.choix_Holt_laury
        self.participant.vars['realisation_Holt_Laury'] = self.realisation_gain_Holt_Laury

        self.participant.vars['payoff_Holt_Laury'] = float(self.realisation_gain_Holt_Laury)

        #print('le payoff participant ',self.participant.vars['payoff_Holt_Laury'])


    def random_choice_InequityAversion(self):
        self.random_choice_line_InequityAversion = random.choice(list(range(11)))
        self.response_choisi_InequityAversion = getattr(self, 'response_Inequity_{}'.
                                                        format(self.random_choice_line_InequityAversion))
        if self.response_choisi_InequityAversion == "option A":
            self.payoff_Inequity += 3
        else :
            self.payoff_Inequity += 10-self.random_choice_line_InequityAversion
