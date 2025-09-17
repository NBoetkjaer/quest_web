from quest_base import quest_base
import typing
import random as rnd


class quest1(quest_base):

    Words = [
        'hemmelig',
        'vigtig',
        'underlig',
        'mærkelig',
        'fantastisk',
        'vidunderlig',
        'ekstraordinær',
        'sindsyg',
        'middelmådig',
        'brilliant',
        'skør'
    ]

    def __init__(self):
        super().__init__()

    def get_new_quest(self) -> dict:
        randomWord = quest1.Words[ rnd.randrange(0, len(quest1.Words)) ]
        questdata = {
            'Hint': 'Bare send beskeden retur.',
            'inputData': "Dette er en " + randomWord + " besked fra serveren"
        }
        return questdata

    def check_answer(self, input: dict, output: dict) -> bool:
        return input['inputData'] == output['outputData']

    def get_description(self) -> str:
        return r'''
<h2 class="center brown-text"><i>Opgave 1</i></h2>
<h5 class="center">Introduktion til Python og http requests</h5>

<p class="flow-text light">
  I denne lille opgave skal vi lave et program som henter data fra en webserver og sender det samme data tilbage til webserveren.
  Når vi skal 'snakke' med webserveren benytter vi et Python modul som hedder 'requests'.
</p>

<p class="flow-text light">
  I starten af vores program importere vi 'requests' modulet:
</p>
<p class="codeblock flow-text">import requests </p>

<p class="flow-text light">
  Nu kan vi lave et Python 'dictonary' som indeholder det data vi skal sende. Et 'dictionary' er en meget fleksibel datastruktur, der samler navne og værdier. Når man skal oprette et 'dictionary' i Python benytter man krøllede parenteser: { 'navn_1': værdi }
  Nedenfor opretter vi et 'dictionary' med variabel navnet 'questGet', som indeholder tre felter 'cmd', 'user' og 'questNo'.
</p>
<p class="codeblock flow-text">questGet =
    {
        'cmd'     : 'get',
        'questNo' : 1,
        'user'    : 'Super koder',
    }</p>

<p class="flow-text light">
  Endelig kan vi sende vores dictionary afsted til serveren.
</p>
<p class="codeblock flow-text">r = requests.post('http://webquest.local', json=questGet)</p>
<p class="flow-text light">
  Svaret fra servern bliver modtaget i variablen 'r' og er pakket i et format der hedder JSON. Du kan eventuelt prøve at printe svaret til konsollen med funktionen 'print(r.text)'.
  Vi kan omdanne JSON pakken i 'r' til et 'dictionary' ved at bruge methoden '.json()' på svaret.
</p>

<p class="codeblock flow-text">data = r.json()
print(data) # Man kan printe hele dictionary til konsollen.
print(data['ID']) # Eller man kan printe et enketlt af felterne i dictionary'et.
</p>

<p class="flow-text light">
  Nu kan vi sende svaret tilbage til serveren. Svaret skal pakkes i et  'dictionary' som vist nedenfor (udskift '%UniqueID' og '%inputData' med værdierne vi modtog fra serveren).
</p>
<p class="codeblock flow-text">questAnswer =
    {
        'cmd'        : 'answer',
        'ID'         : %UniqueID # Det samme ID som vi modtog fra serveren.
        'outputData' : %inputData # Vi sender det som vi modtog fra serveren tilbage igen.
    }
</p>
<p class="flow-text light">
  Prøv nu at sende dette 'dictionary' til servern, på samme måde som ovenfor, og se hvilket svar du får fra webserveren.
</p>
'''