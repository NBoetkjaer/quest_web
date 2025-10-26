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
            spec = importlib.util.spec_from_file_location(questName, f"{questName}.py")
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module.quest()
        except:
            print(f'Failed to import: {questName}')
            return None

if __name__ == "__main__":
    questApp = quest_manager()
    quest = questApp.get_quest(1)
    print(quest.get_html_template())
    print(quest.get_description())
