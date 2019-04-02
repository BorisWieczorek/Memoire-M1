from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class QuestionnairePage(Page):
    form_model = 'player'
    form_fields = [
        'gender',
        'highest_level',
        'age',
        'risk_willingness',
        #'steal_a_million',
        #'never_accept_a_bribe',
        #'tempted_counterfeit_money',
        #'money_not_important',
        #'pleasure_from_luxury_goods',
        #'no_use_flattery',
        #'laugh_worst_jokes',
        #'no_pretend_like',
        #  'v100machines',
        #  'ball_cost',
        #  'lilypads',
        #'charitable_organisations',
        #'unicef',
        #'doctors_without_borders',
        #'wwf',
        'mturk_worker_id',
        'comments',
    ]


class MerciPage(Page):
    def vars_for_template(self):
        return{
            'total_earnings': self.player.participant.payoff_plus_participation_fee(),
        }


page_sequence = [
    QuestionnairePage,
#    MerciPage,
]

