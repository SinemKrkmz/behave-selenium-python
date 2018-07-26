from features.steps.browser import Browser
from features.steps.actionwords import Actionwords
import os, json
import datetime

#

def before_all(context):
    pass


def before_feature(context, feature):
    context.actionwords = Actionwords()


def before_scenario(context, scenario):
    context.actionwords = Actionwords()



def after_scenario(context, scenario):
    context.actionwords.browser = Browser()


def after_feature(context, feature):
    pass


def after_all(context):
    pass
