import typing
import importlib
import os.path as osp
from quest1 import quest1
from quest2 import quest2
from quest3 import quest3

def my_dir() -> str:
    return osp.dirname(osp.realpath(__file__))

class quest_manager(object):
    def __init__(self):
        pass

    def get_quest(self, questNo: int) -> object:
        questName = f'quest{questNo}'
        try:
            importlib.import_module(questName)
            return eval(f'{questName}()')
        except:
            return None

if __name__ == "__main__":
    questApp = quest_manager()
    quest = questApp.get_quest(1)
    print(quest.get_html_template())
    print(quest.get_description())
