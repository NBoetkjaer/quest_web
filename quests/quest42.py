import random as rnd
from quests.quest_base import (quest_base)

class quest(quest_base):
  def __init__(self):
      super().__init__()

  def get_new_quest(self) -> dict:
    questdata = {
      'hint': 'Det ser ud til at du allerede kender svaret - Men hvad er spørgsmålet?',
      'inputData': "Forty-two"
    }
    return questdata

  def check_answer(self, input: dict, output: dict) -> bool:
    text = str(output['outputData']).lower()
    ok =  'ultimate' in text
    ok = ok and 'question' in text
    ok = ok and 'life, the universe, and everything' in text
    return ok

  def get_description(self) -> str:
    return r'''
<h2 class="center brown-text"><i> Forty-two</i> </h2>
<h5 class="center">The Hitchhiker's Guide to the Galaxy</h5>
'''