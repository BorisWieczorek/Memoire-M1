from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        yield (pages.QuestionnairePage,
               {
                   'gender': "Female",
                   'highest_level': "Less than high school degree",
                   'age': 25,
                   'risk_willingness': 5,
                   'steal_a_million': Constants.c_agreement_levels[0],
                   'never_accept_a_bribe': Constants.c_agreement_levels[0],
                   'tempted_counterfeit_money': Constants.c_agreement_levels[0],
                   'money_not_important': Constants.c_agreement_levels[0],
                   'pleasure_from_luxury_goods': Constants.c_agreement_levels[0],
                   'no_use_flattery': Constants.c_agreement_levels[0],
                   'laugh_worst_jokes': Constants.c_agreement_levels[0],
                   'no_pretend_like': Constants.c_agreement_levels[0],
                   #  'v100machines',
                   #  'ball_cost',
                   #  'lilypads',
                   'charitable_organisations': 5,
                   'unicef': 5,
                   'doctors_without_borders': 5,
                   'wwf': 5,
                   'mturk_worker_id': 5,
                   'comments': "",
               })
        yield (pages.MerciPage)



