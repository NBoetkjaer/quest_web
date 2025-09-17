import random as rnd
import typing

def safe_cast(val, to_type, default=None):
    try:
        return to_type(val)
    except (ValueError, TypeError):
        return default

callout = [ 'Hey', 'Hi','Halløj', 'Hej', 'Hejsa', 'yo -', 'Ohøj skipper' ]

positive = ['Super flot klaret!!',
            'Du er jo en rigtig super koder',
            'Det var rigtigt - din hacker ;-)',
            '!! 1337 H4CK3R !!',
            'Excellent svaret',
            'Easy peasy! Den klarede du jo let'
            'Wauw - du må være professionel!',
            'Det kan du godt være stolt over',
            '100% - total i orden makker',
            'Top dollar - hvor er du sej!'
            ]

negative = ['Du må vist øve dig lidt mere :-)', 
            'Op på hesten igen.',
            'Måske du skulle prøve at strikke i stedet.',
            'Godt forsøgt - men det er jo forkert.',
            'Din mor ville gøre det bedre :-)',
            'Ikke helt rigtigt - Men du prøver i det mindste.',
            'Har du brækket alle ti fingre!',
            'Du er vist ikke helt vågen endnu.',
            ]
def getCallout()->str:
    return callout[ rnd.randrange(0, len(callout)) ]

def getPositiveFeedback() -> str:
    return positive[ rnd.randrange(0, len(positive)) ]

def getNegatigveFeedback() -> str:
    return negative[ rnd.randrange(0, len(negative)) ]