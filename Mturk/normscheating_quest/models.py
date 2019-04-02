from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range )
from django.utils.safestring import mark_safe


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'Tquest'
    players_per_group = None
    num_rounds = 1

    c_agreement_levels = ["Strongly agree", "Somewhat agree", "Somewhat disagree", "Strongly disagree"]

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    #############################################
    gender = models.StringField(
        label="What is your gender?",
        choices=["Female", "Male", "Other"],
        widget=widgets.RadioSelect(),
    )
    #############################################
    highest_level = models.StringField(
        label="What is the highest level of school you have completed or the highest degree you have received?",
        choices=[
            "Less than high school degree",
            "High school graduate (high school diploma or equivalent including GED)",
            "Some college but no degree",
            "Associate degree in college (2-year)",
            "Bachelor's degree in college (4-year)",
            "Master's degree",
            "Doctoral degree",
            "Professional degree (JD, MD)"
        ],
        widget=widgets.RadioSelect(),
    )
    age = models.PositiveIntegerField(
        label="How old are you in years?"
    )
    risk_willingness = models.PositiveIntegerField(
        label="Please indicate on the scale if, in general, you are a person who is fully prepared to take "
                     "risks or who tries to avoid taking risks?",
        choices=range(1, 11, 1),
        widget=widgets.RadioSelectHorizontal(),
    )
    #############################################
    #steal_a_million = models.StringField(
    #    label="If I knew that I could never get caught, I would be willing to steal a million dollars.",
    #    choices=Constants.c_agreement_levels,
    #)
    #never_accept_a_bribe = models.StringField(
    #    label="I would never accept a bribe, even if it were very large.",
    #    choices=Constants.c_agreement_levels,
    #)
    #tempted_counterfeit_money = models.StringField(
    #    label="I’d be tempted to use counterfeit money, if I were sure I could get away with it.",
    #    choices=Constants.c_agreement_levels,
    #)
    #money_not_important = models.StringField(
    #    label="Having a lot of money is not especially important to me.",
    #    choices=Constants.c_agreement_levels,
    #)
    #pleasure_from_luxury_goods = models.StringField(
    #    label="I would get a lot of pleasure from owning expensive luxury goods.",
    #    choices=Constants.c_agreement_levels,
    #)
    #no_use_flattery = models.StringField(
    #    label="I wouldn't use flattery to get a raise or promotion at work, even if I thought it would succeed.",
    #    choices=Constants.c_agreement_levels,
    #)
    #laugh_worst_jokes = models.StringField(
    #    label="If I want something from someone, I will laugh at that person's worst jokes.",
    #    choices=Constants.c_agreement_levels,
    #)
    #no_pretend_like = models.StringField(
    #    label="I wouldn’t pretend to like someone just to get that person to do favors for me.",
    #    choices=Constants.c_agreement_levels,
    #)
    #############################################
    #  v100machines = models.StringField(
    #      label="If it takes 5 machines 5 minutes to make 5 widgets, how long would it take 100 machines to make "
    #                   "100 widgets?",
    #      choices=["1 minute", "5 minutes", "100 minutes", "10 minutes"],
    #      widget=widgets.RadioSelect(),
    #  )
    #  ball_cost = models.StringField(
    #      label="A bat and a ball cost $1.10 in total. The bat costs $1.00 more than the ball. How much does the "
    #                   "ball cost?",
    #      choices=["$0.05", "$1.00", "$0.10", "$2.10"],
    #      widget=widgets.RadioSelect(),
    #  )
    #  lilypads = models.StringField(
    #      label="In a lake, there is a patch of lily pads. Every day, the patch doubles in size. "
    #                   "If it takes 48 days for the patch to cover the entire lake, how long would it take for "
    #                   "the patch to cover half the lake?",
    #      choices=["40 days", "24 days", "47 days", "49 days"],
    #      widget=widgets.RadioSelect(),
    #  )
    #charitable_organisations = models.PositiveIntegerField(
    #    label="What is your general opinion of charitable organizations?"
    #                 "1: I do not support the work of charitable organizations."
    #                 "10: I fully support the work of charitable organizations.",
    #    choices=range(1, 11, 1),
    #    widget=widgets.RadioSelectHorizontal(),
    #)
    #unicef = models.PositiveIntegerField(
    #    label=mark_safe("What is your general opinion of the United Nations International Children's Emergency "
    #                    "Fund (UNICEF)?\n"
    #                    "1: I do not support the work of UNICEF.\n"
    #                    "10: I fully support the work of UNICEF."),
    #    choices=range(1, 11, 1),
    #    widget=widgets.RadioSelectHorizontal(),
    #)
    #doctors_without_borders = models.PositiveIntegerField(
    #    label="What is your general opinion of the Doctors Without Borders organization?\n"
    #          "1: I do not support the work of Doctors Without Borders.\n"
    #          "10: I fully support the work of Doctors Without Borders.",
    #    choices=range(1, 11, 1),
    #    widget=widgets.RadioSelectHorizontal(),
    #)
    #wwf = models.PositiveIntegerField(
    #""    label="What is your general opinion of the World Wildlife Fund (WWF)?\n"
    #          "1: I do not support the work of the WWF.\n"
    #          "10: I fully support the work of the WWF.",
    #    choices=range(1, 11, 1),
    #    widget=widgets.RadioSelectHorizontal(),
    #)
    mturk_worker_id = models.StringField(
        label="So that individual payments can be made, please enter your Amazon Mechanical Turk Worker ID."
              "(This number can be found on your worker Dashboard.)\n"
              "Type carefully. If your Worker ID is entered incorrectly, additional earnings may not be "
              "received. \n"
              "Worker ID:",
    )
    comments = models.LongStringField(
        label="Optional: If you have any comments, please feel free to write them here. Thank you!",
        blank=True,
    )
