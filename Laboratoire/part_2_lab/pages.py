from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants


class Part_2(Page):
    def vars_for_template(self):
        participant = self.participant
        session = self.session
        player = self.player
        return {
            'Player': session.vars['Player'],

        }

class Introduction(Page):
    """Description of the game: How to play and returns expected"""
    pass


class Contribute(Page):
    """Player: Choose how much to contribute"""
    pass


class ResultsWaitPage(WaitPage):
    pass



class Results(Page):
    """Players payoff: How much each has earned"""
    pass



page_sequence = [
    Part_2
]
