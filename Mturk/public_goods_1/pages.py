from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants


class Bienvenue(Page):
    pass

class Introduction(Page):
    """Description of the game: How to play and returns expected"""
    pass


class Contribute(Page):
    """Player: Choose how much to contribute"""

    form_model = 'player'
    form_fields = ['contribution']


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()

    body_text = "Please wait the other participant."



class Results(Page):
    """Players payoff: How much each has earned"""






def before_next_page(self):
    if self.request.POST.get('back'):
        if self.request.POST.get('back')[0] == '1':
            self._is_frozen = False
            self._index_in_pages -= 2
            self.participant._index_in_pages -= 2

page_sequence = [
    #Bienvenue,
    Introduction,
    Contribute,
    #ResultsWaitPage,
    #Results,
]
