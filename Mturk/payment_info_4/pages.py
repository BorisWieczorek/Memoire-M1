from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants


class Results(Page):
    """Players payoff: How much each has earned"""
    def vars_for_template(self):
        # Set payoffs
        self.player.random_payoffs()
        # Display
        participant = self.participant
        session = self.session
        player = self.player
        return {
            'Color1': session.vars['Color1'],

            'Contribution1': participant.vars['Contribution1'],
            'Total_contribution1': session.vars['Total_contribution1'],
            'UrnB1': -1*session.vars['UrnB1'],
            'UrnA1': -1*participant.vars['UrnA1'],
            'Initial1': session.vars['Initial1'],
            'Total1': participant.vars['Total1'],
            'Autre_contribution1': session.vars['Total_contribution1'] - participant.vars['Contribution1'],

            'Contribution2' : participant.vars['Contribution2'],
            'Total_contribution2' : session.vars['Total_contribution2'],
            'UrnB2' : -1*session.vars['UrnB2'],
            'UrnA2' : -1*participant.vars['UrnA2'],
            'Initial2' : session.vars['Initial2'],
            'Total2' : participant.vars['Total2'],
            'Autre_contribution2' : session.vars['Total_contribution2'] - participant.vars['Contribution2'],

            'Proba_1' : participant.vars['proba_1'],
            'Proba_2' : participant.vars['proba_2'],
            'Choix_player_ligne' : participant.vars['choix_player_ligne'],
            'Realisation_Holt_Laury' : participant.vars['realisation_Holt_Laury'][0],

        }



class PaymentInfo(Page):

    def vars_for_template(self):
        participant = self.participant
        return {
            'redemption_code': participant.label or participant.code,
        }


page_sequence = [#Results,
                 PaymentInfo]
