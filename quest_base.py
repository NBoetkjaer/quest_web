import typing
from  utils import (getCallout, getPositiveFeedback, getNegatigveFeedback)

class quest_base(object):

    def __init__(self):
        pass

    def get_html_template(self)-> str:
        return "quest.html"

    def get_evaluation_message(self, input: dict, output: dict)->str:
        retVal = self.check_answer(input, output)
        user = input['user']
        if retVal:
            return { 'result': f'{getCallout()} {user} - {getPositiveFeedback()}'}
        else:
            return { 'result': f'{getCallout()} {user} - {getNegatigveFeedback()}'}

    def get_new_quest(self) -> dict:
        raise NotImplementedError()

    def check_answer(self, input: dict, output: dict) -> bool:
        raise NotImplementedError()
    
    def get_description(self) -> str:
        raise NotImplementedError()

