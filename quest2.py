from quest_base import quest_base
import typing
import random as rnd
from utils import *

class quest2(quest_base):

    def __init__(self):
        super().__init__()

    def get_new_quest(self) -> dict:
        scalar1 = rnd.randrange(1000, 90000)
        scalar2 = rnd.randrange(1000, 90000)
        questdata = {
            'Hint': 'Svaret er summen af de to tal.',
            'inputData': [scalar1, scalar2]
        }
        return questdata

    def check_answer(self, input: dict, output: dict) -> bool:
        indata = input['inputData']
        result = indata[0]  + indata[1]
        answer = safe_cast(output['outputData'], int,-1)
        return result == answer

    def get_description(self) -> str:
        return r'''
<h2 class="center brown-text"><i class="material-icons">Opgave 2</i></h2>
<h5 class="center">Læs input og læg to tal sammen</h5>

<p class="flow-text light">
  I denne opgave skal du lave et program, der læser to værdier fra en liste og lægger dem sammen (adderer).
  Ligesom i <a href="/?quest=1">opgave 1</a> skal du sende en data pakke, hvor serveren bliver spurgt om input-data.
  I svaret fra serveren skal du læse de to tal fra en liste.
  I Python laver man lister ved hjælp af firkant parenteser og man benytter også firkant parenteser når man skal læse et element fra listen.
  (bemærk: Det første element i en liste er index 0). Se eksemplet nedenfor:
</p>
<p class="codeblock flow-text">thisIsAList = [35, 12, 'Ged']
print(thisIsAList[0]) # Printer tallet 35 (første element)
print(thisIsAList[2]) # Printer strengen 'Ged'
</p>

<p class="flow-text light">
  Prøv at sende nedenstående pakke til webserveren.
</p>
<p class="codeblock flow-text">questGet =
    {
        'cmd'     : 'get',
        'questNo' : 2,
        'user'    : 'Super koder',
    }</p>

<p class="codeblock flow-text">r = requests.post('http://webquest.local', data=questGet)</p>
<p class="flow-text light">
  Prøv at læse JSON pakken som du modtager fra servern, ligesom du gjorde i <a href="/?quest=1">opgave 1</a>. (hint: feltet 'inputData' i dictionary'et indeholder en liste med to tal)
</p>

<p class="flow-text light">
  Når du har fundet tallene i listen, skal du addere dem og sende svaret tilbage til serveren. Svaret skal pakkes i et 'dictionary' som vist nedenfor (udskift '%UniqueID' med det ID du modtog fra serveren og %Answer med den værdi du har regnet ud).
</p>
<p class="codeblock flow-text">questAnswer =
    {
        'cmd'        : 'answer',
        'ID'         : %UniqueID # Det samme ID som vi modtog fra serveren.
        'outputData' : %Answer # Vi sender summen af de to tal vi modtog fra serveren.
    }
</p>
<p class="flow-text light">
  Send pakken til serveren og se om du har svaret rigtig.
</p>
'''