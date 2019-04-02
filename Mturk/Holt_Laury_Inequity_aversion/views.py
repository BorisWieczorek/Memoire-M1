from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from . import models

class Bienvenue_anthropo(Page):
    pass

class Bienvenue(Page):
    pass

class Attente(Page):
    pass

class Part_3(Page):
    pass

class RiskAversion(Page):
    form_model = models.Player
    form_fields = ['response_{}'.format(i) for i in
                   range(10,110,10)]
    def before_next_page(self):
        self.player.calculate_payoff_Holt_Laury()
        self.participant.vars['payoff_Inequity_Aversion'] = self.player.payoff_Inequity


class Results(Page):
    def vars_for_template(self):
        return{
            'ligne' : self.player.ligne_Holt_Laury,
            'response_choisi' : self.player.response_choisi,
            'proba_1':self.player.ligne_Holt_Laury,
            'proba_2': (100-self.player.ligne_Holt_Laury),
            'choix_player_ligne': self.player.choix_Holt_laury,
            'realisation_Holt_Laury' : self.player.realisation_gain_Holt_Laury,
        }

class InequityAversion(Page):
    form_model = models.Player
    form_fields = ['response_Inequity_{}'.format(i) for i in
                   range(0,11)]
    def before_next_page(self):
        self.player.random_choice_InequityAversion()

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.calculate_payoff_InequityAversion()
    body_text = "Veuillez attendre svp"

class ShuffleWaitPage(WaitPage):
    wait_for_all_groups = True

    def after_all_players_arrive(self):
        self.subsession.group_randomly()

page_sequence = \
    [
    #Bienvenue_anthropo,
    #Attente,
    #Bienvenue,
    Part_3,
    RiskAversion,
    #Attente,
    #InequityAversion,
    #ResultsWaitPage,
    #Results,
    ]
