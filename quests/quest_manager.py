import typing
import importlib
import importlib.util
import os.path as osp 

def my_dir() -> str:
    return osp.dirname(osp.realpath(__file__))

class quest_manager(object):
    def __init__(self):
        pass

    def get_quest(self, questNo: int) -> object:
        questName = f'quest{questNo}'
        try:
            spec = importlib.util.spec_from_file_location(f'. {questName}', f"quests/{questName}.py")
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            print('here')
            return module.quest()
        except Exception as e: 
            print(f'Failed to import: {questName}. Exception: {repr(e)}')
            return None

if __name__ == "__main__":
    questApp = quest_manager()
    quest = questApp.get_quest(1)
    print(quest.get_html_template())
    print(quest.get_description())
