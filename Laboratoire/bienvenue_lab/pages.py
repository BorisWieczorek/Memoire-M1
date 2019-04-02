from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants


class Bienvenue(Page):
    pass

class Bienvenue_anthropo(Page):
    pass

class Introduction(Page):
    """Description of the game: How to play and returns expected"""
    pass

class Part_1(Page):
    pass

class Attente(Page):
    pass

class Prediction(Page):
    form_model = 'player'
    form_fields = ['prediction']

    def before_next_page(self):
        self.group.set_payoffs()

class Contribute(Page):
    """Player: Choose how much to contribute"""
    pass


class ResultsWaitPage(WaitPage):
    pass



class Results(Page):
    """Players payoff: How much each has earned"""
    pass



page_sequence = [
    Bienvenue_anthropo,
    #Bienvenue,
    #Part_1,
    Attente,
    Prediction,
]
